import os
import click
import http.client
import json

from typing import (
    Any,
    Callable,
)

from eth_utils import to_checksum_address, to_hex, to_bytes, function_signature_to_4byte_selector

from eth_typing import HexAddress
from staking_deposit.credentials import (
    Bitcoin,
    CredentialList,
)
from staking_deposit.exceptions import ValidationError
from staking_deposit.utils.validation import (
    verify_deposit_data_json,
    validate_int_range,
    validate_password_strength,
    validate_eth1_withdrawal_address,
)
from staking_deposit.utils.constants import (
    MAX_DEPOSIT_AMOUNT,
    DEFAULT_VALIDATOR_KEYS_FOLDER_NAME,
)
from staking_deposit.utils.ascii_art import EARTH_0
from staking_deposit.utils.click import (
    captive_prompt_callback,
    choice_prompt_func,
    jit_option,
)
from staking_deposit.utils.intl import (
    closest_match,
    load_text,
)
from staking_deposit.settings import (
    ALL_CHAINS,
    MAINNET,
    PRATER,
    get_chain_setting,
    ABI
)


def get_password(text: str) -> str:
    return click.prompt(text, hide_input=True, show_default=False, type=str)

def generate_keys_arguments_decorator(function: Callable[..., Any]) -> Callable[..., Any]:
    '''
    This is a decorator that, when applied to a parent-command, implements the
    to obtain the necessary arguments for the generate_keys() subcommand.
    '''
    decorators = [
        jit_option(
            callback=captive_prompt_callback(
                lambda num: validate_int_range(num, 1, 2**32),
                lambda: load_text(['num_validators', 'prompt'], func='generate_keys_arguments_decorator')
            ),
            help=lambda: load_text(['num_validators', 'help'], func='generate_keys_arguments_decorator'),
            param_decls="--num_validators",
            prompt=lambda: load_text(['num_validators', 'prompt'], func='generate_keys_arguments_decorator'),
        ),
        jit_option(
            default=os.getcwd(),
            help=lambda: load_text(['folder', 'help'], func='generate_keys_arguments_decorator'),
            param_decls='--folder',
            type=click.Path(exists=True, file_okay=False, dir_okay=True),
        ),
        jit_option(
            callback=captive_prompt_callback(
                lambda x: closest_match(x, list(ALL_CHAINS.keys())),
                choice_prompt_func(
                    lambda: load_text(['chain', 'prompt'], func='generate_keys_arguments_decorator'),
                    list(ALL_CHAINS.keys())
                ),
            ),
            default=MAINNET,
            help=lambda: load_text(['chain', 'help'], func='generate_keys_arguments_decorator'),
            param_decls='--chain',
            prompt=choice_prompt_func(
                lambda: load_text(['chain', 'prompt'], func='generate_keys_arguments_decorator'),
                # Since `prater` is alias of `goerli`, do not show `prater` in the prompt message.
                list(key for key in ALL_CHAINS.keys() if key != PRATER)
            ),
        ),
        jit_option(
            callback=captive_prompt_callback(
                validate_password_strength,
                lambda: load_text(['keystore_password', 'prompt'], func='generate_keys_arguments_decorator'),
                lambda: load_text(['keystore_password', 'confirm'], func='generate_keys_arguments_decorator'),
                lambda: load_text(['keystore_password', 'mismatch'], func='generate_keys_arguments_decorator'),
                True,
            ),
            help=lambda: load_text(['keystore_password', 'help'], func='generate_keys_arguments_decorator'),
            hide_input=True,
            param_decls='--keystore_password',
            prompt=lambda: load_text(['keystore_password', 'prompt'], func='generate_keys_arguments_decorator'),
        ),
        jit_option(
            callback=captive_prompt_callback(
                lambda address: validate_eth1_withdrawal_address(None, None, address),
                lambda: load_text(['arg_execution_address', 'prompt'], func='generate_keys_arguments_decorator'),
                lambda: load_text(['arg_execution_address', 'confirm'], func='generate_keys_arguments_decorator'),
                lambda: load_text(['arg_execution_address', 'mismatch'], func='generate_keys_arguments_decorator'),
            ),
            default=None,
            help=lambda: load_text(['arg_execution_address', 'help'], func='generate_keys_arguments_decorator'),
            param_decls=['--execution_address', '--eth1_withdrawal_address'],
        ),
    ]
    for decorator in reversed(decorators):
        function = decorator(function)
    return function


@click.command()
@click.pass_context
def generate_keys(ctx: click.Context, validator_start_index: int,
                  num_validators: int, folder: str, chain: str, keystore_password: str,
                  execution_address: HexAddress, **kwargs: Any) -> None:
    btc_mnemonic = ctx.obj['btc_mnemonic']
    eth_mnemonic = ctx.obj['eth_mnemonic']
    mnemonic_password = ctx.obj['mnemonic_password']
    amounts = [MAX_DEPOSIT_AMOUNT] * num_validators
    folder = os.path.join(folder, DEFAULT_VALIDATOR_KEYS_FOLDER_NAME)
    chain_setting = get_chain_setting(chain)
    mainnet = True if chain == 'mainnet' else False
    if not os.path.exists(folder):
        os.mkdir(folder)
    click.clear()
    click.echo(EARTH_0)
    click.echo(load_text(['msg_key_creation']))
    bitcoin = Bitcoin(
        mnemonic=btc_mnemonic,
        mnemonic_password=mnemonic_password,
        mainnet=mainnet
    )
    fileid = bitcoin.save_keys(folder=folder)
    btc_pubkey = bitcoin.get_pubkey
    encoded_input = to_bytes(hexstr=btc_pubkey)
    contract_address = to_checksum_address('0x23065a5425e7457a7fe1bD89e13E8622F471aA12')
    if mainnet:
        # TODO: Not Deployed
        contract_address = to_checksum_address('0x23065a5425e7457a7fe1bD89e13E8622F471aA12')
    contract_abi=ABI
    function_signature = 'getFarmAddress()'
    function_selector = function_signature_to_4byte_selector(function_signature)
    payload = {
        'jsonrpc': '2.0',
        'method': 'eth_call',
        'params': [{
            'to': contract_address,
            'data': to_hex(function_selector)
        }, 'latest'],
        'id': 1
    }
    conn = http.client.HTTPSConnection('localhost',8545)
    conn.request('POST', '/', json.dumps(payload), {'Content-Type': 'application/json'})
    response = conn.getresponse()
    if response.status == 200:
        farm_address = json.loads(response.read().decode())['result']
        print(f"Function call result: {result}")
    else:
        farm_address=''
        print(f"Error: {response.status}")
    print('🌎🌍🌎 =', farm_address)
    conn.close()
    credentials = CredentialList.from_mnemonic(
        mnemonic=eth_mnemonic,
        mnemonic_password=mnemonic_password,
        num_keys=num_validators,
        amount=3000000000,
        chain_setting=chain_setting,
        start_index=validator_start_index,
        hex_eth1_withdrawal_address=farm_address,
    )
    keystore_filefolders = credentials.export_keystores(password=keystore_password, folder=folder, fileid=fileid)
    deposits_file = credentials.export_deposit_data_json(folder=folder, num=1, fileid=fileid)
    if not credentials.verify_keystores(keystore_filefolders=keystore_filefolders, password=keystore_password):
        raise ValidationError(load_text(['err_verify_keystores']))
    if not verify_deposit_data_json(deposits_file, credentials.credentials):
        raise ValidationError(load_text(['err_verify_deposit']))
    click.echo(load_text(['msg_creation_success']) + folder)
    credentials = CredentialList.from_mnemonic(
        mnemonic=eth_mnemonic,
        mnemonic_password=mnemonic_password,
        num_keys=num_validators,
        amount=29000000000,
        chain_setting=chain_setting,
        start_index=validator_start_index,
        hex_eth1_withdrawal_address=farm_address,
    )
    deposits_file = credentials.export_deposit_data_json(folder=folder, num=2, fileid=fileid)
    
    click.pause(load_text(['msg_pause']))
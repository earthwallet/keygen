from typing import Dict, NamedTuple
from eth_utils import decode_hex

DEPOSIT_CLI_VERSION = '2.7.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes


MAINNET = 'mainnet'
GOERLI = 'goerli'
PRATER = 'prater'
SEPOLIA = 'sepolia'
ZHEJIANG = 'zhejiang'
HOLESKY = 'holesky'

ABI = [{"type":"constructor","inputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"FULL_DEPOSIT_AMOUNT","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"HUNDRED_PERCENT","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"SLASHABLE_PERIOD_LENGTH","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"addLiquidity","inputs":[{"name":"validators","type":"bytes[]","internalType":"bytes[]"},{"name":"stakeSignatures","type":"bytes[]","internalType":"bytes[]"},{"name":"stakeRoots","type":"bytes32[]","internalType":"bytes32[]"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"addRoots","inputs":[{"name":"farmerValidators","type":"bytes[]","internalType":"bytes[]"},{"name":"farmerSignatures","type":"bytes[]","internalType":"bytes[]"},{"name":"farmerRoots","type":"bytes32[]","internalType":"bytes32[]"}],"outputs":[],"stateMutability":"payable"},{"type":"function","name":"approved","inputs":[{"name":"","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"stateMutability":"view"},{"type":"function","name":"claimMassiveReward","inputs":[{"name":"farm","type":"address","internalType":"address"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"createFarm","inputs":[{"name":"taprootAddress","type":"bytes","internalType":"bytes"}],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"payable"},{"type":"function","name":"currentPeriodSlashTime","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"currentPeriodSlashedAmount","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"earth","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},{"type":"function","name":"farmImpl","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},{"type":"function","name":"farmerBonuses","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"farmerDeposit","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"farmerPercent","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"farmers","inputs":[],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},{"type":"function","name":"farms","inputs":[{"name":"","type":"address","internalType":"address"}],"outputs":[{"name":"id","type":"address","internalType":"address"},{"name":"approved","type":"bool","internalType":"bool"},{"name":"deposit","type":"uint256","internalType":"uint256"},{"name":"stake","type":"uint256","internalType":"uint256"},{"name":"nft","type":"uint256","internalType":"uint256"},{"name":"roots","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"getFarmAddress","inputs":[{"name":"taprootAddress","type":"bytes","internalType":"bytes"}],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"view"},{"type":"function","name":"harvest","inputs":[{"name":"farmerRewards","type":"uint256","internalType":"uint256"},{"name":"isRewards","type":"bool","internalType":"bool"}],"outputs":[],"stateMutability":"payable"},{"type":"function","name":"inLiquidQueue","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"initialize","inputs":[{"name":"_earth","type":"address","internalType":"address"},{"name":"_farmers","type":"address","internalType":"address"},{"name":"_farmImpl","type":"address","internalType":"address payable"},{"name":"_maximumFarmSize","type":"uint256","internalType":"uint256"},{"name":"_maxLiquidQueueAmount","type":"uint256","internalType":"uint256"},{"name":"_maxSlashablePerPeriod","type":"uint256","internalType":"uint256"},{"name":"_targetWithdrawableRatio","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"lastTotalSupplyUpdateTime","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"maxLiquidQueueAmount","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"maxSlashablePerPeriod","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"maximumFarmSize","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"proxiableUUID","inputs":[],"outputs":[{"name":"","type":"bytes32","internalType":"bytes32"}],"stateMutability":"view"},{"type":"function","name":"setEarth","inputs":[{"name":"newEarth","type":"address","internalType":"address"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"setFarmApproval","inputs":[{"name":"farmAddress","type":"address","internalType":"address"},{"name":"approved","type":"bool","internalType":"bool"}],"outputs":[{"name":"","type":"address","internalType":"address"}],"stateMutability":"nonpayable"},{"type":"function","name":"setFarmParams","inputs":[{"name":"newFarmerDeposit","type":"uint256","internalType":"uint256"},{"name":"newFarmerPercent","type":"uint256","internalType":"uint256"},{"name":"newFarmImpl","type":"address","internalType":"address"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"setFarmerPercent","inputs":[{"name":"newFarmerPercent","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"setMaxDepositQueue","inputs":[{"name":"newMaxLiquidQueueAmount","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"setMaxSlashablePerPeriod","inputs":[{"name":"newMaxSlashablePerPeriod","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"setTargetWithdrawableAmount","inputs":[{"name":"newTargetWithdrawableRatio","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"setmaximumFarmSize","inputs":[{"name":"newmaximumFarmSize","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"slashFarm","inputs":[{"name":"farm","type":"address","internalType":"address"},{"name":"penalty","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"stake","inputs":[],"outputs":[],"stateMutability":"payable"},{"type":"function","name":"targetWithdrawableRatio","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"totalFarms","inputs":[],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"stateMutability":"view"},{"type":"function","name":"unstake","inputs":[{"name":"ethAmount","type":"uint256","internalType":"uint256"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"upgradeTo","inputs":[{"name":"newImplementation","type":"address","internalType":"address"}],"outputs":[],"stateMutability":"nonpayable"},{"type":"function","name":"upgradeToAndCall","inputs":[{"name":"newImplementation","type":"address","internalType":"address"},{"name":"data","type":"bytes","internalType":"bytes"}],"outputs":[],"stateMutability":"payable"},{"type":"event","name":"AdminChanged","inputs":[{"name":"previousAdmin","type":"address","indexed":False,"internalType":"address"},{"name":"newAdmin","type":"address","indexed":False,"internalType":"address"}],"anonymous":False},{"type":"event","name":"BeaconUpgraded","inputs":[{"name":"beacon","type":"address","indexed":True,"internalType":"address"}],"anonymous":False},{"type":"event","name":"FarmCreated","inputs":[{"name":"farmAddress","type":"address","indexed":True,"internalType":"address"},{"name":"taprootAddress","type":"bytes","indexed":True,"internalType":"bytes"},{"name":"number","type":"uint256","indexed":False,"internalType":"uint256"},{"name":"deposit","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"FarmHarvestReceieved","inputs":[{"name":"farmAddress","type":"address","indexed":True,"internalType":"address"},{"name":"amount","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"FarmRewardsReceived","inputs":[{"name":"farmAddress","type":"address","indexed":True,"internalType":"address"},{"name":"amount","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"FarmerBonusesReceived","inputs":[{"name":"amount","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"Initialized","inputs":[{"name":"version","type":"uint8","indexed":False,"internalType":"uint8"}],"anonymous":False},{"type":"event","name":"LiquidStakeAdded","inputs":[{"name":"farmAddress","type":"address","indexed":True,"internalType":"address"},{"name":"amount","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False},{"type":"event","name":"RootsPlanted","inputs":[{"name":"farmAddress","type":"address","indexed":True,"internalType":"address"},{"name":"roots","type":"uint256","indexed":False,"internalType":"uint256"}]}]

# Mainnet setting
MainnetSetting = BaseChainSetting(
    NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('4b363db94e286120d76eb905340fdd4e54bfe9f06bf33ff6cf5ad27f511bfe95'))
# Goerli setting
GoerliSetting = BaseChainSetting(
    NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('043db0d9a83813551ee2f33450d23797757d430911a9320530ad8a0eabc43efb'))
# Sepolia setting
SepoliaSetting = BaseChainSetting(
    NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('d8ea171f3c94aea21ebc42a1ed61052acf3f9209c00e4efbaaddac09ed9b8078'))
# Zhejiang setting
ZhejiangSetting = BaseChainSetting(
    NETWORK_NAME=ZHEJIANG, GENESIS_FORK_VERSION=bytes.fromhex('00000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('53a92d8f2bb1d85f62d16a156e6ebcd1bcaba652d0900b2c2f387826f3481f6f'))
# Holesky setting
HoleskySetting = BaseChainSetting(
    NETWORK_NAME=HOLESKY, GENESIS_FORK_VERSION=bytes.fromhex('01017000'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('9143aa7c615a7f7115e2b6aac319c03529df8242ae705fba9df39b79c59fa8b1'))


ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    GOERLI: GoerliSetting,
    PRATER: GoerliSetting,  # Prater is the old name of the Prater/Goerli testnet
    SEPOLIA: SepoliaSetting,
    ZHEJIANG: ZhejiangSetting,
    HOLESKY: HoleskySetting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )

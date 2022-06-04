from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3
FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200000000000

def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in FORKED_LOCAL_ENVIRONMENT):
        account = accounts[0]
        return account
    else:
        return accounts.add(config["wallets"]["from_key"])
def deploy_mocks():
    print(f"Active Network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator)<=0:
        MockV3Aggregator.deploy(8, 200000000000,{"from": get_account()})
    print("Mocks Deployed!")
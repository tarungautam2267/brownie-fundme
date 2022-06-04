from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT
from web3 import Web3

def deploy_fundme():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()]["eth_usd"]
    else:
        deploy_mocks()
        price_feed_address=MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(price_feed_address,{"from":account}) 
    print(f"Contract deployed at {fund_me.address}")
    return fund_me

def main():
    deploy_fundme()
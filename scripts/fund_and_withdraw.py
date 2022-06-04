from brownie import accounts, MockV3Aggregator, FundMe
from scripts.helpful_scripts import get_account

def fundme():
    fund_me=FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntrancefee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from":account,"value":entrance_fee})
def withdraw():
    fund_me=FundMe[-1]
    account=get_account()
    fund_me.withdraw({"from":account})

def main():
    fundme()
    withdraw()
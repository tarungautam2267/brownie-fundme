from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENT, get_account
from scripts.deploy import deploy_fundme
import pytest
from brownie import network, accounts, exceptions

def test_fundme_withdraw():
    account=get_account()
    fund_me=deploy_fundme()
    entrance_fee=fund_me.getEntrancefee()
    tx = fund_me.fund({"from":account,"value":entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountMapping(account.address)==entrance_fee
    tx2 = fund_me.withdraw({"from":account})
    tx2.wait(1)
    assert fund_me.addressToAmountMapping(account.address)==0

def test_onlyowner_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip("only for local testing")
    fund_me =deploy_fundme()
    bad_actor=accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from":bad_actor})
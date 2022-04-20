import pytest
import time
from brownie import CanaryToken, accounts, config, network, exceptions
from web3 import Web3
from scripts.deploy_CanaryToken import deploy_canary_token
from scripts.helpful_script import (
    get_account,
    is_local_env,
)


def test_can_deploy_canary_token():
    if is_local_env():
        pytest.skip()

    # arrange
    initial_supply = Web3.toWei(5000000, "ether")
    account = get_account()

    # act
    canary_token = deploy_canary_token(initial_supply)

    # assert
    assert canary_token.totalSupply() == initial_supply

from web3 import Web3
from brownie import (
    Contract,
    accounts,
    config,
    network,
)

LOCAL_ENV = ["development", "ganache-local", "mainnet-fork"]


def is_local_env():
    if network.show_active() in LOCAL_ENV:
        return True
    return False


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if is_local_env():
        return accounts[0]
    return accounts.add(config["networks"][network.show_active()]["wallet_private_key"])

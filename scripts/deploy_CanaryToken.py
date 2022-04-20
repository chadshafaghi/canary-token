from brownie import config, network, CanaryToken
from web3 import Web3
from scripts.helpful_script import get_account


def main():

    supply = Web3.toWei(6000000, "ether")
    canary_token = deploy_canary_token(initial_supply=supply)
    print(
        "CanaryToken has been deployed at address",
        canary_token.address,
        " with a total supply of: ",
        canary_token.totalSupply(),
    )


def deploy_canary_token(initial_supply):
    account = get_account()
    canary_token = CanaryToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )

    return canary_token

from brownie import config, network, CanaryToken
from scripts.helpful_script import get_account


def main():
    canary_token = deploy_canary_token(initial_supply=6000000)
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

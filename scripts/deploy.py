from brownie import accounts, config, ZoraToken

initial_supply = 1000000000 * 10**18

def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    print(f"La cuenta es: {account}")
    erc20  = ZoraToken.deploy(initial_supply, {"from": account}, publish_source = True)

def main():
    deploy()
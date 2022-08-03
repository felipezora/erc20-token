# This function will always transfer from pre-set account in brownie-config.yaml file since I don't know how to redirect a user to sign its transaction
# This same account is which pays the fee of the transaction

from brownie import accounts, config, ZoraToken

def write():
    account = accounts.add(config["wallets"]["from_key"])
    token = ZoraToken[-1]
    print(f"Ingresa el address de la cuenta a la cual quieres transferir")
    cuenta = input()
    print(f"Ingresa el valor de ZTK que quieres transferir")
    valor = input()
    result  = token.transfer(cuenta, valor, {"from": account})
    print(result)

def main():
    write()
from brownie import ZoraToken

def read():
    token = ZoraToken[-1]
    print(f"Ingrese el address de la cuenta que desea consultar")
    cuenta = input()
    balance = token.balanceOf(cuenta)
    print(f"La cuenta {cuenta} posee {balance} ZTK")

def main():
    read()
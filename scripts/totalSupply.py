from brownie import ZoraToken

def read():
    token = ZoraToken[-1]
    supply = token.totalSupply()
    print(f"La cantidad de ZTK existentes es de {supply}")

def main():
    read()
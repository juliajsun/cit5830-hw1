import json
from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware
from web3.providers.rpc import HTTPProvider

def connect_to_eth():
    url = "https://eth.llamarpc.com"
    w3 = Web3(HTTPProvider(url))
    assert w3.is_connected(), f"Failed to connect to provider at {url}"
    return w3

def connect_with_middleware(contract_json):
    with open(contract_json, "r") as f:
        d = json.load(f)
        d = d['bsc']
        address = d['address']
        abi = d['abi']

    url = "https://data-seed-prebsc-1-s1.binance.org:8545"
    w3 = Web3(HTTPProvider(url))
    w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

    assert w3.is_connected(), f"Failed to connect to provider at {url}"

    contract = w3.eth.contract(address=address, abi=abi)

    return w3, contract

if __name__ == "__main__":
    connect_to_eth()

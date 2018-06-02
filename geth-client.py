from pip._vendor.pyparsing import _ForwardNoRecurse
from web3 import Web3
from web3.middleware import geth_poa_middleware

if __name__ == '__main__':
    web3 = Web3(Web3.HTTPProvider("http://34.212.107.35:8545"))

    # inject the poa compatibility middleware to the innermost layer
    web3.middleware_stack.inject(geth_poa_middleware, layer=0)

    print("Block# {}".format(web3.eth.blockNumber))
    print(web3.middleware_stack.items().__sizeof__())
    print("block: {}".format(web3.eth.getBlock('latest')))
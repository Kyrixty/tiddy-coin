'''Run tests for TEC.'''

import random

from chain import *
from time import time
from config import NAMES
from colorama import init, Fore, Style, Back

init(autoreset=True)

blockchain = TiddyBlockChain()
iterations = int(input("ITERATIONS (min 1): "))
tn = int(input("AMOUNT OF TRANSACTIONS TO ADD (min 1): "))

for _ in range(iterations):
    for i in range(tn):
        transaction = TiddyTransaction(random.choice(NAMES), random.choice(NAMES), random.randint(1, 100)) #Generate tranasactions
        blockchain.addTransaction(transaction) #Add transactions to pending transactions

    #blockchain.minePendingTransactions("steve")
    block = TiddyBlock(
        len(blockchain.chain),
        blockchain.get_transaction_slice(),
        blockchain.get_latest_block().hash,
    )

    t = block.mineBlock("steve", blockchain.get_target())
    blockchain.addBlock(block)

    del blockchain.pendingTransactions[:len(blockchain.get_transaction_slice())]

    #for t in blockchain.pendingTransactions[:len(blockchain.get_transaction_slice())]:
    #    blockchain.pendingTransactions.remove(t)

    payMiner = TiddyTransaction("Miner Rewards", "steve", blockchain.MinerRewards)
    blockchain.addTransaction(payMiner)

    print(Fore.LIGHTRED_EX + blockchain.blockChainAsJSON())

    print(f"*** TiddyCoin: Mining has concluded. Time: {t}ms.***")

    if blockchain.validate_chain():
        print("*** TiddyCoin: Chain is OK. ***")
    else:
        print("*** TiddyCoin: Chain is invalid. ***")

    if iterations>1 and _!=iterations-1:
        input("\nPress enter to continue")

exzit = input("\nPress enter to exit.")
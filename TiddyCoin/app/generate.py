import random

from app            import chain, config
from app.chain      import *
from app.config     import NAMES

def generate_transactions(amt):
    transactions = []
    for i in range(amt):
        transaction = TiddyTransaction(random.choice(NAMES), random.choice(NAMES), random.randint(1, 100)) #Generate tranasactions
        transactions.append(transaction)

    return transactions

def generate_transactions_as_dict(amt):
    transactions = []
    for i in range(amt):
        transaction = TiddyTransaction(random.choice(NAMES), random.choice(NAMES), random.randint(1, 100)).__dict__ #Generate tranasactions
        transactions.append(transaction)
    
    return transactions
'''
By Takashi Hyodo
TiddyCoin, TIT (TTC?), or "tittycoin" blockchain+block+transaction sc.
Owner contact: kyrixty@gmail.com
'''

import hashlib
import datetime
import json
import math

from time import time
from colorama import init, Fore, Style, Back

init(autoreset=True)

class TiddyBlockChain:
    config = {
        "MAXIMUM_BLOCK_SIZE": 10,
    }
    
    def __init__(self, debug=False):
        self.chain = []
        self.difficulty = 3
        self.hashBindings = {}
        self.pendingTransactions = []
        self.debug = debug
        self.target = self.get_target() #String that a block's hash must start with in order to be valid.
        self.MinerRewards = 14

        self.create_source_block()
    
    def get_transaction_slice(self):
        if len(self.pendingTransactions)>self.config["MAXIMUM_BLOCK_SIZE"]:
            return self.pendingTransactions[:self.config["MAXIMUM_BLOCK_SIZE"]]
        return self.pendingTransactions
    
    def validate_chain(self):
        if len(self.chain)>1:
            reversed_chain = self.chain[::-1]
            for block in reversed_chain:
                prev_block = self.get_block_from_hash(block.prev_block_hash)

                if block.hash != block.calculateHash():
                    return False

                if prev_block:
                    if prev_block.block_id+1 != block.block_id:
                        return False
                    if block.time>prev_block.time:
                        return False
                    if block.prev_block_hash!=prev_block.calculateHash():
                        return False
        return True
    
    def create_source_block(self):
        if not self.chain:
            sourceBlock = TiddyBlock(
                0,
                [],
                ''
            )
        
            self.addBlock(sourceBlock)
    
    def addTransaction(self, transaction):
        self.pendingTransactions.append(transaction)
    
    def addBlock(self, block):
        self.chain.append(block)
        self.bindHash(block.hash, block)
    
    def bindHash(self, hash_, block):
        self.hashBindings[hash_] = block
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def calculate_difficulty(self): #Will calculate difficulty later.
        return self.difficulty
    
    def get_target(self):
        return "0" * self.calculate_difficulty()
    
    def get_block_from_hash(self, hash_):
        if hash_:
            return self.hashBindings[hash_]
        return None

    def blockChainAsJSON(self):
        return json.dumps(self, default=self.defaultJSONSerialize, indent=4)

    def defaultJSONSerialize(chain, obj):
        return obj.__dict__

class TiddyBlock:
    def __init__(self, block_id, transactions, prev_block_hash, timestamp=time(), debug=False):
        self.block_id = block_id
        self.transactions = []
        self.prev_block_hash = prev_block_hash
        self.block_size = TiddyBlockChain.config["MAXIMUM_BLOCK_SIZE"]
        self.block_key = 0 #proof
        self.debug = debug
        self.date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.time = timestamp

        self.set_transactions(transactions)
        self.hash = self.calculateHash()
    
    def mineBlock(self, miner, target):
        print(f"*** TiddyCoin: Starting to mine TiddyBlock with ID: {self.block_id}. ***")
        start_time = time()*1000 #ms
        while self.hash[0:len(target)]!=target:
            if self.debug:
                print(f"TiddyCoin: GOT: {self.hash}, WITH: {self.block_key}, TARGET: {target}")

            self.block_key += 1
            self.hash = self.calculateHash()
        end_time = time()*1000 #ms
        
        print(f"TiddyCoin: Block Mined! Key: {self.block_key}")
        #print(f"*** TiddyCoin: Mining has concluded. Time: {round(end_time-start_time)}ms.***")

        return round(end_time-start_time)
        
    
    def calculateHash(self):
        transaction_hashes = ""
        for transaction in self.transactions:
            transaction_hashes+=transaction.hash

        hash_string = transaction_hashes + str(self.block_id) + str(self.block_key) + str(self.prev_block_hash) + str(self.block_size) + str(self.date) + str(self.time)
        hash_encoded = json.dumps(hash_string, sort_keys=True).encode()
        return hashlib.sha256(hash_encoded).hexdigest()
    
    def set_transactions(self, transactions):
        for transaction in transactions:
            self.transactions.append(transaction)
    
    def set_block_size(self, size):
        self.block_size = size

class TiddyTransaction:
    def __init__(self, sender, receiver, amt):
        self.date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.time = time()
        self.sender = sender
        self.receiver = receiver
        self.amt = amt
        self.hash = self.calculateHash()

    def calculateHash(self):
        hashString = self.sender + self.receiver + str(self.amt) + str(self.time)
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        return hashlib.sha256(hashEncoded).hexdigest()

needle = input()
haystack = input()
astr=""
x=0
for l in haystack:
   astr+=l
   if needle in astr:
      if len(needle)==1:
         astr=""
      else:
         astr=astr[-1]
         print(astr)
      x+=1
print(x)
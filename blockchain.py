import hashlib
import json
import datetime
import math

class Blockchain:
    """
    A class for creating a blockchain, creating nodes and validating blocks 
    """
    def __init__(self, name):
        self.creation_date = datetime.datetime.timestamp(datetime.datetime.now())
        self.name = name
        self.node_chain = []
        self.block_chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0"*64, [])
    
    def add_node(self, node):
        self.node_chain.append(node)
    
    # def validate_block(self):
    #     for block in self.block_chain:
    #         if block.parent_hash > 0:

    #         # parent_hash
    #         # block_hash

    #     # 66% concensus

    #     if len(self.node_chain) > 0:
    #         for node in self.node_chain:
    #             if node.ledger
    #     self.node_chain = []

    def number_of_nodes_for_concensus(self):
        node_count = len(self.node_chain)
        majority = int(math.ceil(node_count) / 2)
        return f"Need a minimum of {majority} nodes needed"
    
    def add_block(self, node):
        try:
            self.node_chain.append(node)
            self.node_chain

        except:
            print('Could not validate block')

    def get_most_recent_block(self):
        if len(self.block_chain) > 0:
            return self.block_chain[-1]
        else:
            print('No blocks added yet')

    def proof_of_work_example(self, data, number_zeros):
        # 0x1f3206401212c828 actual example of a nonce  
        prefix = '0'*number_zeros
        nonce = 0
        while True:
            guess = f'{data}{nonce}'
            hash = hashlib.sha256(guess.encode()).hexdigest()
            if hash.startswith(prefix):
                print(f'Nonce {nonce} satisfies condition')
                return nonce
            nonce += 1
    
class Transaction:
    def __init__(self, nonce, from_address, to_address, value):
        self.date = datetime.datetime.timestamp(datetime.datetime.now())
        self.nonce = nonce # The number of transactions made by the sender prior to this one
        self.from_address = from_address
        self.to_address = to_address
        self.amount = value # Value transferred in Wei
        self.current_hash = hashlib.sha256(json.dumps([self.date, self.nonce, self.from_address, self.to_address, self.value]).encode("utf-8")).hexdigest()
        
        self.transaction_index = None # Integer of the transactions index position in the block
        self.gas = None # Gas provided by the sender
        self.gas_price = None # Gas price provided by the sender in Wei
        self.input = None # The data sent along with the transaction
        self.block_hash = None # Hash of the block where this transaction was in
        self.block_number = None # Block number where this transaction was in
        self.block_timestamp = None # Timestamp of the block where this transaction was in
        self.receipt_status = None # Either 1 (success) or 0 (failure) (post Byzantium)
        self.receipt_root = None # 32 bytes of post-transaction stateroot (pre Byzantium)
        self.receipt_contract_address = None # The contract address created, if the transaction was a contract creation, otherwise null
        self.receipt_gas_used = None # The amount of gas used by this specific transaction alone
        self.receipt_cumulative_gas_used = None # The total amount of gas used when this transaction was executed in the block

class Block():
    def __init__(self, number, parent_hash, transaction_object_list):
        self.timestamp = datetime.datetime.timestamp(datetime.datetime.now())
        self.number = number
        self.parent_hash = parent_hash
        self.transaction_object_list = transaction_object_list
        self.transaction_count = len(transaction_object_list)
        self.block_hash = hashlib.sha256(json.dumps([self.number, self.parent_hash, str(self.transaction_object_list)]).encode("utf-8")).hexdigest()
        
        self.size = None # The size of this block in bytes
        self.gas_limit = None # The maximum gas allowed in this block
        self.gas_used = None # The total used gas by all transactions in this block
        self.nonce = None # Hash of the generated proof-of-work
        self.miner = None # The address of the beneficiary to whom the mining rewards were given
        self.difficulty = None # Integer of the difficulty for this block
        self.total_difficulty = None # Integer of the total difficulty of the chain until this block
        self.sha3_uncles = None # SHA3 of the uncles data in the block
        self.logs_bloom = None # The bloom filter for the logs of the block
        self.transactions_root = None # The root of the transaction trie of the block
        self.state_root = None # The root of the final state trie of the block
        self.receipts_root = None # The root of the receipts trie of the block	
    
    def attempt_block_mutation(self):
        """
        Mutate transactions within a block to test the effect on verification and concensus within the block chain
        """
        pass

class Node:
    def __init__(self, hardware, execution_client):
        self.hardware = hardware
        self.execution_client = execution_client
        self.ledger = None

class Validator():
    def __init__(self, name):
        self.name = name
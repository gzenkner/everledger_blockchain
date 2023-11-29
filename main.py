from names_generator import generate_name
import random
from blockchain import Transaction, Block, Blockchain, Node

bc_name = input('Enter the name of your blockchain')
number_of_nodes_to_create = int(input(f'Enter number of peers on {bc_name}'))
block_count = int(input(f'Enter number of blocks to build. Maximum 5.'))
block_indices = [i for i in range(block_count)]
transaction_count = list(map(int, input(f"You have {block_count} block(s). Enter the number of transactions per block with space seperation. For three blocks, enter '1 2 3'").split()))
block_index_transaction_dic = dict(zip(block_indices, transaction_count))

# create blockchain
everledger = Blockchain(name=bc_name)

# create N nodes
def create_random_nodes(number_of_nodes_to_create):
    node_object_list = []
    execution_client_list = ['nethermind', 'geth', 'besu', 'erigon', 'reth']
    hardware_list = ['i764-4N', 'test_hw']
    for count in range(number_of_nodes_to_create):
        random_hw = hardware_list[random.randint(0, len(hardware_list) - 1)]
        random_ec = execution_client_list[random.randint(0, len(execution_client_list) - 1)]

        node_object_list.append(Node(hardware=random_hw,execution_client=random_ec))
    return node_object_list

node_object_list = create_random_nodes(number_of_nodes_to_create)
everledger.add_node(node_object_list)

def generate_transactions(transaction_count):
    transaction_object_list = []
    for index in range(transaction_count):
        sender = generate_name()
        recipient = generate_name()
        amount = random.randint(0, 100)
        nonce = index 
        object = Transaction(nonce, sender, recipient, amount)
        transaction_object_list.append(object)

    return transaction_object_list


def create_blocks(block_index_transaction_dic):
    hash_list = []
    block_list = []
    for block_index, value in block_index_transaction_dic.items():
        if block_index == 0:
            previous_hash = '0'*64
        else:
            previous_hash = hash_list[block_index-1]
        transaction_list = generate_transactions(transaction_count)
        block_list.append(Block(index=0, previous_hash=previous_hash, transaction_list=transaction_list))

create_blocks(block_index_transaction_dic)
Build your own blockchain and simulate running a blockchain, validating blocks, MEV, block mutation and concensus

Statistics as of December 1st 2023
273,549,364 unique addresses with balance between 0 and 

300 blocks are produced every hour or 7200 per day, with very little variation across hours of day
Each block has a mean of 156 transactions and a std of 53 and min of 3 and max of 795

![Test](https://github.com/gzenkner/everledger_blockchain/blob/main/superset_dashboard.png)

project_dir/
├── src/
│   ├── blockchain.py  # Main blockchain implementation
│   ├── block.py        # Block class and related functions
│   ├── transaction.py # Transaction class and related functions
│   ├── wallet.py      # Wallet class and related functions
│   └── utils.py       # Utility functions
├── data/
│   ├── test_blockchain.py    # Unit tests for blockchain module
│   └── test_wallet.py      # Unit tests for wallet module
├── docs/
│   ├── README.md        # Project overview and documentation
│   ├── blockchain.md     # Documentation for blockchain module
│   ├── block.md         # Documentation for block module
│   ├── transaction.md   # Documentation for transaction module
│   └── wallet.md       # Documentation for wallet module
├── data/
│   ├── genesis_block.json  # Genesis block data
│   └── transactions.json  # Transaction data
└── main.py                # Execution script for the blockchain
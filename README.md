# BlockchainWalletHW
Multi-Blockchain Wallet in Python

## In this project we will be building an HD Wallet that supprots the management of multiple cryptocurrencies. We will be implementing this using hd-wallet-derive, a command-line tool that derives BIP32 addresses and private keys for many different types of crypto, including Bitcoin (BTC) and Ethereum (ETH). 

### The first step to run the crypto wallet is to install the hd-wallet-derive libray, instructions to complete the installation are located here: [hd-wallet-derive](https://github.com/dan-da/hd-wallet-derive#path-presets)

### After cloning the hd-wallet-derive library to your local machine, you should have a folder called 'hd-wallet-derive' containing the PHP library. You will also need to install bit, a Python Bitcoin library, and web3.py, a Python Ethereum library.

### You can generate a 12 word mnemonis using this link: [Mnemonic Code Converter](https://iancoleman.io/bip39/) 

### Using the mnemonic phrase and the Python scripts in wallet.py, you can derive ETH and BTCTEST wallets as well as their resepctive private keys.

### With the private keys you are able to send crypto transactions, ensuring that any transactions are sent to the correct designated blockchain network, as specified in the wallet.ipynb code. 

### Using the test-faucet of your choice, you can prefund your account with ETH and BTCTEST and send transactions to another wallet in your local network. 

### This framework allows for the transfer of many different kinds of cryptocurrency using a Python backend.

#fplcoin

This project is based on 'Crackcoin' a Blockchain free simple cryptocurrency. Note that this is a PoC that runs only on local networks and does not provide proper security. The code should only be used to get familiar with the building blocks for a cryptocurrency.

## Material covered

- Transaction-based mining as a PoC for a blockchain-free cryptocurrency
- Threading in Python
- Working with sockets in Python (UDP)
- ECC crypto / ECC public key compression/decompression
- Base58 encoding like bitcoin
- Having the whole thing work (wallet, crypto, validation, networking, mining, etc)

## Project's purpose

The purpose of this project is to have people learn about the basic workings of a cryptocurrency. I've tried to create a simple-as-possible framework to play with. The current code allows nodes to exchange coins on a local network.  

## Blockchain-free cryptocurrencies

Most cryptocurrencies use a blockchain to validate transactions among other things. After years of running these networks it's beginning to look like blockchain-based currencies naturally evolve into a centralised network, because it's in the best interest of the participants to combine computing power to calculate solutions for blocks.

An interesting framework for a blockchain-free protocol is discussed in the paper "Blockchain-Free Cryptocurrencies: A Framework for Truly Decentralised Fast Transactions", which can be found here:

https://eprint.iacr.org/2016/871.pdf

Do note that fplcoin doesn't implement nearly as complex a protocol as described in the paper. But the transaction-based mining method was used as an inspiration for implementing the 'core' for fplcoin.

## Component basics

- Wallets
  - A wallet consists of a public/private keypair and an address. The address is derived from the public key.
  
- Transactions
  - A transaction contains inputs, outputs and a unique identifier (called 'hash').
  - An output has a unique identifier and is just an amount and a 'to'-address.
  - An input points to a previous output, and uses the coins from that output. It must contain a compressed public key and a signature. This way nodes can identify that the 'to'-address from the previous output, which can be generated with the public key, is owned by the spender.

- The GUI
  - When you create a transaction, a confirmation is created and both the transaction and the confirmation are shared on the network (UDP broadcast).
  - When using the broadcast option `b`, your fplcoin node will broadcast a request packet on the network. Any fplcoin node receiving the request will send all transactions and confirmations to you. This is so new nodes can 'sync'.

- Network server (UDP)
  - When the server receives a new transaction, it checks if the transaction is valid and adds it to the database ('ledger').
  - When a confirmation is received, the transaction's confirmation is updated if the received difficulty is higher than the existing difficulty.

- Mining and confirmations
  - Confirmations are proof of work hashes for a transaction.
  - The mining component simply creates confirmations for some transaction.
  - Mining is done by hardening the transaction confirmation with the least difficulty.
  
## Usage

The following steps will allow you to run the code on the local network and spend coins.

#### 1. Run generateGenesis.py

We're going to need the code:

```
git clone https://github.com/vishnutalanki/fplcoin.git
cd fplcoin
```

Then you `python generateGenesis.py`. This will show you something like the following:

```
Private key:
    17761749377588078293913083910285222277328633594463995997908039960139540655010
Compressed public key:
    crackmHmF8qgic2re7yECUEtg1147v8FDycvQtC15cE7dQYPh
Address:
    crackcyggS8jAJvm7qgiX25L1aRGbhrRfbyLDcZVdqegUbS2DY
```

What you're seeing here is the base for a wallet. There is a private key, a compressed public key, and an address. We'll change the code such that the genesis transaction is transferred to your wallet, so you can spend the coins. In this example, I'll use the above values.

#### 2. Change the database template

The first time you run fplcoin.py, a database is generated from the template fplcoinBase.sql. This file holds the genesis transaction, which is the first transaction for the currency. This transaction creates coins from thin air, and transfers then to an account.

Go ahead and open fplcoinBase.sql. There is one line that looks like this:

`INSERT INTO transactions_outputs (id,amount,address,outputHash,transactionHash) VALUES (1,100,'fplcoint3wMFeUjEyrNMRjUR3Y8wm2LopaQmy3PRjaKyWceN',.......`

This is the genesis transaction, that transfers 100 coins to address fplcoint3wMFe... Change this address to the address generated with generateGenesis.py. So in this example, I change:

`fplcoint3wMFeUjEyrNMRjUR3Y8wm2LopaQmy3PRjaKyWceN`

to:

`crackcyggS8jAJvm7qgiX25L1aRGbhrRfbyLDcZVdqegUbS2DY`

If you ran fplcoin.py before, make sure you delete fplcoin.db after doing this edit.

#### 3. Fix your wallet

Do a `python fplcoin.py`. This will create the database and a random wallet. Now type `i`. You should see a wallet with no coins. Now type `q` to quit, and wait for it to quit.

Now, with fplcoin shut down, open fplcoin.db (the database) with an sqlite database editor. You can use a GUI tool for this or just `sqlite3`. On OS X I like to use a tool called DB Browser.

Browse to the table called wallets, and change the private key, public key and address to the values you generated with generateGenesis.py. Save the database, close the tool.

Now if everything went well, you can `python fplcoin.py`, and if you type `i` you should see that your wallet now contains 100 coins.

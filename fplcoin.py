#!/usr/bin/python

import fplcoin

import fplcoin.wallets
import fplcoin.transactions


commands = {'q':'quit', 'h':'help', 'b':'broadcast', 't':'transaction', 'i':'information'}
running = True

if __name__ == "__main__":

	fplcoin.network.startNetworking()
	fplcoin.miner.startMining()
	
	while running:

		try:
		
			ui = raw_input("> ")

			if ui == 'q':
				break

			if ui == 'h':
				for c in commands:
					print "%s: %s" % (c, commands[c])

			if ui == 't':
				to = raw_input("To: ")
				amount = raw_input("Amount: ")
				fplcoin.transactions.createTransaction(to, amount)

			if ui == 'i':
				fplcoin.wallets.printBasicInfo()

			if ui == 'b':
				fplcoin.network.broadcastSync()

		except KeyboardInterrupt:
			print "Exiting ..."
			running = False
			break
				
		except Exception as e:
			print "Exception in main: " + e.message
			break

	fplcoin.network.stopServer = True
	fplcoin.miner.stopMiner = True
	fplcoin.threader.waitForThreads()

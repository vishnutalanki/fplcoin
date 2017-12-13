import databasing, mining, networks, eccs, encodings, networks, threads
from hashlib import sha256

db 				= databasing.crackDB()
miner			= mining.fplcoinMiner()
network 		= networks.fplcoinNetwork()

ecc 			= eccs.ellipticCurve()
hasher 			= sha256
encoder 		= encodings.b58encoder()
threader 		= threads.fplcoinThreader()


from os.path import isfile
if not isfile(db.dbFile):
	db.createDB()
#!/usr/bin/python

import fplcoin

import fplcoin.wallets
import fplcoin.transactions

#coolAddressNames = ['fplcoin','fplcoin','crackco1n','crackco1N']

#while 1:
privateKey, publicKey = fplcoin.wallets.fplcoin.ecc.make_keypair()
compressedPublicKey  = fplcoin.wallets.compressPublicKey(publicKey)
newAddress = fplcoin.wallets.publicKeyToAddress(compressedPublicKey)

#print newAddress[:9]
#if newAddress[:9] in coolAddressNames:
print "Private key:\n\t%s" % privateKey
#print publicKey
print "Compressed public key:\n\t%s" % compressedPublicKey
print "Address:\n\t%s" % newAddress

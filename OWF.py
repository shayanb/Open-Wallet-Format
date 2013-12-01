#!/usr/bin/env python

import os, sys
from optparse import OptionParser
import simplejson


def keyheader(file):
    newfile= open(file, "w")
    newfile.write("# KEEP YOUR PRIVATE KEYS SAFE !\n "
                  "# Anyone who can read this file can spend your bitcoin.\n"
                  "# Format:"
                  "#   <Base58 encoded private key>[<whitespace>[<key createdAt>]]\n"
                  "#   The Base58 encoded private keys are the same format as\n"
                  "#   produced by the Satoshi client/ sipa dumpprivkey utility.\n"
                  "#   Key createdAt is in UTC format as specified by ISO 8601\n"
                  "#   e.g: 2011-12-31T16:42:00Z . The century, 'T' and 'Z' are mandatory\n"
                  "# Converted by Open Wallet Format (Converter for now) - info@btctalk.com\n#\n")
    newfile.close()


if __name__ == '__main__':

    json_db = {}
    nwwallet = ''

    parser = OptionParser(usage="%prog [options]", version="%prog 1.0")

    parser.add_option("--wallet", dest="wallet", action="store",
                      help="wallet.dat or the exported wallet from Bitcoin-QT to be converted")

    parser.add_option("--newwallet", dest="nwwallet",
                      help="New wallet name (multibit .key files only) (in the same directory as the --wallet")

    (options, args) = parser.parse_args()


    if not options.wallet:
        parser.error("No wallet defined for the input, use -h to know how")
    qtwallet = os.path.abspath(options.wallet)

    if options.nwwallet:
        nwwallet = os.path.dirname(qtwallet)
        nwwallet = nwwallet + "/" +options.nwwallet
        if os.path.exists(nwwallet):
            print "WARNING: the name you specified for your new wallet already exists, All your keys are gone!"
            print "Just kidding, I renamed it to the original name + _OLD"
            print "But watch out from now on"
            os.rename(nwwallet, nwwallet+"_OLD")
        if not os.path.exists(nwwallet):
            keyheader(nwwallet)
    if not options.nwwallet:
        nwwallet = os.path.dirname(qtwallet)
        nwwallet = nwwallet + "/Multibit.key"
        if os.path.exists(nwwallet):
            print "WARNING: multibit.key already exists, All your keys are gone!"
            print "Just kidding, I renamed it to multibit.key_OLD"
            print "But watch out from now on"
            os.rename(nwwallet, nwwallet+"_OLD")
        keyheader(nwwallet)
    print("Dumping...")
    scriptpath = os.path.dirname(sys.argv[0])
    a=os.popen(scriptpath + "/pywallet.py --dumpwallet --wallet " + qtwallet, "r")
    for line in a:
        if line.startswith('{'):
            break
    ab = open("./temp", "w")
    ab.write("{\n")
    for line in a:
        ab.write(line)
    a.close()
    ab.close()
    ab = open("./temp", "r")
    json_db = simplejson.load(ab)
    a.close()
    print("OK")
    newwallet = open(nwwallet , "a")
    nkeys = len(json_db['keys'])
    i = 0
    for bkey in json_db['keys']:
        i+=1
        newwallet.write(bkey['sec'])
        newwallet.write(" 2009-04-21T12:42:46Z\n")
    newwallet.write("\n # End of private keys")
    newwallet.close()
    os.remove("./temp")
    print("Done - TAKE GOOD CARE OF THIS FILE AS IT IS NOT ENCRYPTED")






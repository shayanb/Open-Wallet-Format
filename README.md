Open-Wallet-Format
==================
Bitcoin Wallet Convertor


OWF.py reads the keys from Bitcoin-QT wallet (e.g wallet.dat) and exports them to MultiBit wallet format (e.g multibit.key) but also applicable for Blockchain.info imports

I used jackjack-jj fork of Pywallet.py (https://github.com/jackjack-jj/pywallet) to read wallet.dat and it is included in this repository.
so you need to install the pywallet dependencies prior to the use of this.


Why should I use this?
---------------------
To Convert your wallet.dat (or exported wallet from Bitcoin-QT) to:
* MultiBit Wallet
* Blockchain Importable format
* Backup your private keys in a format that would not be as complicated as wallet.dat and less possible to be corrupted

WARNING: the output is not encrypted so take good care of the file! 


Usage:
-------
Usage: OWF.py [options]

Options:

  --version             show program's version number and exit
  
  -h, --help            show this help message and exit
  
  --wallet=WALLET       wallet.dat or the exported wallet from Bitcoin-QT to
                        be converted
                        
  --newwallet=NWWALLET  New wallet name (multibit format) (in the
                        same directory as the --wallet

Example
-------
./OWF.py --wallet ./wallet.dat

./OWF.py --wallet ./wallet.dat ./newwallet.key



TODO
----
* Lesser dependencies to pywallet.py
* Add --passphrase to read encrypted wallet.dat
* Nicer code! for now it works fine but it could be implemented in less hacky-code style


Support
=======
Please support the work by either writing code or donating to 1owfJHTsWrrCpgaaYjC1vbJevuQzYRTYn
It would be greatly appreciated. 

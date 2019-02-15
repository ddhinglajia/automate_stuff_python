#! /usr/bin/python3 
# mapIt.py - launches a map in browser using an address from
# command line or clipboard

import sys, webbrowser, pyperclip

if len(sys.argv) > 1:
    #get address from commmand line.
    address = ' '.join(sys.argv[1:])
else:
    #get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

# chmod +x 041_mapIt.py
# ./041_mapIt.py 870 Valencia St, San Francisco, CA 94110 
# or to use from clipboard
# ./041_mapIt.py
#! /usr/bin/env python3
# pw.py - an insecure password locker program

import sys


Passwords = { 'email': 'dds4f6sd4',
             'blog' : 'dd4s5d',
             'luggage': '5464'}

#if len(sys.argv) < 2:
    #print('usage: python pw.py [account] - copy account password')
    #sys.exit()

#account = sys.argv[1] # first command line arg is the account name

account = sys.argv[1] # first command line arg is the account name
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

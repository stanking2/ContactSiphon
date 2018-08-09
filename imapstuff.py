#! python3


# This is my first attempt at an app to pull contact info
# out of an email account, checking each email for addresses and names.
# With credit to:
# - Piers Lauder (imaplib)
# - Menno Finlay-Smits (imapclient)
# - Alain Spineux (pyzmail)
# - Al Sweigart (chps. 14 & 16 of 'Automate the Boring Stuff With Python')

import csv
import getpass
import imaplib
import socket
import sys
import timeit
import winsound
from typing import List

import imapclient
import pyzmail
from imapclient.exceptions import LoginError

from tilities import get_contacts

imaplib._MAXLINE = 10000000
start = timeit.default_timer()
# Establish a connection to an email server and account
mailHost = 'imap.mail.att.net'
try:
    imapObj = imapclient.IMAPClient(mailHost, ssl=True)
except socket.gaierror as err:
    print('Unable to resolve host name. Exiting.')
    sys.exit()
userName = input('Email Address:')
passWord = getpass.getpass(prompt='Password: ', stream=None)
print('Attempting to connect...')
try:
    imapObj.login(userName, passWord)
    print('Login successful!')
except LoginError as err:
    print('Login failed. Exiting.')
    print(err)
    sys.exit()

# Iterate through the folders and  pull the addresses
folders = imapObj.list_folders()
folders.sort()
addrlist: List = []
fldrs = 0
msgs = 0
while fldrs < len(folders):
    imapObj.select_folder(folders[fldrs][2], True)
    UIDs = imapObj.search(['ALL'])
    if len(UIDs) == 1:
        msgtxt = " message from '"
    else:
        msgtxt = " messages from '"
    print('Now processing ' + str(len(UIDs)) + msgtxt + folders[fldrs][2] + "'...")  # Add count of msgs
    rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
    for i in UIDs:
        imapObj.fetch(i, 'BODY[]')
        message = pyzmail.PyzMessage.factory(rawMessages[i][b'BODY[]'])
        addrlist = get_contacts(message, 'from', userName, addrlist)
        addrlist = get_contacts(message, 'to', userName, addrlist)
        addrlist = get_contacts(message, 'cc', userName, addrlist)
        addrlist = get_contacts(message, 'bcc', userName, addrlist)
        msgs += 1
    print("     ...'" + folders[fldrs][2] + "' completed.")
    fldrs += 1
outputFile = open('parsed-' + userName + '.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
headrow = ('Name', 'Email')
outputWriter.writerow(headrow)
addrlist.sort()
uniqueaddr = 0
stra = ''
straold = ''
strb = ''
strbold = ''
for j in range(len(addrlist)):
    if len(str(addrlist[j][0]).strip() + str(addrlist[j][1]).strip()) > 0:
        stra = str(addrlist[j][0]).strip()
        strb = str(addrlist[j][1]).strip()
        if stra == strb:
            stra = ''
        strb = strb.lower()
        if (stra + strb) != (straold + strbold):
            try:
                bodyrow = (stra, strb)
                uniqueaddr += 1
                outputWriter.writerow(bodyrow)
            except UnicodeEncodeError as err:
                ...
    straold = stra
    strbold = strb
outputFile.close()
print('Done! ' + str(msgs) + ' emails pulled; ' + str(uniqueaddr) + ' addresses siphoned out.')
imapObj.logout()
stop = timeit.default_timer()
print(stop - start)
winsound.PlaySound("tada.wav", winsound.SND_FILENAME)

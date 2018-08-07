#! python3


# This is my first attempt at an app to pull contact info
# out of an email account, checking each email for addresses and names.
# With credit to:
# - Piers Lauder (imaplib)<piers@communitysolutions.com.au>
# - Menno Finlay-Smits (imapclient) <inbox@menno.io>
# - Alain Spineux (pyzmail)
# - Al Sweigart (chps. 14 & 16 of 'Automate the Boring Stuff With Python')

import csv
import sys
import socket
import getpass
import imaplib
from typing import List, Any, Union
import winsound
import imapclient
from imapclient.exceptions import LoginError
import pyzmail
from tilities import parse_address
import timeit

imaplib._MAXLINE = 10000000
start = timeit.default_timer()
print(str(start))
# Establish a connection to an email server and account
mailHost = 'imap.mail.att.net'
# TODO to be replaced later with GUI input
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
addrlist: List[Union[List[tuple], Any]] = []
fldrs = 0
msgs = 0
adrs = 0
while fldrs < len(folders):
    imapObj.select_folder(folders[fldrs][2], readonly=True)
    UIDs = imapObj.search(['ALL'])
    if len(UIDs) == 1:
        msgtxt = " message from '"
    else:
        msgtxt = " messages from '"
    print('Now processing ' + str(len(UIDs)) + msgtxt + folders[fldrs][2] + "'...")  # Add count of msgs
    if folders[fldrs][2] in ['Bulk Mail', 'Inbox', 'Junk E-mail', 'Sent Messages', 'Trash']:
        winsound.PlaySound("Alarm03.wav", winsound.SND_FILENAME)
    # Iterate through the emails and pull out the addresses
    rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
    for i in UIDs:
        imapObj.fetch(i, 'BODY[]')
        message = pyzmail.PyzMessage.factory(rawMessages[i][b'BODY[]'])
        cFr = message.get_address('from')
        parsed = parse_address(cFr[0], cFr[1], userName)
        if parsed is not False:
            addrlist.append(parsed)
            adrs += 1
        cTo = message.get_addresses('to')
        if len(cTo) > 0:
            for j in range(len(cTo)):
                parsed = parse_address(cTo[j][0], cTo[j][1], userName)
                if parsed is not False:
                    addrlist.append(parsed)
                    adrs += 1
        cCc = message.get_addresses('cc')
        if len(cCc) > 0:
            for j in range(len(cCc)):
                parsed = parse_address(cCc[j][0], cCc[j][1], userName)
                if parsed is not False:
                    addrlist.append(parsed)
                    adrs += 1
        cBc = message.get_addresses('bcc')
        if len(cBc) > 0:
            for j in range(len(cBc)):
                parsed = parse_address(cBc[j][0], cBc[j][1], userName)
                if parsed is not False:
                    addrlist.append(parsed)
                    adrs += 1
        msgs += 1
    print("     ...'" + folders[fldrs][2] + "' completed.")
    fldrs += 1
winsound.Beep(440, 2000)
winsound.MessageBeep(winsound.MB_OK)
outputFile = open('parsed-' + userName + '.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
headrow = ('Name', 'Email')
outputWriter.writerow(headrow)
addrlist.sort()
# TODO remove duplicates, and validate addresses
stra = ''
strb = ''
for j in range(len(addrlist)):
    if len(str(addrlist[j][0]).strip() + str(addrlist[j][1]).strip()) > 0:
        stra = str(addrlist[j][0]).strip()
        strb = str(addrlist[j][1]).strip()
        if stra == strb:
            stra = ''
        strb = strb.lower()
        try:
            bodyrow = (stra, strb)
            outputWriter.writerow(bodyrow)
        except UnicodeEncodeError as err:
            ...
outputFile.close()
print('Done! ' + str(msgs) + ' emails pulled; ' + str(adrs) + ' addresses siphoned out.')
imapObj.logout()
stop = timeit.default_timer()
print(stop - start)
winsound.PlaySound("*", winsound.SND_ALIAS)
winsound.PlaySound("*", winsound.SND_ALIAS)
winsound.PlaySound("tada.wav", winsound.SND_FILENAME)

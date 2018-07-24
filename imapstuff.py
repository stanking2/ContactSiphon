#! python3
# This is my first attempt at an app to pull contact info
# out of an email account, checking each email for addresses and names.
import csv
import imapclient
import pyzmail
# import pprint

# replace specific host, email address and password with input methods
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('stanking2@gmail.com', '33sEsame88')

imapObj.select_folder('Test', readonly=True)
UIDs = imapObj.search(['ALL'])

outputFile = open('output.csv', 'w', newline='') #add code to select filename and location
outputWriter = csv.writer(outputFile)
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
for UID in UIDs:
# new section using pyzmail
# I want to iterate through all messages... 
    message = pyzmail.PyzMessage.factory(rawMessages[UID]['BODY[]'])
    cFr = message.get_addresses('from')
    cTo = message.get_addresses('to')
    cCc = message.get_addresses('cc')
    cBc = message.get_addresses('bcc')
    outputWriter.writerow([cFr, cTo, cCc, cBc])

outputFile.close()
imapObj.logout()

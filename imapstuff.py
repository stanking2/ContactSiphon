# This is my first attempt at an app to pull contact info
# out of an email account, checking each email for addresses and names.
import csv
import imapclient
import pyzmail
import pprint

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('stanking2@gmail.com', '33sEsame88')
# can skip the next line if you already have the folder name
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['ALL'])
UIDs
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
# new section using pyzmail
# I want to iterate through all messages...
message = pyzmail.PyzMessage.factory(rawMessages[833]['BODY[]'])
# ... so would this work? NOPE!
# message = pyzmail.PyzMessage.factory(rawMessages[UIDs]['BODY[]'})
# then get the addresses! and put them in a csv file
cFr = message.get_addresses('from')
cTo = message.get_addresses('to')
cCc = message.get_addresses('cc')
cBc = message.get_addresses('bcc')
# just started creating the csv file...

imapObj.logout()

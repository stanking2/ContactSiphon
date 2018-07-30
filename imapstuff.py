#! python3
# This is my first attempt at an app to pull contact info
# out of an email account, checking each email for addresses and names.
# With credit to Menno Smits (imapclient), Alain Spineux (pyzmail), and
# Al Sweigart (chps. 14 & 16 of 'Automate the Boring Stuff With Python')
import csv, sys
import imaplib
import imapclient, pyzmail
imaplib._MAXLINE = 10000000

## Step 1: Establish a connection to an email server and account
mailHost = 'imap.mail.yahoo.com' #to be replaced later with user input
imapObj = imapclient.IMAPClient(mailHost, ssl=True)
userName = input('User Name:')
passWord = input('Password:')
if(imapObj.login(userName, passWord))!=b'LOGIN completed':
    print('Connection failed. Exiting program.')
    sys.exit()

## Step 8: Wrap Steps 2-4 to iterate through all folders in the IMAP account

## Step 2: Pull the emails in a folder
imapObj.select_folder('Test', readonly=True)
UIDs = imapObj.search(['ALL'])

## Step 3: Create the CSV file to hold the data
outputFile = open('output.csv', 'w', newline='') #add code to select filename and location
outputWriter = csv.writer(outputFile)

## Step 4: Iterate through the emails and pull out the addresses
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
for i in UIDs:
    imapObj.fetch(i, 'BODY[]')
    message = pyzmail.PyzMessage.factory(rawMessages[i]['BODY[]'])
    cFr = message.get_addresses('from')
    cTo = message.get_addresses('to')
    cCc = message.get_addresses('cc')
    cBc = message.get_addresses('bcc')
    outputWriter.writerow([cFr, cTo, cCc, cBc])

## Step 5: Validate the addresses

## Step 6: Eliminate the duplicate entries

## Ste[ 7: Close the CSV and the connection]
outputFile.close()
imapObj.logout()

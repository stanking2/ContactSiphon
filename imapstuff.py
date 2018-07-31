#! python3
# This is my first attempt at an app to pull contact info
# out of an email account, checking each email for addresses and names.
# With credit to Menno Smits (imapclient), Alain Spineux (pyzmail), and
# Al Sweigart (chps. 14 & 16 of 'Automate the Boring Stuff With Python')
import csv, sys
import imaplib, pprint
import imapclient, pyzmail
imaplib._MAXLINE = 10000000

## Step 1: Establish a connection to an email server and account
mailHost = 'imap.mail.yahoo.com' #to be replaced later with user input
imapObj = imapclient.IMAPClient(mailHost, ssl=True)
userName = 'stan@king-of-tx.com' #remove
passWord = '33Sesame44' #remove
##userName = input('User Name:')
##passWord = input('Password:')
if(imapObj.login(userName, passWord))!=b'LOGIN completed':
    print('Connection failed. Exiting program.') #add retry code
    sys.exit()

## Step 2: Create the CSV file to hold the data
outputFile = open('output.csv', 'w', newline='') #add code to select filename and location
outputWriter = csv.writer(outputFile)
adrs = 0

## Step 3: Wrap Steps 4-5 to iterate through all folders in the IMAP account
folders = imapObj.list_folders()
k = 0
while k < len(folders):
    # print(folders[k][2])
    ## Step 4: Pull the emails in a folder
    imapObj.select_folder(folders[k][2], readonly=True)
    UIDs = imapObj.search(['ALL'])
    print('Now processing ' + folders[k][2] + '...')

    ## Step 5: Iterate through the emails and pull out the addresses
    rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
    for i in UIDs:
        imapObj.fetch(i, 'BODY[]')
        message = pyzmail.PyzMessage.factory(rawMessages[i][b'BODY[]'])
        cFr = message.get_addresses('from')
        cTo = message.get_addresses('to')
        cCc = message.get_addresses('cc')
        cBc = message.get_addresses('bcc')
        # trap UnicodeEncodeError
        outputWriter.writerow([cFr, cTo, cCc, cBc])
        adrs = adrs + 1
    print(folders[k][2] + ' completed.')
    k = k + 1

## Step 5: Validate the addresses

## Step 6: Eliminate the duplicate entries
print('Done! ' + str(adrs) + ' emails pulled for addresses.')

## Ste[ 7: Close the CSV and the connection]
outputFile.close()
imapObj.logout()

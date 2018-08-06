#! python3
# This is my first attempt at an app to pull contact info
# out of an email account, checking each email for addresses and names.
# With credit to Menno Smits (imapclient), Alain Spineux (pyzmail), and
# Al Sweigart (chps. 14 & 16 of 'Automate the Boring Stuff With Python')
import csv
import imaplib
import imapclient
from imapclient.util import to_unicode
import pyzmail
imaplib._MAXLINE = 10000000

# Establish a connection to an email server and account
mailHost = 'imap.mail.att.net'
# TODO to be replaced later with GUI input
imapObj = imapclient.IMAPClient(mailHost, ssl=True)
userName = input('User Name:')
passWord = input('Password:')
# TODO use getpass to conceal password
# TODO convert to try/catch connection and authentication errors
print(imapObj.login(userName, passWord))
# if(imapObj.login(userName, passWord) != b'LOGIN completed'):
#     print('Connection failed. Exiting program.')
#     sys.exit()  # b'[AUTHENTICATIONFAILED] LOGIN Invalid credentials'
#     # refer to imaplib line 592 to trap no/bad
# else:
#     print('Successful connection!')

# Create the CSV file to hold the siphoned contacts;may push this until after the data pull
outputFile = open('output-' + userName + '.csv', 'w', newline='')
# TODO add code to select filename and location
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['FROM', 'TO', 'CC', 'BCC'])

# Iterate through the folders and  pull the addresses
folders = imapObj.list_folders()
k = 0
emails = 0
adrs = 0
while k < len(folders):
    # print(folders[k][2])
    # Step 4: Pull the emails in a folder
    imapObj.select_folder(folders[k][2], readonly=True)
    UIDs = imapObj.search(['ALL'])  # Can I chg to ENVELOPE HERE AS WELL?
    print('Now processing ' + folders[k][2] + '...')  # Add count of msgs

    # Step 5: Iterate through the emails and pull out the addresses
    rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
    # TODO change 'BODY' references to 'ENVELOPE' or the individual address fields
    for i in UIDs:
        imapObj.fetch(i, 'BODY[]')
        message = pyzmail.PyzMessage.factory(rawMessages[i][b'BODY[]'])
        cFr = list(message.get_address('from'))
        cFr[0] = to_unicode(cFr[0])
        cTo = message.get_addresses('to')
        cCc = message.get_addresses('cc')
        cBc = message.get_addresses('bcc')
        # trap UnicodeEncodeError
        try:
            outputWriter.writerow([cFr, to_unicode(cTo), to_unicode(cCc), to_unicode(cBc)])
        except UnicodeEncodeError as err:
            outputWriter.writerow([[], to_unicode(cTo), to_unicode(cCc), to_unicode(cBc)])
        emails = emails + 1
        adrs = adrs + len(cFr) + len(cTo) + len(cCc) + len(cBc)
    print(folders[k][2] + ' completed.')
    k = k + 1

# Step 5: Validate the addresses

# Step 6: Eliminate the duplicate entries
print('Done! ' + str(emails) + ' emails pulled; ' + str(adrs) + ' addresses siphoned out.')

# Step 7: Close the CSV and the connection]
outputFile.close()
imapObj.logout()

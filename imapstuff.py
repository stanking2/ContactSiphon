#imap notes from imapclient

>>> import imapclient
>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
>>>> imapObj.login('stanking2@gmail.com', '33sEsame88')
b'stanking2@gmail.com authenticated (Success)'
# can skip these next 2 lines if you already have the folder name
>>> import pprint
>>> pprint.pprint(imapObj.list_folders())
[((b'\\HasNoChildren',), b'/', 'AARP'),
 ((b'\\HasNoChildren',), b'/', 'Amazon'),
 ((b'\\HasNoChildren',), b'/', 'Amy'),
 ((b'\\HasNoChildren',), b'/', 'Banking'),
 ((b'\\HasNoChildren',), b'/', 'Dell'),
 ((b'\\HasNoChildren',), b'/', 'Divorce'),
 ((b'\\HasNoChildren',), b'/', 'EmailAccts'),
 ((b'\\HasNoChildren',), b'/', 'Family'),
 ((b'\\HasNoChildren',), b'/', 'Fitbit'),
 ((b'\\HasNoChildren',), b'/', 'Forwarded FAS'),
 ((b'\\HasNoChildren',), b'/', 'From Yahoo'),
 ((b'\\HasNoChildren',), b'/', 'INBOX'),
 ((b'\\HasChildren',), b'/', 'NRHBC'),
 ((b'\\HasNoChildren',), b'/', 'NRHBC/NRHBC Choir-Prayer'),
 ((b'\\HasNoChildren',), b'/', 'Notes'),
 ((b'\\HasNoChildren',), b'/', 'Online Orders'),
 ((b'\\HasNoChildren',), b'/', 'RedBubble'),
 ((b'\\HasChildren', b'\\Noselect'), b'/', '[Gmail]'),
 ((b'\\All', b'\\HasNoChildren'), b'/', '[Gmail]/All Mail'),
 ((b'\\Drafts', b'\\HasNoChildren'), b'/', '[Gmail]/Drafts'),
 ((b'\\HasNoChildren', b'\\Important'), b'/', '[Gmail]/Important'),
 ((b'\\HasNoChildren', b'\\Sent'), b'/', '[Gmail]/Sent Mail'),
 ((b'\\HasNoChildren', b'\\Junk'), b'/', '[Gmail]/Spam'),
 ((b'\\Flagged', b'\\HasNoChildren'), b'/', '[Gmail]/Starred'),
 ((b'\\HasNoChildren', b'\\Trash'), b'/', '[Gmail]/Trash')]
>>> imapObj.select_folder('INBOX', readonly=True)
{b'PERMANENTFLAGS': (), b'FLAGS': (b'\\Answered', b'\\Flagged', b'\\Draft', b'\\Deleted', b'\\Seen', b'$NotPhishing', b'$Phishing'), b'UIDVALIDITY': 594705252, b'EXISTS': 35, b'RECENT': 0, b'UIDNEXT': 835, b'HIGHESTMODSEQ': 379823, b'READ-ONLY': [b'']}
>>> UIDs = imapObj.search(['ALL'])
>>> UIDs
[194, 197, 517, 524, 595, 632, 654, 672, 701, 741, 751, 761, 763, 765, 779, 780, 796, 800, 801, 810, 816, 818, 819, 821, 822, 823, 824, 825, 826, 827, 828, 829, 831, 832, 833]
>>> rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
# new section using pyzmail
>>> import pyzmail
# I want to iterate through all messages...
>>> message = pyzmail.PyzMessage.factory(rawMessages[833]['BODY[]'])
# ... so would this work?
>>> message = pyzmail.PyzMessage.factory(rawMessages[UIDs]['BODY[]'})
# then get the addresses! and put them in a csv file
>>> message.get_addresses('from')
[('From Name'. 'from.name@fake.com')]
>>> message.get_addresses('to')
[('To Name'. 'to.name@fake.com'), ('Another Name'. 'another.name@fake.com')]
>>> message.get_addresses('cc')
[] # usually blank
>>> message.get_addresses('bcc')
[] # usually blank



>>> imapObj.logout()
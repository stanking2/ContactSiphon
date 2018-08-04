#! python3


import re


# takes a string? splits and trims, assigns to a list of tuples
def parseaddress(unparsed):
    if unparsed == '[]':
        return ''
    else:
        unparsedRE = re.compile
        addrlist = unparsed.split("), (")
        """replace ,[] with NOTHING
        replace " with NOTHING
        replace [ with NOTHING
        replace ] with NOTHING
        replace ( with NOTHING
        replace ) with NOTHING
        replace ',' with '\n' REGEX
        replace '\n' with \n REGEX
        (have to figure out how to escape , in name)
        replace ', ' with , REGEX
        remove initial '
        remove last '
        TRIM all fields
        SORT alphanumeric, case insensitive, deleting duplicate lines
        
        remove lines beginning with LEAVE or UNSUB
        remove addresses with forms of NO_REPLY, DO_NOT_REPLY, MAILER-DAEMON
        make EMAIL lowercase
        SORT BY EMAIL, NAME"""
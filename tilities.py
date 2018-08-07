#! python3


def parse_address(rawname, rawaddress, username):
    if len(rawname) + len(rawaddress) == 0:
        return False
    else:
        if rawname == rawaddress:
            rawname = ''
        rawaddress = rawaddress.lower()
        if rawaddress == username:
            return False
        return rawname, rawaddress

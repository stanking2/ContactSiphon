#! python3


def get_contacts(message, header_field, username, addrlist):
    hf = message.get_address(header_field)
    if len(hf) > 0:
        for k in range(len(hf)):
            parsed = parse_address(hf[0], hf[1], username)
            if parsed is not False:
                addrlist.append(parsed)
    return addrlist


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

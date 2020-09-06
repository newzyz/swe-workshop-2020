import re


def validate_name(name):
    name = str(name)
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special = ["!", "@", "#", "$"]
    if(name == ""):
        return False

    if " " in name:
        return False

    if(name.isalpha()):
        return True

    for s in name:
        if (s in digits) or (s in special):
            return False

    return True


def validate_id(id):
    id = str(id)
    if(id == ""):
        return False

    if(id.isdigit()):
        if(len(id) == 13):
            sum = 0
            for i in range(len(id) - 1):
                sum += int(id[i]) * (len(id) - i)
            if(11 - (sum % 11) == int(id[12])):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def validate_phone_number(phone_number):
    return True

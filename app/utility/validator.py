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
    return True


def validate_phone_number(phone_number):
    return True

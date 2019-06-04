import re


class Phone(object):
    """Phone class for North American Numbering Plan (NANP) phone numbers"""

    def __init__(self, phone_number):
        digits = re.sub("[^0-9]", "", phone_number)
        if digits[0] == '1':
            digits = digits[1:]

        if len(digits) != 10:
            raise ValueError("Error: lenght of phone number is not 10")
        if digits[0] < '2' or digits[3] < '2':
            raise ValueError("Error: area/exchange code starting with '0/1'")

        self.number = digits
        self.area_code = digits[0:3]
        self.exchange = digits[3:6]
        self.subscriber = digits[6:]

    def __str__(self):
        return f"({self.area_code}) {self.exchange}-{self.subscriber}" 

    def pretty(self):
        return str(self)

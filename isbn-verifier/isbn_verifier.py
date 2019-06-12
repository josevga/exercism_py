import re

def is_valid(isbn):
    digits = re.sub("[^0-9,X]", "", isbn)
    if re.match("^[0-9]{9}[0-9,X]$", digits):
        nums = list(digits)
        if nums[-1] == "X":
            nums[-1] = 10
        return sum((10 - i) * int(x) for (i, x) in enumerate(nums)) % 11 == 0

    return False

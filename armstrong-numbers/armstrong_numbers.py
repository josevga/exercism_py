def is_armstrong_number(number):
    digits = str(number)
    return number == sum((int(x) ** len(digits) for x in digits))

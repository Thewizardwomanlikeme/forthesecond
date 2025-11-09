import sys


def main():
    credit = retrieve_credit_number()
    first_total = calculate_luhn_product_total(credit)
    next_total = calculate_luhn_others_total(credit)
    num = (first_total + next_total) % 10
    initial_check(num, credit)
    length = len(str(credit))
    check_card_type(num, credit, length)


def retrieve_credit_number():
    while True:
        credit = input("Number: ")
        if len(credit) == 13 or len(credit) == 15 or len(credit) == 16:
            return int(credit)
        else:
            print("INVALID")
            sys.exit()


def calculate_luhn_product_total(credit):
    total = 0
    while credit > 0:
        credit = credit // 10
        num = credit % 10
        num *= 2
        if num > 9:
            sum = 0
            while num > 0:
                numm = num % 10
                sum += numm
                num = num // 10
            total += sum
        total += num
        credit = credit // 10
    return total


def calculate_luhn_others_total(credit):
    total = 0
    while credit > 0:
        num = credit % 10
        total += num
        credit = credit // 100
    return total


def initial_check(num, credit):
    total = 0
    while True:
        total += credit % 10
        credit = credit // 10
        if credit == 0:
            break
    if total == 0 or num != 0:
        print("INVALID")


def check_for_AMEX(credit, length):
    if length == 15:
        nnum = credit // 10 ** 13
        if nnum == 34 or nnum == 37:
            print("AMEX")
        else:
            print("INVALID")


def check_for_VISA_or_MASTERCARD(length, credit):
    nuum = credit // 10 ** 14
    numm = credit // 10 ** 15
    mastercard = [51, 52, 53, 54, 55]
    if length == 13:
        print("VISA")
    elif length == 16:
        if numm == 4:
            print("VISA")
            sys.exit()
        elif nuum in mastercard:
            print("MASTERCARD")
            sys.exit()
        else:
            print("INVALID")


def check_card_type(num, credit, length):
    if num == 0:
        check_for_AMEX(credit, length)
        check_for_VISA_or_MASTERCARD(length, credit)


main()

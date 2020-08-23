UNITS = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

TENS = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}


def _less_than_hundred_to_words(number):
    if number < 20:
        return UNITS[number]
    elif number < 100:
        number_tens = number // 10
        number_units = number % 10
        return f'{TENS[number_tens]} {UNITS[number_units]}'

    # if none of the above clauses are met, the number is out of bounds, we throw an assertion error
    assert 0 < number < 100, f'we should have 0 < number < 100, but number is {number}'


def _less_than_thousand_to_words(number):
    if number < 100:
        return _less_than_hundred_to_words(number)
    elif number < 1000:
        number_hundreds = number // 100
        remainder = number % 100
        remainder_in_words = _less_than_hundred_to_words(remainder)
        return f'{UNITS[number_hundreds]} hundred {remainder_in_words}'


def int_to_words(number):
    # if number == 0:
    #     return 'zero'

    if number < 1000:
        return _less_than_thousand_to_words(number).strip()

    elif number < 1_000_000:
        number_thousands = number // 1000
        number_thousands_in_words = int_to_words(number_thousands)

        remainder = number % 1000
        remainder_in_words = int_to_words(remainder)
        return f'{number_thousands_in_words} thousand {remainder_in_words}'.strip()

    elif number < 1_000_000_000:
        number_millions = number // 1_000_000
        number_millions_in_words = int_to_words(number_millions)

        remainder = number % 1_000_000
        remainder_in_words = int_to_words(remainder)
        return f'{number_millions_in_words} million {remainder_in_words}'






def convert_currency(amount):

    return 'three dollars'


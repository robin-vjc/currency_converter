from converter.constants import MAGNITUDES
from converter.constants import TENS
from converter.constants import UNITS


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
        if remainder_in_words:
            return f'{UNITS[number_hundreds]} hundred and {remainder_in_words}'
        else:
            return f'{UNITS[number_hundreds]} hundred'


def int_to_words(number):
    """
    Converts integer into words;
    """
    if number < 1000:
        return _less_than_thousand_to_words(number).strip()

    # find the magnitude of the number;
    # 1_000 -> magnitude = 1
    # 1_000_000 -> magnitude = 2
    # etc.
    number_magnitude = 0
    for allowed_magnitude in MAGNITUDES:
        if number // 1000 ** allowed_magnitude:
            number_magnitude += 1

    # if we have number = 1_000_000_000, magnitude is in [3, 2, 1]
    for magnitude in reversed(range(1, number_magnitude+1)):
        number_xillions = number // 1000**magnitude
        number_xillions_in_words = int_to_words(number_xillions)

        remainder = number % 1000**magnitude
        remainder_in_words = int_to_words(remainder)

        if remainder_in_words:
            return f'{number_xillions_in_words} {MAGNITUDES[magnitude]}, {remainder_in_words}'.strip()
        else:
            return f'{number_xillions_in_words} {MAGNITUDES[magnitude]}'.strip()


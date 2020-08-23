from converter.converter import convert_currency
from converter.converter import int_to_words


def test_converter():
    # assert convert_currency(1357256.32) == 'one million, three hundred and fifty seven thousand, ' \
    #                                        'two hundred and fifty six DOLLARS AND thirty two CENTS'

    test_int_numbers = {
        # 0: 'zero',
        10: 'ten',
        14: 'fourteen',
        34: 'thirty four',
        99: 'ninety nine',
        100: 'one hundred',
        101: 'one hundred one',
        453: 'four hundred fifty three',
        # 1000: 'one thousand',
        1999: 'one thousand nine hundred ninety nine',
        10000: 'ten thousand',
        989999: 'nine hundred eighty nine thousand nine hundred ninety nine',
    }

    for int_number in test_int_numbers:
        int_number_in_words = int_to_words(int_number)
        print(int_number, ': ', int_number_in_words)
        assert int_number_in_words == test_int_numbers[int_number]

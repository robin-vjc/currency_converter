from converter.converter import _int_to_words, currency_amount_to_words


def test_int_to_words():
    """ Test of function _int_to_words() """

    test_int_numbers = {
        # assert that we correctly map -0 -> 0 and return 'zero' instead of 'minus zero'
        -0: 'zero',
        10: 'ten',
        14: 'fourteen',
        34: 'thirty four',
        99: 'ninety nine',
        100: 'one hundred',
        101: 'one hundred and one',
        -133: 'minus one hundred and thirty three',
        453: 'four hundred and fifty three',
        1000: 'one thousand',
        1999: 'one thousand, nine hundred and ninety nine',
        10_000: 'ten thousand',
        989_999: 'nine hundred and eighty nine thousand, nine hundred and ninety nine',
        1_989_999: 'one million, nine hundred and eighty nine thousand, nine hundred and ninety nine',
        1_357_256: 'one million, three hundred and fifty seven thousand, two hundred and fifty six',
        3_000_000_000: 'three billion',
        7_221_300_000: 'seven billion, two hundred and twenty one million, three hundred thousand',
        -7_221_300_000: 'minus seven billion, two hundred and twenty one million, three hundred thousand',
    }

    # verify that we map the integer amounts to the expected strings
    for int_number in test_int_numbers:
        int_number_in_words = _int_to_words(int_number)
        print(int_number, ': ', int_number_in_words)
        assert int_number_in_words == test_int_numbers[int_number]


def test_currency_amount_to_words():
    """ Test of converter function currency_amount_to_words() """

    test_currency_amounts = {
        345.78: 'three hundred and forty five DOLLARS AND seventy eight CENTS',
        -345.00: 'minus three hundred and forty five DOLLARS AND zero CENTS',
        0: 'zero DOLLARS AND zero CENTS',
        1_100_452.30: 'one million, one hundred thousand, four hundred and fifty two DOLLARS AND thirty CENTS'
    }

    # verify that we map the currency amounts to the expected strings
    for currency_amount in test_currency_amounts:
        amount_in_words = currency_amount_to_words(currency_amount)
        print(currency_amount, ': ', amount_in_words)
        assert amount_in_words == test_currency_amounts[currency_amount]

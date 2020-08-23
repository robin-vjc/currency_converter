from converter.converter import int_to_words


def test_converter():
    test_int_numbers = {
        # 0: 'zero',
        10: 'ten',
        14: 'fourteen',
        34: 'thirty four',
        99: 'ninety nine',
        100: 'one hundred',
        101: 'one hundred and one',
        453: 'four hundred and fifty three',
        1000: 'one thousand',
        1999: 'one thousand, nine hundred and ninety nine',
        10_000: 'ten thousand',
        989_999: 'nine hundred and eighty nine thousand, nine hundred and ninety nine',
        1_989_999: 'one million, nine hundred and eighty nine thousand, nine hundred and ninety nine',
        1_357_256: 'one million, three hundred and fifty seven thousand, two hundred and fifty six',
        3_000_000_000: 'three billion',
        7_221_300_000: 'seven billion, two hundred and twenty one million, three hundred thousand'
    }

    for int_number in test_int_numbers:
        int_number_in_words = int_to_words(int_number)
        print(int_number, ': ', int_number_in_words)
        assert int_number_in_words == test_int_numbers[int_number]

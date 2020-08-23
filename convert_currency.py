import sys
from converter.converter import currency_amount_to_words

for arg in sys.argv[1:]:
    currency_amount = float(arg)
    print(currency_amount_to_words(currency_amount))

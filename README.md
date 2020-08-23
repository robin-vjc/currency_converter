# Installation

Simply clone the repo
```
git clone git@github.com:robin-vjc/currency_converter.git
```

Running tests
```
cd currency_converter
pip install -r requirements.txt
pytest
```

# Usage

The code in the repo can be used through a simple a CLI utility:
```
$ python convert_currency.py 345.65 698.3498 -39282398.3232
```
prints to stdout: 
```
three hundred and forty five DOLLARS AND sixty five CENTS
six hundred and ninety eight DOLLARS AND thirty four CENTS
minus thirty nine million, two hundred and eighty two thousand, three hundred and ninety eight DOLLARS AND minus thirty two CENTS
```

# TODOs

* create setup.py to make package pip-installable ("pip install -e .")
* handle other currencies / languages
* handle quantities above billions (simple: just update MAGNITUDES in constants.py)
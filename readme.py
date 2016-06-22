"""
>>> def test(arg):
...    print('Hello World')
...

>>> from watsite.sym import main as site_main
>>> site_main(main, [ 'something' '--test' ])
Hello World

"""

import doctest as dt

from  watsite.decorators import docparser
@docparser
def main():
   pass

if __name__ == '__main__':
    dt.testmod(optionflags=dt.NORMALIZE_WHITESPACE)

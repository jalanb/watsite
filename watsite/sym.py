

import sys


def main(main_method, argv):
    sys.argv = argv
    main_method()


def exit(main, argv):
    sys.argv = argv
    sys.exit(main)

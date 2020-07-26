# -*- coding: utf-8 -*-


"""fintualcli.fintualcli: provides entry point main()."""


__version__ = "0.1.0"


import sys
from fintualcli.stuff import Stuff


def main():
    print("Executing fintual-cli version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    print("Stuff and Boo():\n%s\n%s" % (Stuff, Boo()))


class Boo(Stuff):
    pass

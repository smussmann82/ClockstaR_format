#!/usr/bin/env python

from comline import ComLine
from phylip import Phylip

import sys

def main():
	input = ComLine(sys.argv[1:])
	alignment = Phylip(input.args.phylip, input.args.genes) # make new phylip object
	alignment.parseFile() # read and parse the phylip file

main()

raise SystemExit

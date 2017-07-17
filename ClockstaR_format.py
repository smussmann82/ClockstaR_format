#!/usr/bin/env python

from __future__ import print_function

from comline import ComLine
from phylip import Phylip
from partitions import Partitions

import sys

def main():
	input = ComLine(sys.argv[1:])
	alignment = Phylip(input.args.phylip, input.args.genes) # make new phylip object
	alignment.parseFile() # read and parse the phylip file
	models = Partitions(input.args.partitions) #new partitions object
	models.parseFile() # read the partitions nexus file

	for part, model in models.modelsdict.iteritems():
		temp = part.split("_")
		fn = temp[0] + "_" + model + ".fasta"
		print(fn)
		fh = open(fn, 'w')
		for sample, seq in sorted(alignment.seqdict.iteritems()):
			fh.write(">")
			fh.write(sample)
			fh.write("\n")
			for coord in models.coordsdict[part]:
				#print(coord)
				coords = coord.split("-")
				fh.write(seq[int(coords[0])-1:int(coords[1])])
			fh.write("\n")
		#print(part)

		fh.close()

main()

raise SystemExit

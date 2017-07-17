from __future__ import print_function

import argparse
import os.path

class ComLine():
	'Class for implementing command line options'
	

	def __init__(self, args):
		parser = argparse.ArgumentParser()
		parser.add_argument("-i", "--phylip",
							dest='phylip',
							required=True,
							help="Specify a phylip file for input."
		)
		parser.add_argument("-p", "--partitions",
							dest='partitions',
							required=True,
							help="Specify partition file output from IQtree"
		)
		parser.add_argument("-g", "--genes",
							dest='genes',
							required=True,
							help="Specify file with coordinates of genes in phylip file"
		)
		parser.add_argument("-o", "--out",
							dest='out',
							default="output.txt",
							help="Specify an output file name."
		)
		
		self.args = parser.parse_args()

		#check if files exist
		self.exists(self.args.phylip)
		self.exists(self.args.partitions)
		self.exists(self.args.genes)



	def exists(self, filename):
		if( os.path.isfile(filename) != True ):
			print(filename, "does not exist")
			print("Exiting program...")
			print("")
			raise SystemExit

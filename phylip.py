from __future__ import print_function

import sys

class Phylip():
	'Class for parsing phylip files'
	
	def __init__(self, fname, loci):
		self.fname = fname
		self.loci = loci
		self.header = str()
		self.seqdict = dict()
		self.locidict = dict()
	
	def parseFile(self):
		self.parsePhylip()
		self.parseLoci()

	def parsePhylip(self):
		lines = [line.rstrip('\n') for line in open(self.fname)]
		self.header = lines.pop(0) #remove and retail phylip header
		for line in lines:
			temp = line.split()
			k = temp[0]
			v = temp[1]
			self.seqdict[k] = v

		#print(self.seqdict)

	def parseLoci(self):
		lines = [line.rstrip("\n") for line in open(self.loci)]
		for line in lines:
			temp = line.split().pop(-1)
			templist = temp.split("=")
			name = templist.pop(0)
			coords = templist.pop(0)
			self.locidict[name] = coords
		#print(self.locidict)

	def getLocus(self):
		print("stuff")

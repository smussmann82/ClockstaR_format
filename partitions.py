from __future__ import print_function

import sys

from collections import defaultdict

class Partitions():
	'Class for parsing partition nexus files from IQtree'
	
	def __init__(self, fname):
		self.fname = fname
		self.coordsdict = defaultdict(list)
		self.modelsdict = dict()
	
	def parseFile(self):
		self.parsePartitions()

	def parsePartitions(self):
		lines = [line.rstrip('\n') for line in open(self.fname)]
		for line in lines:
			temp = line.strip()
			if temp.startswith("charset"):
				linelist = temp.split("=")
				name = linelist[0].split().pop(-1)
				coordslist = linelist[1].strip(",;").split()
				self.coordsdict[name]=coordslist
			if ":" in temp:
				#print(temp)
				linelist = temp.split(":")
				model = linelist.pop(0)
				name = linelist[0].strip(",;").strip()
				self.modelsdict[name]=model
		#print(self.coordsdict)
		#print(self.modelsdict)

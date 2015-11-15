# Jacob Martin
# CS 311

import json

class Grammar:

	def __init__(self, source):
		self.desc  = ""
		self.rules = []
		try:
			grammar   = json.load(open(source))
			self.desc = grammar["desc"]
			for variable, rule in grammar["rules"].iteritems():
				self.rules[variable].append(rule)
		except FileNotFoundError:
			pass

	def getDesc(self):
		return self.desc
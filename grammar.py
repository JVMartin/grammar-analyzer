# Jacob Martin
# CS 311

import json

class Grammar:

	def __init__(self, source):
		self.desc  = ""
		self.rules = dict()
		try:
			grammar   = json.load(open(source))
			self.desc = grammar["desc"]
			for variable, rule in grammar["rules"].items():
				if variable not in self.rules:
					self.rules[variable] = []
				self.rules[variable].append(rule)
		except FileNotFoundError:
			pass

	def get_desc(self):
		return self.desc

	def get_rules(self):
		return
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
			for variable, rules in grammar["rules"].items():
				self.rules[variable] = rules
		except FileNotFoundError:
			pass

	def get_desc(self):
		return self.desc

	def produces(self, variable):
		if variable not in self.rules:
			return False

		return self.rules[variable]

	def get_rule(self, variable, input_symbol):
		if len(input_symbol) != 1:
			return False

		productions = self.produces(variable)
		if not productions:
			return False

		for production in productions:
			if production[0] == input_symbol:
				return production

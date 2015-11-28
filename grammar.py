# Jacob Martin
# CS 311

# A class used as a data structure to represent a grammar.

# An instance of the Grammar class is initialized with the source path to
# a grammar JSON file.  The JSON file is parsed into the grammar object's
# members.

import json

class Grammar:

	def __init__(self, source):
		self.desc  = ""
		self.rules = dict()
		try:
			with open(source) as json_file:
				grammar = json.load(json_file)
			self.desc = grammar["desc"]
			for variable, rules in grammar["rules"].items():
				self.rules[variable] = rules
		except FileNotFoundError:
			pass

	def get_desc(self):
		return self.desc

	def produces(self, variable):
		"""
		Retrieve all the productions that the passed variable is
		capable of producing.

		:param variable: The variable in question.
		:return: A list of productions.
		"""
		if variable not in self.rules:
			return False

		return self.rules[variable]

	def get_rule(self, variable, input_symbol):
		"""
		Retrieve the single production (rule) that the passed variable
		can produce whose leftmost symbol is the passed input symbol.

		:param variable: The variable in question.
		:param input_symbol: The input symbol in question.
		:return: A single production.
		"""
		if len(input_symbol) != 1:
			return False

		productions = self.produces(variable)
		if not productions:
			return False

		for production in productions:
			if production[0] == input_symbol:
				return production

		return False

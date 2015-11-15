# Jacob Martin
# CS 311

import grammar

class GrammarChecker:

	# Load the DFA from the JSON file.
	def __init__(self, Grammar: grammar):
		self.grammar = grammar
# Jacob Martin
# CS 311

import grammar

class GrammarAnalyzer:

	def __init__(self, grammar):
		self.grammar = grammar
		self.stack   = []
		self.input   = []
		print("Grammar analyzer initialized.")
		print("Imported grammar: " + grammar.get_desc())

	def test_string(self, string):
		if not len(string):
			return False

		self.stack = ["$", "S"]
		self.input = list(string)

		print("Testing string: " + string)
		print("Starting stack: " + self.stack_to_string())

		self.parse_input()

	def parse_input(self):
		pass

	def stack_to_string(self):
		return ''.join(reversed(self.stack))

	def print_stack(self):
		print(self.stack_to_string())
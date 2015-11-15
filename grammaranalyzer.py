# Jacob Martin
# CS 311

import helpers

class GrammarAnalyzer:

	def __init__(self, grammar):
		self.grammar = grammar
		self.stack   = []
		self.input   = []
		print("Grammar analyzer initialized.")
		helpers.hr()
		print("Imported grammar: " + grammar.get_desc())

	def test_string(self, string):
		if not len(string):
			return False

		self.stack = ["$", "S"]
		self.input = list(string)
		self.input.reverse()

		print("Testing string: " + string)
		print("Starting stack: " + self.stack_to_string())

		return self.parse_input()

	def parse_input(self):
		helpers.hr()
		stack_symbol = self.stack.pop()

		print("Popped stack symbol: " + stack_symbol)

		# If the stack is empty and the input is too, accept.
		# Otherwise, reject.
		if stack_symbol == "$":
			return True if not self.input else False

		# If we have a variable...
		if stack_symbol.isupper():
			# Peek at the next input symbol.
			next_input = self.input[-1]
			print(next_input)

	def stack_to_string(self):
		return ''.join(reversed(self.stack))

	def print_stack(self):
		print(self.stack_to_string())

	def input_to_string(self):
		return ''.join(reversed(self.input))

	def print_input(self):
		print(self.input_to_string())

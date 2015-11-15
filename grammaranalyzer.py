# Jacob Martin
# CS 311

import helpers

class GrammarAnalyzer:

	def __init__(self, grammar):
		self.verbose = False
		self.grammar = grammar
		self.stack   = []
		self.input   = []

		self.verbalize("Grammar analyzer initialized.")
		self.verbalize("Imported grammar: " + grammar.get_desc())
		self.verbalize(self.hr())

	def test_string(self, string):
		if not len(string):
			return False

		self.stack = ["$", "S"]
		self.input = list(string)
		self.input.reverse()

		self.verbalize("Testing string: " + string)
		self.verbalize("Starting stack: " + self.stack_to_string())

		return self.parse_input()

	def parse_input(self):
		self.verbalize(self.hr())
		self.verbalize("Input stack: " + self.input_to_string())
		self.verbalize("Stack: " + self.stack_to_string())

		# Pop the next symbol off the stack.
		stack_symbol = self.stack.pop()

		# If the stack is empty and the input is too, accept.
		# Otherwise, reject.
		if stack_symbol == "$":
			return True if not self.input else False

		# If the input is empty, reject.
		if not self.input:
			return False

		# Peek at the next input symbol.
		input_symbol = self.input[-1]

		# If we have a variable...
		if stack_symbol.isalpha() and stack_symbol.isupper():
			# Grab the next rule to apply.
			rule = self.grammar.get_rule(stack_symbol, input_symbol)

			if not rule:
				self.verbalize("There was no rule to push.")
				return False

			# Push the rule onto the stack.
			symbols = list(rule)
			for symbol in reversed(symbols):
				self.stack.append(symbol)

		# If we have a terminal and it matches the next input symbol...
		elif stack_symbol == input_symbol:
			# Turn the peek into a pop.
			self.input.pop()

		else:
			return False

		return self.parse_input()

	def stack_to_string(self):
		return ''.join(reversed(self.stack))

	def print_stack(self):
		self.verbalize(self.stack_to_string())

	def input_to_string(self):
		return ''.join(reversed(self.input))

	def print_input(self):
		self.verbalize(self.input_to_string())

	def verbalize(self, output):
		if self.verbose:
			print(output)

	def hr(self):
		return "--------------------------------------------------"
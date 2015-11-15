# Jacob Martin
# CS 311

import unittest
from grammar import Grammar
from grammaranalyzer import GrammarAnalyzer

class TestGrammar(unittest.TestCase):

	def test_nonexistant_file(self):
		# No real need to assert anything, just ensure no
		# exceptions are thrown.
		grammar = Grammar("nonexistant.json")

	def test_grammar1(self):
		grammar = Grammar("grammars/grammar1.json")

		self.assertEquals(grammar.get_desc(), "{a^n # b^n | n > 0}")

	def test_grammar1_productions(self):
		grammar = Grammar("grammars/grammar1.json")

		# Check start variable productions
		rules = grammar.produces("S")
		self.assertEquals(rules, ["aSb", "#"])

		# Check nonexistant variable productions
		rules = grammar.produces("N")
		self.assertFalse(rules)

	def test_grammar1_rules(self):
		grammar = Grammar("grammars/grammar1.json")

		# Check that the correct rule is returned
		rule = grammar.get_rule("S", "a")
		self.assertEquals(rule, "aSb")

		rule = grammar.get_rule("S", "#")
		self.assertEquals(rule, "#")

		# Check nonexistant input symbol
		rule = grammar.get_rule("S", "k")
		self.assertFalse(rule)

		# Check nonexistant variable
		rule = grammar.get_rule("N", "a")
		self.assertFalse(rule)


class TestGrammarChecker(unittest.TestCase):

	def test_grammar1(self):
		grammar = Grammar("grammars/grammar1.json")
		grammar_checker = GrammarAnalyzer(grammar)

		grammar_checker.test_string("a#b")
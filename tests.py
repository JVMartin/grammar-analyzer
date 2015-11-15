# Jacob Martin
# CS 311

import unittest
from grammar import Grammar
from grammaranalyzer import GrammarAnalyzer

class TestGrammar(unittest.TestCase):

	def test_nonexistent_file(self):
		# Ensure no exceptions are thrown.
		grammar = Grammar("nonexistent.json")

		self.assertEquals(grammar.get_desc(), "")

	def test_grammar1(self):
		grammar = Grammar("grammars/grammar1.json")

		self.assertEquals(grammar.get_desc(), "{a^n # b^n | n > 0}")

	def test_grammar1_productions(self):
		grammar = Grammar("grammars/grammar1.json")

		# Check start variable productions.
		rules = grammar.produces("S")
		self.assertEquals(rules, ["aAb"])

		rules = grammar.produces("A")
		self.assertEquals(rules, ["aAb", "#"])

		# Check nonexistent variable productions.
		rules = grammar.produces("N")
		self.assertFalse(rules)

	def test_grammar1_rules(self):
		grammar = Grammar("grammars/grammar1.json")

		# Check that the correct rules are returned.
		rule = grammar.get_rule("S", "a")
		self.assertEquals(rule, "aAb")

		rule = grammar.get_rule("A", "#")
		self.assertEquals(rule, "#")

		# Check nonexistent input symbol.
		rule = grammar.get_rule("S", "k")
		self.assertFalse(rule)

		# Check nonexistent variable.
		rule = grammar.get_rule("N", "a")
		self.assertFalse(rule)


class TestGrammarAnalyzer(unittest.TestCase):

	def test_grammar1(self):
		grammar = Grammar("grammars/grammar1.json")
		grammar_analyzer = GrammarAnalyzer(grammar)

		# Check accepted strings.
		self.assertTrue(grammar_analyzer.test_string("a#b"))
		self.assertTrue(grammar_analyzer.test_string("aa#bb"))
		self.assertTrue(grammar_analyzer.test_string("aaa#bbb"))
		self.assertTrue(grammar_analyzer.test_string("aaaa#bbbb"))
		self.assertTrue(grammar_analyzer.test_string("aaaaa#bbbbb"))

		# Check rejected strings.
		self.assertFalse(grammar_analyzer.test_string("a"))
		self.assertFalse(grammar_analyzer.test_string("aa#b"))
		self.assertFalse(grammar_analyzer.test_string("a#bb"))
		self.assertFalse(grammar_analyzer.test_string("#"))
		self.assertFalse(grammar_analyzer.test_string("asdf"))

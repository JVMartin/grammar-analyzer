# Jacob Martin
# CS 311

import unittest
from grammar import Grammar
from grammarchecker import GrammarChecker

class TestGrammar(unittest.TestCase):

	def testNonexistantFile(self):
		grammar = Grammar("nonexistant.json")

	def testGrammar1(self):
		grammar = Grammar("grammars/grammar1.json")
		self.assertEquals(grammar.getDesc(), "{a^n # b^n | n > 0}")


class TestGrammarChecker(unittest.TestCase):

	def testGrammar(self):
		self.assertEqual(2, 2)
#!/usr/bin/env python3

"""
Jacob Martin
CS 311

Unit tests for the Grammar class and for the GrammarAnalyzer class.
Tests each grammar in the "grammars" folder against a variety of strings.

Run unit tests with:
python3 -m unittest tests.py
"""

import unittest
from grammar import Grammar
from grammaranalyzer import GrammarAnalyzer

class TestGrammar(unittest.TestCase):

	def test_nonexistent_file(self):
		# Ensure no exceptions are thrown.
		grammar = Grammar("nonexistent.json")

		self.assertEqual(grammar.get_desc(), "")

	def test_grammar_load(self):
		grammar = Grammar("grammars/grammar1.json")

		self.assertEqual(grammar.get_desc(), "{a^n # b^n | n > 0}")

	def test_grammar_productions(self):
		grammar = Grammar("grammars/grammar1.json")

		# Check start variable productions.
		rules = grammar.produces("S")
		self.assertEqual(rules, ["aAb"])

		rules = grammar.produces("A")
		self.assertEqual(rules, ["aAb", "#"])

		# Check nonexistent variable productions.
		rules = grammar.produces("N")
		self.assertFalse(rules)

	def test_grammar_rules(self):
		grammar = Grammar("grammars/grammar1.json")

		# Check that the correct rules are returned.
		rule = grammar.get_rule("S", "a")
		self.assertEqual(rule, "aAb")

		rule = grammar.get_rule("A", "#")
		self.assertEqual(rule, "#")

		# Check nonexistent input symbol.
		rule = grammar.get_rule("S", "k")
		self.assertFalse(rule)

		# Check nonexistent variable.
		rule = grammar.get_rule("N", "a")
		self.assertFalse(rule)


class TestGrammarAnalyzer(unittest.TestCase):

	def test_grammar1(self):
		grammar          = Grammar("grammars/grammar1.json")
		grammar_analyzer = GrammarAnalyzer(grammar)

		# Check accepted strings.
		self.assertTrue(grammar_analyzer.test_string("a#b"))
		self.assertTrue(grammar_analyzer.test_string("aa#bb"))
		self.assertTrue(grammar_analyzer.test_string("aaa#bbb"))
		self.assertTrue(grammar_analyzer.test_string("aaaa#bbbb"))
		self.assertTrue(grammar_analyzer.test_string("aaaaa#bbbbb"))
		self.assertTrue(grammar_analyzer.test_string("aaaaaa#bbbbbb"))
		self.assertTrue(grammar_analyzer.test_string("aaaaaaa#bbbbbbb"))
		self.assertTrue(grammar_analyzer.test_string("aaaaaaaa#bbbbbbbb"))
		self.assertTrue(grammar_analyzer.test_string("aaaaaaaaa#bbbbbbbbb"))
		self.assertTrue(grammar_analyzer.test_string("aaaaaaaaaa#bbbbbbbbbb"))

		# Check rejected strings.
		self.assertFalse(grammar_analyzer.test_string("xxx"))
		self.assertFalse(grammar_analyzer.test_string(""))
		self.assertFalse(grammar_analyzer.test_string("#"))
		self.assertFalse(grammar_analyzer.test_string("a"))
		self.assertFalse(grammar_analyzer.test_string("aa#b"))
		self.assertFalse(grammar_analyzer.test_string("a#bb"))
		self.assertFalse(grammar_analyzer.test_string("asdf"))
		self.assertFalse(grammar_analyzer.test_string("aaaa#bbbbbb"))

	def test_grammar2(self):
		grammar          = Grammar("grammars/grammar2.json")
		grammar_analyzer = GrammarAnalyzer(grammar)

		# Check accepted strings.
		self.assertTrue(grammar_analyzer.test_string("#"))
		self.assertTrue(grammar_analyzer.test_string("0#0"))
		self.assertTrue(grammar_analyzer.test_string("1#1"))
		self.assertTrue(grammar_analyzer.test_string("01#10"))
		self.assertTrue(grammar_analyzer.test_string("10#01"))
		self.assertTrue(grammar_analyzer.test_string("010#010"))
		self.assertTrue(grammar_analyzer.test_string("1111#1111"))
		self.assertTrue(grammar_analyzer.test_string("010001#100010"))
		self.assertTrue(grammar_analyzer.test_string("0100011#1100010"))
		self.assertTrue(grammar_analyzer.test_string("01000101#10100010"))

		# Check rejected strings.
		self.assertFalse(grammar_analyzer.test_string("xxx"))
		self.assertFalse(grammar_analyzer.test_string(""))
		self.assertFalse(grammar_analyzer.test_string("0"))
		self.assertFalse(grammar_analyzer.test_string("0#1"))
		self.assertFalse(grammar_analyzer.test_string("1#10"))
		self.assertFalse(grammar_analyzer.test_string("01#01"))
		self.assertFalse(grammar_analyzer.test_string("11#111"))
		self.assertFalse(grammar_analyzer.test_string("111#11"))
		self.assertFalse(grammar_analyzer.test_string("111#110"))
		self.assertFalse(grammar_analyzer.test_string("0111#110"))

	def test_grammar3(self):
		grammar          = Grammar("grammars/grammar3.json")
		grammar_analyzer = GrammarAnalyzer(grammar)

		# Check accepted strings.
		self.assertTrue(grammar_analyzer.test_string("a#b#c#"))
		self.assertTrue(grammar_analyzer.test_string("a#b#cc#"))
		self.assertTrue(grammar_analyzer.test_string("a#b#ccc#"))
		self.assertTrue(grammar_analyzer.test_string("a#b#cccc#"))
		self.assertTrue(grammar_analyzer.test_string("a#b#ccccc#"))
		self.assertTrue(grammar_analyzer.test_string("aa#bb#c#"))
		self.assertTrue(grammar_analyzer.test_string("aa#bb#cc#"))
		self.assertTrue(grammar_analyzer.test_string("aa#bb#ccc#"))
		self.assertTrue(grammar_analyzer.test_string("aa#bb#cccc#"))
		self.assertTrue(grammar_analyzer.test_string("aa#bb#ccccc#"))
		self.assertTrue(grammar_analyzer.test_string("aaaa#bbbb#c#"))
		self.assertTrue(grammar_analyzer.test_string("aaaaa#bbbbb#c#"))
		self.assertTrue(grammar_analyzer.test_string("aaaaa#bbbbb#cc#"))
		self.assertTrue(grammar_analyzer.test_string("aaaaa#bbbbb#ccc#"))
		self.assertTrue(grammar_analyzer.test_string("aaaaa#bbbbb#cccc#"))
		self.assertTrue(grammar_analyzer.test_string("aaaaa#bbbbb#ccccc#"))

		# Check rejected strings.
		self.assertFalse(grammar_analyzer.test_string("xxx"))
		self.assertFalse(grammar_analyzer.test_string(""))
		self.assertFalse(grammar_analyzer.test_string("a"))
		self.assertFalse(grammar_analyzer.test_string("a#b"))
		self.assertFalse(grammar_analyzer.test_string("a#b#c"))
		self.assertFalse(grammar_analyzer.test_string("####"))
		self.assertFalse(grammar_analyzer.test_string("abcd"))
		self.assertFalse(grammar_analyzer.test_string("aaaaa#bbb#c#"))
		self.assertFalse(grammar_analyzer.test_string("aaaaa##ccccc#"))
		self.assertFalse(grammar_analyzer.test_string("aaaa##ccccc#"))
		self.assertFalse(grammar_analyzer.test_string("aaa##ccccc#"))

	def test_grammar4(self):
		grammar          = Grammar("grammars/grammar4.json")
		grammar_analyzer = GrammarAnalyzer(grammar)

		# Check accepted strings.
		self.assertTrue(grammar_analyzer.test_string("a#b#c#d"))
		self.assertTrue(grammar_analyzer.test_string("aa#bb#c#d"))
		self.assertTrue(grammar_analyzer.test_string("a#b#cc#dd"))
		self.assertTrue(grammar_analyzer.test_string("aaa#bbb#c#d"))
		self.assertTrue(grammar_analyzer.test_string("a#b#ccc#ddd"))
		self.assertTrue(grammar_analyzer.test_string("aaaa#bbbb#c#d"))
		self.assertTrue(grammar_analyzer.test_string("a#b#cccc#dddd"))
		self.assertTrue(grammar_analyzer.test_string("aa#bb#cccc#dddd"))
		self.assertTrue(grammar_analyzer.test_string("aaa#bbb#cccc#dddd"))
		self.assertTrue(grammar_analyzer.test_string("aaaa#bbbb#ccccc#ddddd"))
		self.assertTrue(grammar_analyzer.test_string("a#b#cccccc#dddddd"))
		self.assertTrue(grammar_analyzer.test_string("aaaaaaa#bbbbbbb#c#d"))

		# Check rejected strings.
		self.assertFalse(grammar_analyzer.test_string("xxx"))
		self.assertFalse(grammar_analyzer.test_string(""))
		self.assertFalse(grammar_analyzer.test_string("#"))
		self.assertFalse(grammar_analyzer.test_string("a#b#c#"))
		self.assertFalse(grammar_analyzer.test_string("#b#c#d"))
		self.assertFalse(grammar_analyzer.test_string("a#bb#c#d"))
		self.assertFalse(grammar_analyzer.test_string("a#b#c#dd"))
		self.assertFalse(grammar_analyzer.test_string("a#bb#c#dd"))
		self.assertFalse(grammar_analyzer.test_string("aa#bb#cc#dd#"))
		self.assertFalse(grammar_analyzer.test_string("aaa#bbb#ccc#dddd"))
		self.assertFalse(grammar_analyzer.test_string("aaa#bbb#ccc#dddd##"))

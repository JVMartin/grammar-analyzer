#!/usr/bin/env python3

"""
Use the grammar analyzer to load the grammar of your choice and an input
string of your choice, then see if the grammar can generate the string.

usage:
	./analyze.py <path to grammar json> <input string>

examples:
	./analyze.py grammars/grammar1.json "a#b"
	./analyze.py grammars/grammar1.json ""
"""

import sys
from grammar import Grammar
from grammaranalyzer import GrammarAnalyzer

args = sys.argv

# Helpful usage hints.
if len(args) != 3:
	print("usage:")
	print("\t./analyze.py <path to grammar json> <input string>\n")
	print("examples:")
	print("\t./analyze.py grammars/grammar1.json \"a#b\"")
	print("\t./analyze.py grammars/grammar1.json \"\"")
	sys.exit()

path_to_grammar = args[1]
input_string    = args[2]

grammar          = Grammar(path_to_grammar)
grammar_analyzer = GrammarAnalyzer(grammar)

if grammar_analyzer.test_string(input_string):
	print(grammar.get_desc() + ' CONTAINS "' + input_string + '"')
else:
	print(grammar.get_desc() + ' DOES NOT CONTAIN "' + input_string + '"')

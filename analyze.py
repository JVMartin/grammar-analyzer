#!/usr/bin/env python3
# Jacob Martin
# CS 311

# Use the grammar analyzer to load the grammar of your choice and
# test the input string of your choice.

# usage:
#        python3 analyze.py <path to grammar json> <input string>
#
# examples:
#        python3 analyze.py grammars/grammar1.json "a#b"
#        python3 analyze.py grammars/grammar1.json ""

import sys
from grammar import Grammar
from grammaranalyzer import GrammarAnalyzer

args = sys.argv

# Helpful usage hints.
if len(args) != 3:
	print("usage:")
	print("\tpython3 analyze.py <path to grammar json> <input string>\n")
	print("examples:")
	print("\tpython3 analyze.py grammars/grammar1.json \"a#b\"")
	print("\tpython3 analyze.py grammars/grammar1.json \"\"")
	sys.exit()

path_to_grammar = args[1]
input_string    = args[2]

grammar          = Grammar(path_to_grammar)
grammar_analyzer = GrammarAnalyzer(grammar)

if grammar_analyzer.test_string(input_string):
	print(grammar.get_desc() + ' ACCEPTS "' + input_string + '"')
else:
	print(grammar.get_desc() + ' REJECTS "' + input_string + '"')

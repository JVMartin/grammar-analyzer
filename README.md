Python Grammar Analyzer
=======================

[![Build Status](https://travis-ci.org/JVMartin/grammar-analyzer.svg)](https://travis-ci.org/JVMartin/grammar-analyzer)

A simple grammar analyzer written in Python.

Grammar Formatting
------------------
1.  All rules in the grammar must have a terminal as the first symbol
on the right hand side of the rule.

2.  No variable in the grammar can have two rules with the same terminal
as the first symbol on the right hand side.
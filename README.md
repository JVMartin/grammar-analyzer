Python Grammar Analyzer
=======================

[![Build Status](https://travis-ci.org/JVMartin/grammar-analyzer.svg)](https://travis-ci.org/JVMartin/grammar-analyzer)

A simple grammar analyzer written in Python.

Usage:
```
./analyze.py <path to grammar json> <input string>
```

Examples:
```
./analyze.py grammars/grammar1.json "a#b"
./analyze.py grammars/grammar1.json ""
```

Grammar Formatting
------------------
1.  All rules in the grammar must have a terminal as the first symbol
on the right hand side of the rule.

2.  No variable in the grammar can have two rules with the same terminal
as the first symbol on the right hand side.

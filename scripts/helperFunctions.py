#!/usr/bin/env python

bold      = "\033[1;30m"
red       = "\033[0;31m"
green     = "\033[0;32m"
defcol    = "\033[m"
yellowbkg = "\033[0;30;43m"
graybkg   = "\033[48;5;255m"

def info(*args):
	if args[0]<3: print yellowbkg,
	if args[0]==0: print "-"*30,
	elif args[0]>0: print " "*(args[0]-1),"++",
	for text in args[1:]: print text,
	if args[0]<3: print defcol
	else: print

def error(*args):
	print
	print red,
	for text in args: print text,
	print default
	print

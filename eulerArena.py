#################################################################################
	#							The Arena of Euler
	#
	#	There may be some really ugly code here, anyhting here is unfinished
	#
	#
	#
	#
##################################################################################

import sys
import math
import numpy as np
import eulerFunctions as eulFunc
import itertools as it

def fibGen():
	a,b = 0,1
	yield a
	yield b
	while True:			
		yield a+b
		a,b = b, a+b

def getFibIndexWithLength(limit):
	phi = (1+math.sqrt(5))/2

	return round((limit-1 + math.log10(5)/2)/math.log10(phi))

def getFibAtIndex(index):
	phi = (1+math.sqrt(5))/2

	return round((1/math.sqrt(5)) * ((phi ** index) - ((phi - 1) ** index)))

print(getFibAtIndex(1))


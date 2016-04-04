################################################################################################
#						Project Euler - Python3
#
#		 	This file is the main build file for my Solution for Project Euler
#		 	Most of the actual math/logic is located in eulerFunction.py
# 
#
################################################################################################
import sys
import time
from datetime import timedelta
from eulerProblemInfo import eulerProblemInfo
import eulerFunctions as eulFunc


# Main Entry point for extraction solutions called at the bottom of the file
	# with options for which parameters to use.
	#
	# 							***Parameters****
	# isTest determines if functions that are slow with the standard parameters 
	# 	will use paramters from testParams[] if they exist 
	# problemNumber determines which problems will be executed, if <0 all will 
	#	be run, if the problem has not been finished yet a message will be printed
def projectEuler(isTest, problemNumber):

	# Refernce Object that contains Project Euler Info
	info = eulerProblemInfo()

	# Used for seperating output and increasing readability
	problemSep = "*****" * 10

	# This is used to generating function calls
	prefix = 'euler'

	# These are testing parameters for Project Euler problems
	# If set to None no test parameter is being used
	# Index corresponds to problem number
	testParams = [None] * (info.problemsSolved + 2)
	testParams[0] = "This contains test parameters for time consuming problems"
	testParams[4] = 99
	testParams[5] = range(1,5+1)
	testParams[10] = 100000
	testParams[12] = 50
	testParams[14] = 100
	testParams[23] = 1000

	##########
	#
	#	This Section is where each problem is defined as a function and that function
	#	calls the applicable functions in eulFunc(eulerFunction.py)
	#
	#	Function naming is used to allow for a looping call that will automatically 
	#	call functions as they are completed(as in code complete) and the problems are
	#	added to problems.txt
	#
	##########

	def euler1(limit):

		return sum(eulFunc.getMutlpilesOf3or5(limit))

	def euler2(limit):

		return sum(eulFunc.evenFib(limit))

	def euler3(x):

		return max(eulFunc.getPrimeFactors(x))

	def euler4(limit):

		return eulFunc.getPalindromes(limit)

	# When using standard paramters this takes a while(~5 Seconds)
	def euler5(divList):

		return eulFunc.getLcmOfRange(divList)

	def euler6(numRange):

		return (eulFunc.getSquareOfSum(numRange) - eulFunc.getSumOfSquares(numRange))

	def euler7(x):

		return eulFunc.getXPrimeNum(x)

	def euler8(paramDic):

		return eulFunc.largestProductInSeries(paramDic['series'], paramDic['count'])
	
	def euler9(x):
		result = 1
		for x in eulFunc.getPythagoreanTripletWithSum(x):
			result *= x
		return result

	# When using standard paramters this is a little slow(~2 Seconds)
	def euler10(x):
		primeGen = eulFunc.genPrime()
		primes = []
		primes.append(next(primeGen))
		while(primes[-1] < x):
		 	primes.append(next(primeGen))
		if(primes[-1] > x):del primes[-1]

		return sum(primes)

	def euler11(paramDic):

		return eulFunc.getAdjancyProduct(paramDic)

	# When using standard paramters this takes a while(~5 Seconds)
	def euler12(divisors):
		x = 0
		i = 1
		while(eulFunc.getNumOfDivisors(x) <= divisors):
			x += i
			i += 1
		return x

	def euler13(paramDic):
		# This problem could easliy be solved using the sum() function
			# This problem was meant to overload the typical variable size
			# The statement below would work just as well:
			# 	return int(str(sum(paramDic['numbers']))[-paramDic[-'digits']:])
		result = 0
		digits = paramDic['digits']
		for num in paramDic['numbers']:
			result = eulFunc.getLSDofSum(result, num, digits)
		return result

	# When using standard paramters this takes a quite while(~40 Seconds)
	def euler14(x):

		return eulFunc.getLongestCollatz(x)[0]

	def euler15(paramDic):

		return eulFunc.getUniqueLatticePaths(paramDic['width'], paramDic['height'])

	def euler16(num):

		return eulFunc.getSumOfDigits(num)

	def euler17(numRange):
		numStrList = []
		totalLetters = 0
		for x in numRange:
			numStrList.append(eulFunc.numToWords(x))
		for s in numStrList:
			totalLetters += eulFunc.getLettersInString(s)
		return totalLetters

	def euler18(grid):

		return eulFunc.getTrianglePathSum(info.eulerParams[18])

	# Skipping this problem because the calendar system makes for super annoying and ugly code
	def euler19(z):

		print(z)

	def euler20(x):

		return eulFunc.getSumOfDigits(eulFunc.getFactorial(x))

	def euler21(limit):
	
		return sum(eulFunc.getAmicableNumbers(limit))

	# 	This problem ended up with more code here than others,
		# Couldn't think of anything contained within that fit 
		# in eulerFunctions.py
	def euler22(fileName):
		# Take the file and throw it into a list with excess trimmed
		def parseFile(fileName):
			f = open(fileName, 'r+')
			names = []
			for name in f.read().split(","):
				names.append(name.strip('\"'))
			f.close()

			return names

		total = 0
		i = 1
		# For each name in the sorted names list evaluate nameValue * place in list and add to total
		for name in sorted(parseFile(fileName)):
			total += i * eulFunc.getWordSum(name)
			i += 1
		return total
	
	def euler23(limit):
		amicableNums = eulFunc.getAbundantNumRange(limit)
		notSumSet = set()
		for i in range(1, limit+1):
			notSumSet.add(i)
		while(len(amicableNums) != 0):
			for num in amicableNums:
				tot = amicableNums[0] + num
				if(tot in notSumSet):
					notSumSet.remove(tot)
			amicableNums.remove(amicableNums[0])

		return sum(notSumSet)

	def euler24(paramDic):

		return eulFunc.lexicographicPerm(paramDic['charList'], paramDic['permNum'])

	def euler25(limit):
		
		return eulFunc.getFibIndexWithLength(limit)


	print(problemSep)
	print("Number of completed problems: ", info.problemsSolved)
	print(problemSep)

	#########################################
	#
	#	This is where all the functions are called, timed, and printed; Along with formatting and context.
	#	i is used to determine the current problem number and combined with the prefix(euler) used to call
	#	the completed functions so that as problems are finished there are fewer places to update to include new
	#	solutions.
	#
	#	TODO: Things in the for statement should be its own function.
	#
	##########################################


	def callFunction(method, params):
		t = time.time()

		if(params != None):
			print(method(params))
		else: print(method())

		tElapsed = timedelta(seconds = time.time() - t)
		print("This problem took: ", tElapsed.total_seconds()," Seconds.")

	def getParameters(problemNum):
		if(isTest and testParams[problemNum] != None):
			return testParams[problemNum]
		else: return info.eulerParams[problemNum]
		
	if(problemNumber <= 0):
		for i in range(1,info.problemsSolved+1):
			print("Project Euler problem #",i)
			print(info.problemText[i])
			callFunction(locals()[prefix + str(i)], getParameters(i))
			print(problemSep)

	elif(problemNumber < info.problemsSolved+1):
		print("Project Euler problem #",problemNumber)
		print(info.problemText[problemNumber])
		callFunction(locals()[prefix + str(problemNumber)], getParameters(problemNumber))
			
	else: print("Requested Problem not yet solved!")

# For ease of running and testing in SublimeText which has trouble with console input
isTestRun = False
problemNumber = 0

for arg in sys.argv:
	if(str(arg).lower() == "test"):
		isTestRun = True
	elif(arg.isdigit()):
		problemNumber = int(arg)

if(isTestRun):
	projectEuler(isTestRun, problemNumber)
else: projectEuler(False, problemNumber)
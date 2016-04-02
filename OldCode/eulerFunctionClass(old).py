####################################################################
	#			**********OLD************	
	#			Euler Functions - Python3
	#	
	#	This was written as a class early on for some reason,
	#	it has been replaced as a classless script which lets
	#	all the self refferences to be removed.
	#	This contains the math/logic used by projectEuler.py
	#	
	#
	#	Apologies for the horrible use of math terms
###################################################################

import sys
import math
class eulerFunction:

	#Return the nth Fibonacci Number
	def fib(self, count):
		a,b = 1,1
		fibs = []
		for i in range(count-1):
			fibs.append(a)
			a,b = b, a+b
		fibs.append(a)
		return fibs 

	#Recursive Fibonacci
	def fibR(self, x):
		if x == 1 or x == 2:
			return 1
		return fibR(x-1)+fibR(x-2)

	#Returns Array of factors of x
	def getFactors(self, x):
		factors = []
		lim = int(math.sqrt(x))

		for y in range(1,lim+1):
			if(x%y == 0):
				factors.append(y)
				if(x/y != y):
					factors.append(int(x/y))

		return factors

	#Returns list of divisors without x
	#Not sure if the math vocab is accurate
	def getProperDivisors(self, x):
		div = (self.getFactors(x))
		div.remove(x)
		return div

	#Uses getFactors function and returns the length of the produced array
	def getNumOfDivisors(self, x):

		return len(self.getFactors(x))

	#Returns array of the prime factors of x
	def getPrimeFactors(self, x):
		factors = []
		i = 2
		while(i < x):
			if( x%i == 0 ):
				x = int(x/i)
				factors.append(i)
				i = 2
			else:
				i += 1
		factors.append(x)
		return factors

	#Returns array of the unique prime factors of x
	def getUniquePrimeFactors(self, x):
		factors = []
		i = 2
		while(i < x):
			if( x%i == 0 ):
				x = x/i
				if(i not in factors):
					factors.append(i)
				i = 2
			else:
				i += 1
		if(x not in factors):
			factors.append(x)
		return factors

	def isPrime(self, x):
		i = 2

		if(x == 2):return True

		while(i < x/2):
			if(x%i == 0):
				return	False	
			else:
				i += 1	
		return True

	def getFactorial(self, x):
		if(x == 0):
			return 1
		y = x 
		while x >= 2:
			y *= (x-1)
			x -= 1
		return y	

	#Recursive Factorial with recursion depth catch	
	def getFactorialR(self, x):
		if(x == 1 or x == 0):
			return 1
		elif(x >= sys.getrecursionlimit()):		
			return "Out of Range: Recursion Overflow, limit is: " + str(sys.getrecursionlimit())				#Alternatively the recursion depth could be changed using sys.setrecursionlimit(x+1)
		elif(x < -1):
			return 0
		elif(x > 0):
			return x * self.getFactorialR(x-1)

	#Return an array of of primes with length limit
	def getPrimeList(self, limit):
		i = 3							#Start Prime testing at 3 to avoid even prime
		primes = [2,]					#Prime the prime list witht he only even prime
		while(len(primes) < limit):
			if(self.isPrime(i)):
				primes.append(i)
			i += 2						#Increment by 2 to only check odd numbers
		return primes

	#Prime number generator
	def genPrime(self):
		multipleDict = {}
		x = 2
		while True:
			if x not in multipleDict:											#Check for entry in Dictionary
				yield x 														#If not in dict, then is prime, spit out x
				multipleDict[(x*x)] = [x]										#Add x^2 to Dict with x 
			else:
				for factors in multipleDict[x]:									
					multipleDict.setdefault(factors + x, []).append(factors)
				del multipleDict[x]
			x += 1
	        
	def isMultiplesOf3or5(self, x):
		if(x%5 == 0 or x%3 == 0):
			return True
		else: return False

	def getMutlpilesOf3or5(self, limit):
		x = 1
		multiples = []
		while(x <= limit):
			if(self.isMultiplesOf3or5(x)):
				multiples.append(x)
				x += 1
			else: x += 1
		return multiples

	#Returns an Array that conains all the even Fibs under limit
	def evenFib(self, limit):
		x,y = 1,1
		evenFibs = []
		while(y <= limit):
			if(y%2 == 0):
				evenFibs.append(y)
			x,y = y, x+y
		return evenFibs

	def isPalindrome(self, x):
		#Compares the string of x against the reversed string of x
		#[start:stop:step] using a negative in the steps iterate through the string backwards
		return str(x) == str(x)[::-1]

	#Returns the greatest palindrome number less than the limit
	def getPalindromes(self, limit):
		greatestPalindrome = 0
		x,y = limit, limit
		base = 10**(len(str(limit))-1)
		while(x >= base):
			while(y >= base):
				if(self.isPalindrome(x*y) and x*y > greatestPalindrome):
					greatestPalindrome = x*y
					y -= 1
				else: y -= 1
			x -= 1
			y = limit
		return greatestPalindrome

	#Determines if y is divisible by all numbers withing divRange
	def isDivisibleByRange(self, y, divRange):
		for x in divRange:
			if y%x != 0:
				return False
		return True

	#Returns the Lowest common denominator of numbers in divList
	def getLcmOfRange(self, divList):
		y = max(divList)
		yStep = max(divList)
		while(self.isDivisibleByRange(y, divList) == False):
			y += yStep
		return y

	#Returns the sum of the squares of the numbers contained in numRange
	def getSumOfSquares(self, numRange):
		total = 0
		for x in numRange:
			total += x**2
		return total

	#Returns the square of the sum of the numbers in numRange
	def getSquareOfSum(self, numRange):

		return (sum(numRange)**2)

	#Returns the xth prime number using the prime number generator
	def getXPrimeNum(self, x):
		primeGen = self.genPrime()
		prime = 0
		for y in range(x):
			prime = next(primeGen)
		return prime

	#Returns the maximum product of sampleSize adjacent digits in series
	def largestProductInSeries(self, series, sampleSize):
		loc = 0
		tempProduct = 1
		maxProduct = 0
		while(loc < len(str(series)) - sampleSize+1):
			for x in (str(series)[loc:(loc+sampleSize)]):
				tempProduct *= int(x)
			if(tempProduct > maxProduct):
				maxProduct = tempProduct
			tempProduct = 1
			loc += 1
		return maxProduct

	#Returns all the Prime factors that numbers in numList share
	def getCDPrime(self, numList):
		factorLists = []
		cdList = []
		i = 0
		for x in numList:
			factorLists.append(self.getUniquePrimeFactors(x))

		return list(set.intersection(*map(set,factorLists)))

	#Returns the Greatest Common prime factor of numbers in numList
	def getGCDPrime(self, numList):

		return max(self.getCDPrime(numList))

	#Returns a list containing all the common factors of the numbers in numList
	def getCD(self, numList):
		factorLists = []
		i = 0
		for x in numList:
			factorLists.append(self.getFactors(x))

		return list(set.intersection(*map(set,factorLists)))

	#Returns the Greatest Common Factors of number in numList
	def getGCD(self, numList):

		return max(self.getCD(numList))

	#Determines if the Greatest Common Denominator of numbers in numList is 1
	def isCoPrime(self, numList):
		if(getGCD(numList) == 1):
			return True
		else: return False

	#Get the Pythagorean triplet where a+b+c = x
	def getPythagoreanTripletWithSum(self, x):
		genTriplet = self.genPrimPythTriplet()
		triplet = next(genTriplet)
		i = 1
		while(True):
			if(sum(triplet) == x):
				return triplet
			elif(sum([y*i for y in triplet]) == x):
				return [y*i for y in triplet]
			elif(sum(triplet) < x and sum([y*i for y in triplet]) < x):
				i += 1
				continue
			elif(sum(triplet) > x):
				triplet = genTriplet.next()
				continue
			elif(sum([y*i for y in triplet]) > x):
				i = 1
				triplet = next(genTriplet)
				continue

	#Generates Pythagorean triplets(a^2+b^2=c^2)
	def genPrimPythTriplet(self):
		m,n = 2,1
		while(True):
			while(m > n):
				if(self.getGCD([m,n]) == 1 and (m-n & 1) == 1):
					a = 2*m*n
					b = m**2 - n**2
					c = m**2 + n**2
					if(a < b):
						yield [a,b,c]
					else:
						yield [b,a,c]
				n += 1
			m,n = m+1, 1

	#Returns an array of x Primative(a,b,c are coprime) Pythagorean triplets
	def getPrimPythagoreanTriplets(self, x):
		m,n = 2,1
		triplets = []

		while(len(triplets) < x):
			while(m > n):
				if(self.getGCD([m,n]) == 1 and (m-n & 1) == 1):
					a = 2*m*n
					b = m**2 - n**2
					c = m**2 + n**2
					if(a < b):
						triplets.append([a,b,c])
					else:
						triplets.append([b,a,c])
				n += 1
			m,n = m+1, 1
		return triplets

	#Determines if a^2+b^2=c^2
	def isPythTriplet(self, numList):
		if(math.hypot(numList[0],numList[1]) == (numList[2])):
			return True
		else: return False

	#Returns the product of maximum product of paramDic['count'] adjacent numbers in anydirection contained in paramDic[]
	def getAdjancyProduct(self, paramDic):
		grid = paramDic['grid']
		count = paramDic['count']

		#a,b will refer to coordinates of current position
		#When a = 0 it refers to the first(top) row
		#When b = 0 it refers to the left-most column
		a,b = 0,0
		maxProd = 0

		def getHorizontal(x,y):
			result = 1
			if(y+count >= len(grid[x])):return 0
			for i in range(count):
				result *= grid[x][y+i]
			return result

		def getVertical(x,y):
			result = 1
			if(x+count >= len(grid)):return 0
			for i in range(count):
				result *= grid[x+i][y]
			return result
		
		def getUphill(x,y):
			result = 1
			if(x+count > len(grid) or y-count < 0):return 0
			for i in range(count):
				result *= grid[x+i][y-i]
			return result

		def getDownhill(x,y):
			result = 1
			if(x+count >= len(grid) or y+count >= len(grid[x])):return 0
			for i in range(count):
				result *= grid[x+i][y+i]
			return result

		def processNum(x,y):
			products = []
			tests = (getHorizontal, getVertical, getDownhill, getUphill)
			for test in tests:
				products.append(test(x,y))
			return products
		for row in grid:
			for num in row:
				numMax = max(processNum(a,b))
				if(numMax > maxProd): 
					maxProd = numMax
				b += 1
			b = 0
			a += 1
		return maxProd

	#This Function is not required or particuarly useful in python
	def getLeastSigDigits(self, num, digits):

		return int(str(num)[-digits:])
	
	#This Function is not required or particuarly useful in python
	def getLSDofSum(self, x, y, digits):
		x += y
		x = self.getLeastSigDigits(x, digits)

		return x

	#Returns the Longest Collatz Chain that starts with number less than limit
	def getLongestCollatz(self, limit):
		tChain = []
		maxChain = [0]

		def getChain(x):
			chain = []
			while(x != 1 and x != maxChain[0]):
				chain.append(x)
				if(x&1 == 1):
					x = 3*x+1
				elif(x&1 == 0):
					x >>= 1
			if(x == 1):
				chain.append(x)
				return chain
			elif(x == maxChain[0]):
				for y in maxChain:
					chain.append(y)
				return chain

		for x in range(limit):
			tChain = getChain(x+1)
			if(len(tChain) > len(maxChain)):
				maxChain = tChain
		return maxChain

	#Returns a list contain the collatz chain that starts with x
	def getCollatzChain(self, x):
		chain = []
		while(x != 1):
			chain.append(x)
			if(x&1 == 1):
				x = 3*x+1
			elif(x&1 == 0):
				x >>= 1
		chain.append(x)
		return chain

	#Checks if numList conforms to Collatz Function
	def isCollatzChain(self, numList):
		i = 0
		while(i < len(numList)):
			x = numList[i]
			if(x == 1):
				return True
			elif(x & 1 == 1 and 3*x+1 == numList[i+1]):
				i += 1
				continue
			elif(x & 1 == 0 and x >> 1 == numList[i+1]):
				i += 1
				continue
			else: return False
		return True

	#Returns the number of unique paths(using routing defined in problem #15) across a grid defined by width and height
	def getUniqueLatticePaths(self, width, height):
		import numpy as np
		from itertools import product

		grid  = np.zeros((width+1,height+1),dtype=float)			#Uses Numpy to create a 2D grid filled with zeroes

		#Fills in the edge cases for the grid where there is only one path
		def initializeGrid(grid):
			width = len(grid)
			height = len(grid[0])

			for x in range(width):
				grid[x][height-1] = 1
			for y in range(height):
				grid[width-1][y] = 1
			grid[width-1][height-1] = 0

			return grid	
		
		#Starting from the final grid point the number of paths are reverse propogated across the grid	
		def processGrid(grid):
			width,height = len(grid)-1,len(grid[0])-1
			for x,y in product(range(width,-1,-1), range(height,-1,-1)):
				if(x == width or y == height):
					continue
				grid[x][y] = int(grid[x+1][y] + grid[x][y+1])
			return grid

		grid = initializeGrid(grid)
		grid  = processGrid(grid)

		return grid[0][0]

	#Sums the digits in num
	def getSumOfDigits(self, num):
		total = 0
		for c in str(num):
			total += int(c)
		return total

	#Converts an int into english, bleh
	#Surely this is not the best way to do this, its so ugly
	def numToWords(self, num):
		numStr = str(num)
		singleDigit = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
		teens = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
		tens = {1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
		powersOfTen = {2:'hundred',3:'thousand'}

		result = ''

		while(len(numStr) > 0):
			if(int(numStr[0]) == 0):
				numStr = numStr[1:]
			elif(len(numStr) == 4):
				result += singleDigit[int(numStr[0])]+'-'+powersOfTen[3]+' '
				numStr = numStr[1:]
			elif(len(numStr) == 3):
				result += singleDigit[int(numStr[0])]+'-'+powersOfTen[2]+' '
				numStr = numStr[1:]
			elif(len(numStr) == 2 and int(numStr[0]) == 1):
				if(len(result) > 1):
					result += 'and '+ teens[int(numStr[0:])]
				else:
					result += teens[int(numStr[0:])]
				numStr = ''
			elif(len(numStr) == 2 and int(numStr[0]) != 0 and int(numStr[1]) == 0):
				if(len(result) > 1):
					result += 'and '+ tens[int(numStr[0])]
				else:
					result += tens[int(numStr[0])]
				numStr = ''
			elif(len(numStr) == 2 and int(numStr[0]) != 0 and int(numStr[1]) != 0):
				if(len(result) > 1):
					result += 'and '+ tens[int(numStr[0])]+'-'+singleDigit[int(numStr[1])]
				else:
					result += tens[int(numStr[0])]+'-'+singleDigit[int(numStr[1])]
				numStr = ''
			elif(len(numStr) == 1):
				if(len(result) > 1):
					result += 'and '+singleDigit[int(numStr[0])]
				else:
					result += singleDigit[int(numStr[0])]
				numStr = ''
		return result

	#Returns the number of letters in a string
	def getLettersInString(self, string):
		i = 0
		for x in string:
			if(x.isalpha()):
				i += 1
		return i

	#Returns the greatest sum of the path down a triangle
	def getTrianglePathSum(self, grid):
		row = len(grid) - 2
		column =  0
		while(row >= 0):
			while(column < len(grid[row])):
				grid[row][column] = grid[row][column] + max(grid[row+1][column], grid[row+1][column+1])
				column += 1
			column = 0
			row -= 1
		return grid[0][0]

	#Returns list of all amicable numbers under limit
	#Should probably change it up so that numbers are added in pairs to a set so the relationship is retained
	def getAmicableNumbers(self, limit):
		amicDic = dict()
		amiNum = []
		#Build a dict of the relating x and the sum of divisors
		for x in range(1, limit):
			divs = (self.getProperDivisors(x))
			amicDic[x] = sum(divs)

		#Check dict i:sum == sum:i
		for i in iter(amicDic):
			if(sum(self.getProperDivisors(i)) in amicDic):
				if(i != amicDic[i] and i == amicDic[sum(self.getProperDivisors(i))]):
					amiNum.append(i)

		return amiNum

	#Returns the sum of the letters in a word given a/A=1, b/B=2, c/C=3....
	def getWordSum(self, word):
		total = 0
		word = word.lower()
		for c in word:
			total += ord(c)-96
		return total

	#Takes the euler22 text file and creates a list of the names contained within
	def parseEuler22File(self, fileName):
		f = open(fileName)
		outList = [f.read(-1)]
		f.close()
		print(outList[0])
		return outList

	#Check if the sum of the proper divisors of x is x
	def isPefectNumber(self, x):
		if(x == sum(self.getProperDivisors)):
			return True
		else: return False
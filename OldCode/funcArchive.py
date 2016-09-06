#Archive functions
#Storage for old functions

#These function are pre-eulerFunction.py
	def fib(count):
		a,b = 1,1
		fibs = []
		for i in range(count-1):
			fibs.append(a)
			a,b = b, a+b
		fibs.append(a)
		return fibs

	def fibR(x):
		if x == 1 or x==2:
			return 1
		return fibR(x-1)+fibR(x-2)

	def getFactors(x):
		factors = []
		i = 2
		factors.append(1)
		while(i <= x/2):
			if( x%i == 0 ):
				factors.append(i)
			i += 1
		factors.append(x)
		return factors

	def getPrimeFactors(x):
		factors = []
		i = 2
		while(i < x):
			if( x%i == 0 ):
				x = x/i
				factors.append(i)
				i = 2
			else:
				i += 1
		factors.append(x)
		return factors

	def getUniquePrimeFactors(x):
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

	def isPrime(x):
		i = 2
		while(i < x/2):
			if(x%i == 0):
				return	False	
			else:
				i += 1	
		return True

	def getFactorial(x):
		y = x 
		while x >= 2:
			y *= (x-1)
			x -= 1
		return y	

	def getPrimeList(limit):
		i = 3
		primes = [2,]
		while(len(primes) < limit):
			if(isPrime(i)):
				primes.append(i)
			i += 2	
		return primes

	def isMultiplesOf3or5(x):
		if(x%5 == 0 or x%3 == 0):
			return True
		else: return False

	def getMutlpilesOf3or5(limit):
		x = 1
		multiples = []
		while(x <= limit):
			if(isMultiplesOf3or5(x)):
				multiples.append(x)
				x += 1
			else: x += 1
		return multiples

	def evenFib(limit):
		x,y = 1,1
		evenFibs = []
		while(y <= limit):
			if(y%2 == 0):
				evenFibs.append(y)
			x,y = y, x+y
		return evenFibs

	def isPalindrome(x):
		#Compares the string of x against the reversed string of x
		#[start:stop:step] using a negative in the steps iterate through the string backwards
		return str(x) == str(x)[::-1]

	def getPalindromes(limit):
		greatestPalindrome = 0
		x,y = limit, limit
		base = 10**(len(str(limit))-1)
		while(x >= base):
			while(y >= base):
				if(isPalindrome(x*y) and x*y > greatestPalindrome):
					greatestPalindrome = x*y
					y -= 1
				else: y -= 1
			x -= 1
			y = limit
		return greatestPalindrome

	def isDivisibleByRange(y, divRange):
		for x in divRange:
			if y%x != 0:
				return False
		return True

	def getLcmOfRange(divList):
		y = max(divList)
		yStep = max(divList)
		while(isDivisibleByRange(y, divList) == False):
			y += yStep
		return y

	def getSumOfSquares(numRange):
		total = 0
		for x in numRange:
			total += x**2
		return total

	def getSquareOfSum(numRange):

		return (sum(numRange)**2)

	def getXPrimeNum(x):
		i = 1
		while(x > 0):
			if(isPrime(i)):
				x -= 1
			i += 2
		return (i - 2)

	def largestProductInSeries(series, sampleSize):
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

	def getCDPrime(numList):
		factorLists = []
		cdList = []
		i = 0
		for x in numList:
			factorLists.append(getUniquePrimeFactors(x))

		return list(set.intersection(*map(set,factorLists)))

	def getGCDPrime(numList):

		return max(getCDPrime(numList))

	def getCD(numList):
		factorLists = []
		i = 0
		for x in numList:
			factorLists.append(getFactors(x))

		return list(set.intersection(*map(set,factorLists)))

	def getGCD(numList):

		return max(getCD(numList))

	def isCoPrime(numList):
		if(getGCD(numList) == 1):
			return True
		else: return False

	def getPythagoreanTripletWithSum(x):
		genTriplet = genPrimPythTriplet()
		triplet = genTriplet.next()
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
			elif(([y*i for y in triplet]) > x):
				i = 1
				triplet = genTriplet.next()
				continue

	def genPrimPythTriplet():
		m,n = 2,1
		while(True):
			while(m > n):
				if(getGCD([m,n]) == 1 and (m-n & 1) == 1):
					a = 2*m*n
					b = m**2 - n**2
					c = m**2 + n**2
					if(a < b):
						yield [a,b,c]
					else:
						yield [b,a,c]
				n += 1
			m,n = m+1, 1

	def getPrimPythagoreanTriplets(x):
		m,n = 2,1
		triplets = []

		while(len(triplets) < x):
			while(m > n):
				if(getGCD([m,n]) == 1 and (m-n & 1) == 1):
					a = 2*m*n
					b = m**2 - n**2
					c = m**2 + n**2
					if(a < b):
						triplets.append([a,b,c])
						print a,b,c
					else:
						triplets.append([b,a,c])
						print b,a,c
				n += 1
			m,n = m+1, 1

		print len(triplets)
		return triplets

	def isPythTriplet(numList):
		if(math.hypot(numList[0],numList[1]) == (numList[2])):
			return True
		else: return False

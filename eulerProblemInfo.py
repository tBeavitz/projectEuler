#############################################################################################
#		Project Euler Problem Info - Python3
#
#		This Class contains the Problem text constructor and the Standard Parameters
#		for Project Euler Problems that have been completed.
#
#		Requires these files in program root:
#			problems.txt	- Contains Problem Numbers and Text
#			euler8.txt		- Contains Problem 8 1000-digit number
#			euler11.txt 	- Contains Problem 11 Grid
#			euler18.txt 	- Contains Problem 18 Grid
######################################################################################
class eulerProblemInfo(object):
	
	#Tracks problems solved and used to configure eulerParams size
	problemsSolved = -1

	#This List contains the Project Euler Problem Text
	problemText = []

	#Files for Odd/Large Parameters in program root
	files = {'problems':'problems.txt' , 'euler8':'euler8.txt' , 'euler11':'euler11.txt' , 'euler13':'euler13.txt' , 'euler18':'euler18.txt', 'euler22':'euler22.txt'}

	#This holds the Standard Parameters for Project Euler Problems
	#Index of eulerParams corresponds to the problem number
	eulerParams = []
	

	def __init__(self):
		self.buildProblemText(self.files['problems'])
		self.buildParams(self.problemsSolved)

	#This was used to build the file that holds the problem numbers and text
	def writeProblemFile(targetName):
		target = open(targetName, 'w')
		problemNum = 1
		target.write("#This File contains Project Euler Problem text\n\n\n")

		while(problemNum - 1 < info.problemsSolved):
			target.write("#This Is Project Euler Problem #{0}\n".format(problemNum))
			target.write(str(problemNum).zfill(5))
			target.write('\n')
			target.write(info.problemText[problemNum])
			target.write('\n\n\n')
			problemNum += 1
		
	#Parse the problems.txt file for ease of printing when displaying reuslts
	def buildProblemText(self, fileName):
		f = open(fileName)
		self.problemText.append(None)
		for line in f:
			if(line[0] == '#'):
				continue
			elif(line[0:4].isdigit()):
				self.problemsSolved = int(line)
			elif(line[0] == '%'):
				self.problemText.append(line[1:-1])

	#Builds the parameter array for ease of injection into functions
	#Some paramters require odd formats and have there own build functions called at the end of this function
	def buildParams(self, numSolved):
		self.eulerParams = [None,]*(numSolved+1)
		self.eulerParams[0] = None #Spacer used for convenience
		self.eulerParams[1] = 1000
		self.eulerParams[2] = 4000000
		self.eulerParams[3] = 600851475143
		self.eulerParams[4] = 999
		self.eulerParams[5] = range(20, 0, -1)
		self.eulerParams[6] = range(1, 100+1)
		self.eulerParams[7] = 10001
		self.eulerParams[8] = {'series': None,'count':13}
		self.eulerParams[9] = 1000
		self.eulerParams[10] = 2000000
		self.eulerParams[11] = {'grid':[],'count':4}
		self.eulerParams[12] = 500
		self.eulerParams[13] = {'numbers':[] , 'digits':10}
		self.eulerParams[14] = 1000000
		self.eulerParams[15] = {'width': 20, 'height':20}
		self.eulerParams[16] = 2**1000
		self.eulerParams[17] = range(1,1000+1)
		self.eulerParams[19] = "Calender + Math = ugly"
		self.eulerParams[20] = 100
		self.eulerParams[21] = 10000
		self.eulerParams[22] = 'euler22.txt'
		self.eulerParams[23] = 28123
		self.eulerParams[24] = {'charList': [0,1,2,3,4,5,6,7,8,9], "permNum" : 1000000}
		self.eulerParams[25] = 1000

		self.buildEuler8Param(self.files['euler8'])
		self.buildEuler11Param(self.files['euler11'])
		self.buildEuler13Param(self.files['euler13'])
		self.buildEuler18Param(self.files['euler18'])

	def buildEuler8Param(self, fileName):
		f = open(fileName)
		self.eulerParams[8]['series'] = int(f.readline())
		f.close()

	def buildEuler11Param(self, fileName):

		self.eulerParams[11]['grid'] = self.buildEulerGrid(fileName)

	def buildEulerGrid(self, fileName):
		f = open(fileName)
		grid = []
		for line in f:
			row = []
			while(len(line) > 1):
				part = line.partition(' ')
				row.append(int(part[0]))
				line = part[2]
			grid.append(row)
		f.close()
		return grid

	def buildEuler13Param(self, fileName):
		f = open(fileName)
		for line in f:
			self.eulerParams[13]['numbers'].append(int(line))

	def buildEuler18Param(self, fileName):
		f = open(fileName)
		grid = []
		for line in f:
			grid.append([int(s) for s in line.split() if s.isdigit()])
		
		self.eulerParams[18] = grid
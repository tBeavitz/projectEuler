########################################################################
 #								Euler Core
 #	This is the core engine which controls the execution of Problems,
 #	statistical functions, database interactions, html/css formatter,
 #	
 #
 #
 ########################################################################
from mongoengine import *
from bs4 import BeautifulSoup
import requests
from eulerProb import eulerProb
import inspect
import eulerAlg
import time

class eulerCore():
	
	db = 'probDB'
	dbHost = '192.168.1.18'

	print("EulerCore has Initialized")

	def __init__(self):
 		#TODO: Initialization here
		register_connection(self.db, name=None, host=self.dbHost)
		connect(self.db)

### Introspection

	def getSourceCode(self, func):

		return inspect.getsource(func)

	def getProblemFunction(self, name):

		return getattr(self, name)

### Problem Database Handling

	def getProblemTitle(cls, problemPage):
		#Retrives the Problem Title which is located within the only <h2> tag on the page
		return problemPage.find('h2').string

	def getProblemText(cls, problemPage):
		#Gets the Problem Text from the page
		# TODO This can't handle the odd text formatting within some of the problems

		pText = []
		problemHTML = problemPage.find("div", class_ = "problem_content")
		test = problemHTML.find_all("p")
		for line in test:
			pText.append(line.string)
		
		return pText

	def formatProblemText(cls, problemTextA):
		pText = ''
		for line in problemTextA:
			if(line != None):
				pText += str(line) + "\n"
		pText = pText.encode(encoding=sys.stdout.encoding, errors='replace')
		return pText


	
	def executeProblem(cls, num):
		# TODO This whole function
		return None

	def getProbDoc(cls, pNum):

		return eulerProb.objects.get(num = pNum)

	def isProbInDB(cls, pNum):
		if(len(eulerProb.objects(num = pNum)) == 0):
			return False
		else: return True

	def buildProblem(cls, pNum):
		if(not cls.isProbInDB(pNum)):
			problem = eulerProb(num = pNum)
			problem.buildURL()
			pageRequest = requests.get(problem.url)
			probPage = BeautifulSoup(pageRequest.content, 'html.parser')
			problem.title = cls.getProblemTitle(probPage)
			problem.text = cls.formatProblemText(cls.getProblemText(probPage))
			problem.save()
			print("Problem %d has been added to the DB!" %pNum)
		else: print("Problem %d is already in the DB!" %pNum)

core = eulerCore()

for x in range(1,556):
	core.buildProblem(x)

for prob in eulerProb.objects():
	print("%d - %s\n-)%s"%(prob.num,prob.title,prob.text.encode(encoding='UTF-8', errors='replace')))
import sys
print(sys.version)
print(sys.stdout.encoding)
###################################################################

# class eulerStat:
# 	###########################################################################
# 	#	
# 	#	Tracks execution time, processor usage and memory usage, added to database when complete
# 	#
# 	#
# 	###########################################################################

# class eulerOut:
# 	###########################################################################
# 	#
# 	#	Formats data into html/css for viewing
# 	#
# 	#
# 	#
# 	###########################################################################

# class eulerDB:
# 	###########################################################################
# 	#	
# 	#	Uses the standard python sqlite3 serverless
# 	#	database, can retrieve/store info for each function(time,
# 	#	algorithm history, usage) individual run(functions used, run stats) 
# 	#
# 	#
# 	###########################################################################




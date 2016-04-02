#Used to create Project Euler Problem text file
from eulerProblemInfo import eulerProblemInfo

targetName = 'problems.txt'
info = eulerProblemInfo()

def writeProblemFile():
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

writeProblemFile()


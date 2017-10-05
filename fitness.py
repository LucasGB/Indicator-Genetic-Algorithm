
class Solution(object):
	def __init__(self, solution):
		self.solution = solution

	def getSolution(self):
		return self.solution

def setSolution(solution):
	global __solution__
	__solution__ = Solution(solution)

def calculateFitness(individual):
	fitness = 0
	s = __solution__.getSolution()
	for i in range(individual.size()):
		if(i > len(s)):
			break
		elif(individual.getGene(i) == s[i]):
			fitness += 1
	return fitness

def getMaxFitness():
	return len(solution)
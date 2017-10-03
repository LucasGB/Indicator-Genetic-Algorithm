solution = ""

def calculateFitness(individual):
	fitness = 0
	for i in range(individual.size()):
		if(i > len(solution)):
			break
		elif(individual.getGene[i] == solution[i]):
			fitness += 1
	return fitness

def getMaxFitness():
	return len(solution)

def setSolution(solution):
	solution = solution
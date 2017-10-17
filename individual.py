from random import randint

class Individual(object):
	def __init__(self):
		self.defaultGenomeLength = 64
		self.genome = ""
		self.fitness = 0

	def generateIndividual(self):
		self.genome = ''.join(str(randint(0,1)) for i in range(self.defaultGenomeLength))

	def generateIndividual(self, parent1, parent2):
		self.genome = parent1.getGenome()[start:end] + parent2.getGenome()[end:start]

	def setDefaultGenomeLength(self, lengh):
		self.defaultGenomeLength = lengh

	def getGene(self, index):
		return self.genome[index]

	def getGenome(self):
		return self.genome

	def setGene(self, index, value):
		self.genome[index] = value
		self.fitness = 0

#	def getFitness(self):
#		if(self.fitness == 0):
#			self.fitness = getFitness(self)
#		return self.fitness

	def setFitness(self, fitness):
		self.fitness = fitness

	def getFitness(self):
		return self.fitness

	def printIndividual(self):
		print self.genome

	def size(self):
		return len(self.genome)
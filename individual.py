#from fitness import getFitness
from random import randint

class Individual(object):
	def __init__(self):
		self.defaultGenomeLength = 64
		self.genome = ""
		self.fitness = 0

	def generateIndividual(self):
		self.genome = ''.join(str(randint(0,1)) for i in range(self.defaultGenomeLength))

	def setDefaultGenomeLength(self, lengh):
		self.defaultGenomeLength = lengh

	def getGene(self, index):
		return genome[index]

	def setGene(self, index, value):
		self.genome[index] = value
		self.fitness = 0

	def getFitness(self):
		if(fitness == 0):
			fitness = getFitness(self)
		return fitness

	def printIndividual(self):
		print self.genome

	def size():
		return len(self.genome)
from individual import Individual

'''
Creates a population of individuals based by the specified size. 
'''
class Population(object):
	def __init__(self, populationSize):
		self.individuals = []

		for i in range(populationSize):
			i = Individual()
			i.generateIndividual()
			self.individuals.append(i)

	def getPopulation(self):
		return self.individuals
		
	def getIndividual(self, index):
		return self.individuals[index]

	def getFittest(self):
		fittest = self.individuals[0]

		for i in range(1, self.size()):
			if(fittest.getFitness() <= self.getIndividual(i).getFitness()):
				fittest = self.getIndividual(i)

		return fittest

	def printPopulation(self):
		[individual.printIndividual() for individual in self.individuals]

	def size(self):
		return len(self.individuals)
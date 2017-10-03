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

	def getIndividual(index):
		return self.individuals[index]

	def getFittest():
		fittest = self.individuals[0]

		for i in range(self.size()):
			if(fittest.getFittest() <= getIndividual[i].getFittest()):
				fittest = getIndividual[i]

		return fittest

	def printPopulation(self):
		[individual.printIndividual() for individual in self.individuals]

	def size(self):
		return len(self.individuals)
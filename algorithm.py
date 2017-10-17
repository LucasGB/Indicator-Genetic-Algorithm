from population import Population
from fitness import calculateFitness, setSolution
from random import *

class Algorithm(object):
	def __init__(self):
		self.uniformRate = 0.5
		self.mutationRate = 0.015
		self.tournamentSize = 5
		self.elitism = True

		self.population = []

	"""
	Returns the individual by chance of probability. The higher the fitness score, the more likely the individual will be chosen to procreate.
	r: random generated number.
	l: list containing the fitness score for each individual.
	"""
	def getParentIndex(self, r, l):
		l = [abs(r - p) for p in l]
		index = l.index(min(l))
		return self.population.getIndividual(index), index

	"""
	Iterates over the population and calculates the fitness score for each individual
	"""
	def evaluatePopulation(self):
		for individual in self.population.getPopulation():
			individual.setFitness(calculateFitness(individual))

	"""
	Selects two parents to generate an offspring.
	"""
	def select(self):
		select_probability = [individual.getFitness() for individual in self.population.getPopulation()]

		parent1, index1 = self.getParentIndex(random()*100, select_probability)
		parent2, index2 = self.getParentIndex(random()*100, select_probability[:index1] + select_probability[(index1+1):])

		print 'Parent 1:', parent1.printIndividual()
		print 'Parent 2:', parent2.printIndividual()

		return parent1, parent2

	def crossover(self, parent1, parent2):
		child1 = 

	def run(self):
		setSolution("1111111111111111111111111111111111111111111111111111111111111111")
		self.population = Population(5)
		self.population.printPopulation()

		self.evaluatePopulation()
		parent1, parent2 = self.select()
		self.crossover(parent1, parent2)
		self.population.printPopulation()

		

		

if __name__ == '__main__':
	ga = Algorithm()
	ga.run()
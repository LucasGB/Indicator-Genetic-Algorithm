from population import Population
from fitness import calculateFitness, setSolution

class Algorithm(object):
	def __init__(self):
		self.uniformRate = 0.5
		self.mutationRate = 0.015
		self.tournamentSize = 5
		self.elitism = True

		self.population = []

	"""
	Returns the individual by index
	"""
	def getParentIndex(self, r, l):
		l = [abs(r - p) for p in l]
		return self.population.getIndividual(l.index(min(l)))

	def evaluatePopulation(self):
		for individual in self.population.getPopulation():
			individual.setFitness(calculateFitness(individual))

	def select(self):
		select_probability = [individual.getFitness() for individual in population]

		parent1 = getParentIndex(random(), select_probability)
		parent2 = getParentIndex(random(), select_probability)

		print parent1
		print parent2

	#def crossover():

	def run(self):
		setSolution("1111111111111111111111111111111111111111111111111111111111111111")
		self.population = Population(5)
		self.evaluatePopulation()
		self.population.printPopulation()

		

		

if __name__ == '__main__':
	ga = Algorithm()
	ga.run()
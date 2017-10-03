from population import Population
from fitness import setFitness, calculateFitness

class Algorithm(object):
	def __init__(self):
		self.uniformRate = 0.5
		self.mutationRate = 0.015
		self.tournamentSize = 5
		self.elitism = True

	def getParentIndex(self, r, l):
		l = [abs(r - p) for p in l]
		return l.index(min(l))

	def evaluatePopulation():
		for individual in population:
			individual.setFitness(calculateFitness(individual))

	def select():
		select_probability = [individual.getFitness() for individual in population]

		parent1 = getParentIndex(random(), select_probability)
		parent2 = getParentIndex(random(), select_probability)

	#def crossover():

	def run():
		

		

if __name__ == '__main__':
	run()
from individual import Individual
from population import Population
from fitness import Fitness
from algorithm import Algorithm
from random import *


a = [1, 2, 3]
b = [0.5, 0.2, 0.3]

def getParent(r, d):
	d = [abs(r - e) for e in b]
	print d
	print r
	return d.index(min(d))

if __name__ == '__main__':
#fitness = Fitness()
#fitness.setSolution("1111000000000000000000000000000000000000000000000000000000001111")#
#

#p = Population(50)
#genCount = 0
#while(population.getFittest().getFitness < fitness.getMaxFitness()):
#	genCount += 1
#	print "Generation: %d  Fitness: %d" % (genCount, population.getFittest.getFitness())
#	population = algorithm.evolve(population)#

#print "Solution found!"
#print "Generation: ", genCount
#print "Genes: ", population.getFittest()

	#p = Population(5)
	#p.printPopulation()

	a = [1, 2, 3]
	b = [0.5, 0.2, 0.3]
	
	
	print getParent(random(), b)
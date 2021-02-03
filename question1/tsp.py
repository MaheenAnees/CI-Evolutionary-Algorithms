import numpy as np
import random

class TSP(GA):

    def createChromosome(self):
        order = set(np.arrange(self.dimension, dtype=int))
        route = list(random.sample(order, self.dimension))
        return route
    
    def findDist(node1, node2):
        return np.sqrt((node1[0]-node2[0])**2 + (node1[1]-node2[1])**2)

    def calcFitness(chromosome):
        fitness = 0
        for i in range(1, len(chromosome)):
            node1 = chromosome[i-1]
            node2 = chromosome[i]
            fitness = fitness + findDist(node1, node2)
        return fitness

    

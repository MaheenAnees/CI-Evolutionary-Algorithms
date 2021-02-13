import numpy as np
import random
from geneticAlgo import *

class TSP(GA):
    def __init__(self, data, populationSize, children, mutationRate, iterations, dimension, totalGenerations):
        self.data = data
        self.populationSize = populationSize
        self.children = children
        self.mutationRate = mutationRate
        self.iterations = iterations
        self.dimension = dimension
        self.totalGenerations = totalGenerations
        self.max = math.inf
        self.population = self.initializePopulation()
         
    def initializePopulation(self):
        population = []
        for i in range(self.populationSize):
            individual = []
            while(len(individual) < self.dimension):
                node = random.randint(0 , self.dimension - 1)
                if self.data[node] not in individual:
                    individual.append(self.data[node])
            population.append(individual)
        return population
    

    def findDistance(self, node1, node2):
        return np.sqrt((node1[1]-node2[1])**2 + (node1[2]-node2[2])**2)
  
    def calcFitness(self, chromosome):       
        fitness = 0
        for i in range(1, len(chromosome)):
            node1 = chromosome[i-1]
            node2 = chromosome[i]
            fitness = fitness + self.findDistance(node1, node2)
        return (1/fitness , -1)




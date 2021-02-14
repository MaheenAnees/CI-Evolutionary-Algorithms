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
        self.population = self.initializePopulation()
         
    def initializePopulation(self):
        population = []
        for i in range(self.populationSize):
            population.append(self.createChromosome())
        return population
    
    def createChromosome(self):
        order = set(np.arange(self.dimension, dtype=int))
        individual = list(random.sample(order, self.dimension))    
        return individual

    def findDistance(self, node1, node2):
        return np.sqrt((node1[1]-node2[1])**2 + (node1[2]-node2[2])**2)
  
    def calcFitness(self, chromosome):       
        fitness = 0
        for i in range(1, len(chromosome)):
            node1 = chromosome[i-1]
            node2 = chromosome[i]
            fitness = fitness + self.findDistance(self.data[node1], self.data[node2])
        return 1/fitness
    
    def print(self):
        print("Distance: " + str(1/self.rankRoutes()[0][1]))
    
    def returnFitness(self):
        return 1/self.rankRoutes()[0][1]




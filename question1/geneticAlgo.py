import numpy as np
import random

class GA:
    def _init_(self):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.iterations = iterations
        self.dimension = dimension 
        self.totalGenerations = totalGenerations

    def initializePopultaion(self):
        population = []
        for i in range(0, self.populationSize):
            population.append(self.createChromosome(self.dimension))
        return population

    def createChromosome(self): #problem specific
        pass

    def calcFitness(self, chromosome): #problem specific
        pass
    
    def mutate(self):
        pass

    def crossOver(self):
        pass

    def selection(self, selectType, population):
        if selectType == 'RB':
            parent = self.RBS(self, population)
        if selectType == 'FP':
            parent = self.FPS(self, population)
        if selectType == 'truncate':
            parent = self.truncate(self, population)
        if selectType == 'BT':
            parent = self.binaryTournament(self, population)

    def binaryTournament(self):
        individual1 = np.random.randint(0, self.dimension) #randomly select the first chromosome
        individual2 = np.random.randint(0, self.dimension) #randomly select the second chromosome
        fitness1 = self.calcFitness(individual1) #calculate fitness for the first chromosome
        fitness2 = self.calcFitness(individual2) #calculate fitness for the second chromosome
        return max(fitness1, fitness2) #return the fittest chromosome 

    def truncate(self, population, n):
        pass

    def FPS(self, population):
        pass

    def RBS(self, population):
        pass








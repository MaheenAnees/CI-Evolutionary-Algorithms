from geneticAlgo import *

class Knapsack(GA):
    def __init__(self, data, populationSize, children, mutationRate, iterations, totalGenerations):
        self.data = data
        self.populationSize = populationSize
        self.children = children
        self.mutationRate = mutationRate
        self.iterations = iterations
        self.totalGenerations = totalGenerations
        self.dimension = self.data["Info"][0]
        self.weightCapacity = self.data["Info"][1]
        self.population = self.initializePopulation()

    def initializePopulation(self):
        population = []
        for i in range(self.populationSize):
            population.append(self.createChromosome())
        return population
    
    def createChromosome(self):
        individual = []
        for i in range(self.dimension):
            individual.append(random.choice([0,1]))
        return individual

    def calcFitness(self, chromosome):
        totalWeight = 0
        totalProfit = 0
        for i in range(self.dimension):
            if chromosome[i]!=0:
                totalProfit += self.data[i][0]
                totalWeight += self.data[i][1]
        if totalWeight <= self.weightCapacity:
            return totalProfit
        else:
            return 0
    
    def print(self):
        print("Distance: " + str(self.rankRoutes()[0][1]))
    
    def returnFitness(self):
        return self.rankRoutes()[0][1]
        



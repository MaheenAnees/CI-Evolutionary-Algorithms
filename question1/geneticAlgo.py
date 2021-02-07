import numpy as np, random, operator

class GA:
    def _init_(self):
        self.populationSize = populationSize
        self.offsprings = offsprings
        self.mutationRate = mutationRate
        self.iterations = iterations
        self.dimension = dimension 
        self.totalGenerations = totalGenerations

    def initializePopultaion(self):
        population = []
        for i in range(0, self.populationSize):
            population.append(self.createChromosome(self, data))
        return population

    #problem specific function
    #implemented in specific problem's class
    def createChromosome(self, data):
        pass

    #problem specific function
    #implemented in specific problem's class
    def calcFitness(self, chromosome):
        pass
    
    #swap randomly selected nodes in chromosome
    def mutate(self, chromosome):
        for node in chromosome:
            if (random.random() < self.mutationRate):
                node2 = np.random.randint(0, self.dimension)
                temp1 = chromosome[node]
                temp2 = chromosome[node2]
                chromosome[node] = temp2
                chromosome[node2] = temp1
        return chromosome


    def crossOver(self, parents):
        pass

    def selection(self, selectType, population, n):
        pass

    def binaryTournament(self, population):
        individual1 = population[np.random.randint(0, self.dimension)] #randomly select the first chromosome
        individual2 = population[np.random.randint(0, self.dimension)] #randomly select the second chromosome
        fitness1 = self.calcFitness(individual1) #calculate fitness for the first chromosome
        fitness2 = self.calcFitness(individual2) #calculate fitness for the second chromosome
        if (fitness1 > fitness2): #return the fittest individual
            return individual1
        else:
            return individual2

    def truncate(self, population, n): #returns top n fittest chromosomes 
        fitnessResult = {}
        for i in range(len(population)):
            #calculate fitness for all the chromosomes
            fitnessResult[i] = self.calcFitness(population[i])
        #sort in descending order based on fitness
        sortedFitness = sorted(fitnessResult.items(), key = operator.itemgetter(1))
        finalResult = []
        for i in range(n):
            #select top n fittest chromosomes
            finalResult.append(population[sortedFitness[i][0]]) 
        return finalResult

    def FPS(self, population):
        fitnessResult = {}
        for i in range(len(population)):
            #calculate fitness for all the chromosomes
            fitnessResult[i] = self.calcFitness(population[i])
        fitnessSum = sum(fitnessResult.values())
        #divide each fitness value by the sum
        for i in range(len(population)):
            fitnessResult[i] = fitnessResult[i] / fitnessSum
        #find the cumulative fitness for each
        for i in range(1,len(population)):
            fitnessResult[i] += fitnessResult[i-1] 
        #find the cumulative fitness closest to the generated random number
        result = min(fitnessResult.values(), key=lambda x:abs(random.random()))
        #find the chromosome index with the closest value that we found
        for key,value in fitnessResult.items():
            if value == result:
                index=key
                break
        return population[index]

    def RBS(self, population):
        fitnessResult = {}
        for i in range(len(population)):
            #calculate fitness for all the chromosomes
            fitnessResult[i] = self.calcFitness(population[i])
        #sort in ascending order based on fitness so that highest index(rank) is of the fittest indivual
        #each tuple => first val = index of chromosome in pop , second val = fitness
        sortedFitness = sorted(fitnessResult.items(), key = operator.itemgetter(1), reverse = False)
        rankedResult = []
        for i in range(len(sortedFitness)):
            #divide each fitness by its rank
            rankedFitness = sortedFitness[i][1]/i
            rankedResult.append((sortedFitness[0],rankedFitness))
        

    def random(self, population):
        #randomly select the chromosome
        return population[np.random.randint(0, self.dimension)]

    #will run steps for each generation
    def evolve(self):
        pass

    #will run total generations
    def geneticAlgorithm(self):
        pass








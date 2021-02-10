import numpy as np, random, operator

class GA:
    def _init_(self):
        self.data = data
        self.populationSize = populationSize
        self.children = children
        self.mutationRate = mutationRate
        self.iterations = iterations
        self.dimension = dimension 
        self.totalGenerations = totalGenerations

    def initializePopultaion(self):
        population = []
        for i in range(0, self.populationSize):
            population.append(self.createChromosome())
        return population

    #problem specific function
    #implemented in specific problem's class
    def createChromosome(self):
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
        child=[]
        childA=[]
        childB=[]   
        geneA=int(random.random()* len(parents[0]))
        geneB=int(random.random()* len(parents[0]))
        
        start = min(geneA,geneB)
        end = max(geneA,geneB)
        for i in range(start,end):
            childA.append(parents[0][i])    
        childB=[gene for gene in parents[1] if gene not in childA]
        child = childA + childB
        return child

    
    def selection(self, selectType, population, n):
        """
            n = number of individuals to be selected
            selectType = the name of selection scheme to be applied
        """
        selected = []
        if (selectType == 'BT'):
            for i in range(n):
                selected.append(self.binaryTournament(self, population))
        if (selectType == 'rand'):
            for i in range(n):
                selected.append(self.random(self, population))
        if (selectType == 'truncate'):
            selected.append(self.truncate(self, population, n))
        if (selectType == 'FPS'):
            selected.append(self.FPS(self, population, n))
        if (selectType == 'RBS'):
            selected.append(self.RBS(self, population, n))
        return selected


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

    def FPS(self, population, n):
        fitnessResult = {}
        selected = []
        for i in range(len(population)):
            #calculate fitness for all the chromosomes
            fitnessResult[i] = self.calcFitness(population[i])
        fitnessSum = sum(fitnessResult.values())
        #divide each fitness value by the sum
        for i in range(len(population)):
            j = i - 1
            fitnessResult[i] = fitnessResult[i] / fitnessSum
            if (j >= 0):
                #find the cumulative fitness for each
                fitnessResult[i] += fitnessResult[j] 
        for i in range(n):
            #find the cumulative fitness closest to the generated random number
            result = min(fitnessResult.values(), key=lambda x:abs(random.random()))
            #find the chromosome index with the closest value that we found
            for key,value in fitnessResult.items():
                if value == result:
                    index=key
                    break
            selected.append(population[index])
        return selected

    def RBS(self, population, n):
        fitnessResult = {}
        selected = []
        for i in range(len(population)):
            #calculate fitness for all the chromosomes
            fitnessResult[i] = self.calcFitness(population[i])
        #sort in ascending order based on fitness
        sortedFitness = sorted(fitnessResult, key = fitnessResult.get) #returns the sorted list of index
        rankSum = sum(range(self.populationSize + 1))
        for i in range(len(sortedFitness)):
            j = i - 1
            #divide each fitness by rankSum
            rankedFitness = (i+1)/rankSum
            fitnessResult[sortedFitness[i]] = rankedFitness
            #find the cumulative fitness for each
            if (j >=0):
                fitnessResult[sortedFitness[i]] += fitnessResult[sortedFitness[j]] 
        for i in range(n):
            #find the cumulative fitness closest to the generated random number
            result = min(fitnessResult.values(), key=lambda x:abs(random.random()))
            #find the chromosome index with the closest value that we found
            for key,value in fitnessResult.items():
                if value == result:
                    index=key
                    break
            selected.append(population[index])
        return selected
            

    def random(self, population):
        #randomly select the chromosome
        return population[np.random.randint(0, self.dimension)]

    #will run steps for each generation
    def evolve(self):
        pass

    #will run total generations
    def geneticAlgorithm(self):
        for i in range(self.totalGenerations):
            self.evolve()








import numpy as np, random, operator, math
# import pandas as pd
import matplotlib.pyplot as plt

class GA:
    def __init__(self): #problem specific
        pass

    def calcFitness(self, chromosome): #problem specific
        pass

    def binaryTournament(self):
        individual1 = self.population[np.random.randint(0, len(self.population))] #select the first random individual
        individual2 = self.population[np.random.randint(0, len(self.population))] #select the second random individual
        fitness1 = self.calcFitness(individual1) #calculate fitness for individual1
        fitness2 = self.calcFitness(individual2) #calculate fitness for individual2
        if (fitness1 >= fitness2):  #return the fittest individual
            return individual1
        else:
            return individual2

    def FPS(self, n):
        """
            n = number of individuals to be selected
        """
        fitnessResult = {}
        selected = []
        for i in range(len(self.population)):
            #calculate fitness for all the chromosomes
            fitnessResult[i] = self.calcFitness(self.population[i])
        fitnessSum = sum(fitnessResult.values())
        #divide each fitness value by the sum
        for i in range(len(self.population)):
            j = i - 1
            fitnessResult[i] = fitnessResult[i] / fitnessSum
            if (j >= 0):
                #find the cumulative fitness for each
                fitnessResult[i] += fitnessResult[j] 
        for i in range(n):
            #find the cumulative fitness closest to the generated random number
            lst = np.asarray(list(fitnessResult.values())) 
            idx = (np.abs(lst - random.random())).argmin() 
            result = lst[idx]
            #find the chromosome index with the closest value that we found
            for key,value in fitnessResult.items():
                if value == result:
                    index=key
                    break
            selected.append(self.population[index])
        return selected

    def RBS(self, n):
        """
            n = number of individuals to be selected
        """
        fitnessResult = {}
        selected = []
        for i in range(len(self.population)):
            #calculate fitness for all the chromosomes
            fitnessResult[i] = self.calcFitness(self.population[i])
        #sort in ascending order based on fitness
        sortedFitness = sorted(fitnessResult, key = fitnessResult.get) #returns the sorted list of index
        rankSum = sum(range(self.populationSize + 1))
        for i in range(len(sortedFitness)):
            j = i - 1
            #divide each rank by rankSum
            rankedFitness = (i+1)/rankSum
            fitnessResult[sortedFitness[i]] = rankedFitness
            #find the cumulative fitness for each
            if (j >=0):
                fitnessResult[sortedFitness[i]] += fitnessResult[sortedFitness[j]] 
        for i in range(n):
            #find the cumulative fitness closest to the generated random number
            lst = np.asarray(list(fitnessResult.values())) 
            idx = (np.abs(lst - random.random())).argmin() 
            result = lst[idx]
            #find the chromosome index with the closest value that we found
            for key,value in fitnessResult.items():
                if value == result:
                    index=key
                    break
            selected.append(self.population[index])
        return selected

    def truncate(self, n): #returns top n fittest chromosomes 
        fitnessResult = {}
        for i in range(len(self.population)):
            #calculate fitness for all the chromosomes
            fitnessResult[i] = self.calcFitness(self.population[i])
        #sort in descending order based on fitness
        sortedFitness = sorted(fitnessResult.items(), key = operator.itemgetter(1), reverse= True)
        finalResult = []
        for i in range(n):
            #select top n fittest chromosomes
            finalResult.append(self.population[sortedFitness[i][0]]) 
        return finalResult

    def random(self):
        #randomly select the chromosome
        return self.population[np.random.randint(0, len(self.population))]

    def select(self, selectType, n):
        """
            selectType = name of the selection scheme
            n = number of individuals to be selected
        """
        selected = []
        if (selectType == 'BT'):
            for i in range(n):
                selected.append(self.binaryTournament())
        if (selectType == 'trunc'):
            return self.truncate(n)
        if (selectType == 'random'):
            for i in range(n):
                selected.append(self.random())
        if (selectType == 'FPS'):
            return self.FPS(n)    
        if (selectType == 'RBS'):
            return self.RBS(n)
        return selected
    
    def crossOver(self, parents):
        child1 = parents[0].copy()
        child2 = parents[1].copy()    
        geneA=int(random.random()* len(parents[0]))
        geneB=int(random.random()* len(parents[0]))       
        start = min(geneA,geneB)
        end = max(geneA,geneB)
        tmp = child1[start:end]
        child1[start:end] = child2[start:end]
        child2[start:end] = tmp
        return [child1, child2]

    def mutate(self, individual):
        node1 = np.random.randint(0, self.dimension)  #select the first random node in the chromosome
        node2 = np.random.randint(0, self.dimension)  #select the second random node in the chromosome
        temp1 = individual[node1]                     # S
        temp2 = individual[node2]                     # W
        individual[node1] = temp2                     # A
        individual[node2] = temp1                     # P
        return individual
    
    def mutatePopulation(self, children):
        for i in range(len(children)):
            if(random.random() <= self.mutationRate):
                children[i] = self.mutate(children[i])
        return children
    
    def nextGeneration(self): 
        children = []      
        for i in range(self.children//2):
            parents = self.select("BT", 2)
            children = self.crossOver(parents)
            children = self.mutatePopulation(children)
            self.population += children    
        self.population = self.select("trunc", self.populationSize)
    
    def rankRoutes(self):
        routeRank = {}
        for i in range(len(self.population)):
            routeRank[i] = self.calcFitness(self.population[i])     
        return sorted(routeRank.items(), key = operator.itemgetter(1), reverse=True)
    
    
    def geneticAlgorithm(self):
        self.print()  
        progress = []
        progress.append(self.returnFitness())
        for i in range(0, self.totalGenerations):
            print("Generation:", i)
            self.nextGeneration()
            progress.append(self.returnFitness())
            
        self.print() 
        bestRouteIds = self.rankRoutes()[0][0]
        # plt.plot(progress)
        # plt.ylabel('Distance')
        # plt.xlabel('Generation')
        # plt.show()
        return self.population[bestRouteIds]


# obj.plotFitness()
# for i in range(10):
#   obj.evolve()
#   fitnessSoFar.append(obj.getBFS())

# df = pd.DataFrame(fitnessSoFar)
# sns.heatmap(df)
# plt.show()
# df = df.transpose()
# df[len(fitnessSoFar)] = sum(df[:])

# print(df)            








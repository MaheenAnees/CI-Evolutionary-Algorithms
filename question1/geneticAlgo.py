#     #swap randomly selected nodes in chromosome
#     # def mutate(self, chromosome):
#     #     for node in chromosome:
#     #         if (random.random() <= self.mutationRate):
#     #             node2 = np.random.randint(0, self.dimension)
#     #             temp1 = chromosome[node]
#     #             temp2 = chromosome[node2]
#     #             chromosome[node] = temp2
#     #             chromosome[node2] = temp1
#     #     return chromosome


#     # def crossOver(self, parents):
#     #     child=[]
#     #     childA=[]
#     #     childB=[]   
#     #     geneA=int(random.random()* len(parents[0]))
#     #     geneB=int(random.random()* len(parents[0]))
        
#     #     start = min(geneA,geneB)
#     #     end = max(geneA,geneB)
#     #     for i in range(start,end):
#     #         childA.append(parents[0][i])    
#     #     childB=[gene for gene in parents[1] if gene not in childA]
#     #     child = childA + childB
#     #     return child

#     """
#     #will run steps for each generation
#     def newGeneration(self):
#         offsprings = []
#         mutatedPop = []
#         for i in range(self.iterations):
#             parents = self.selection('BT', 2)
#             offsprings.append(self.crossOver(parents))
#         for i in offsprings:
#             mutatedPop.append(self.mutate(i))
#         self.population += mutatedPop
#         survivors = self.selection('truncate', self.populationSize)
#         # print("Offsprings:", offsprings)
#         # print("mutated:", mutatedPop)
#         # print("newPop", self.population[0])
#         print("Survive", len(survivors))
#         return survivors

#     #will run total generations
#     def evolve(self):
#         # Initial = {}
#         # for i in range(len(self.population)):
#         #     #calculate fitness for all the chromosomes
#         #     Initial[i] = self.calcFitness(self.population[i])
#         # sortedIni = sorted(Initial.items(), key = operator.itemgetter(1), reverse=True)
#         # ini = 1/sortedIni[0][1]
#         # print("Initial", ini)

#         for i in range(self.totalGenerations):
#             print("Generation number:", i)
#             self.population = self.newGeneration()
#             # print(self.population)
#             fitnessResult = {}
#             for i in range(len(self.population)):
#             #calculate fitness for all the chromosomes
#                 fitnessResult[i] = self.calcFitness(self.population[i])
#             sortedFitness = sorted(fitnessResult.items(), key = operator.itemgetter(1), reverse=True)
#             fittest = 1/sortedFitness[0][1]
#             print("fitness", fittest)
            
#             # print(self.population)
#             # print(len(self.population))
#         # fitnessResult = {}
#         # for i in range(len(self.population)):
#         #     #calculate fitness for all the chromosomes
#         #     fitnessResult[i] = self.calcFitness(self.population[i])
#         # sortedFitness = sorted(fitnessResult.items(), key = operator.itemgetter(1), reverse=True)
#         # fittest = 1/sortedFitness[0][1]
#         # print("fitness", fittest)
#         """

import numpy as np, random, operator, math
# import pandas as pd
import matplotlib.pyplot as plt

class GA:
    def __init__(self): #problem specific
        pass

    def calcFitness(self, chromosome): #problem specific
        pass

    @staticmethod
    def takefitness(elem):
        return elem[1]

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
        fitnessSum = sum(i for i, j in fitnessResult.values())
        #divide each fitness value by the sum
        for i in range(len(self.population)):
            j = i - 1
            fitnessResult[i] = fitnessResult[i][0] / fitnessSum
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
# """
#     def FPS(self, n):
#         sel = []
#         routeCMF = []
#         sumFitness = 0
#         # find fitness of each chromosome
#         for i in range(len(self.population)):
#             f = self.calcFitness(self.population[i])
#             routeCMF.append([self.population[i], f])
#             sumFitness += f
#         # sort by fitness proportion
#         routeCMF.sort(key=TSP.takefitness)
#         # find fitness proportion of each chromosome and find CMF
#         routeCMF[0][1] /= sumFitness
#         for i in range(1,len(self.population)):
#             routeCMF[i][1] /= sumFitness
#             routeCMF[i][1] += routeCMF[i-1][1]

#         while len(sel) != n:
#             rdm = random.random()
#             for i in range(len(self.population)):
#                 if rdm <= routeCMF[i][1]:
#                     if n == 2 or (n > 2 and routeCMF[i][0] not in sel):
#                         sel.append(routeCMF[i][0])
#         return sel

#     def RBS(self, n):
#         sel = []
#         routeFitness = []
#         sumRank = (self.dimension-1)*(self.dimension)/2
#         # find fitness of each chromosome
#         for i in range(len(self.population)):
#             f = self.calcFitness(self.population[i])
#             routeFitness.append([self.population[i], f])
#         # sort by fitness proportion
#         routeFitness.sort(key=TSP.takefitness)
#         # find fitness proportion of each chromosome and find CMF
#         routeFitness[0].append(1/sumRank)
#         for i in range(1,len(self.population)):
#             routeFitness[i].append((i+1)/sumRank)
#             routeFitness[i][2] += routeFitness[i-1][2]
#         while len(sel) != n:
#             rdm = random.random()
#             for i in range(len(self.population)):
#                 if rdm <= routeFitness[i][2]:
#                     if n == 2 or (n > 2 and routeFitness[i][0] not in sel):
#                         sel.append(routeFitness[i][0])
#                         # sel.append(routeFitness[i][0])
#                         break
#         return sel
#     """
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
            parents = self.select("RBS", 2)
            children = self.crossOver(parents)
            children = self.mutatePopulation(children)
            self.population += children    
        self.population = self.select("trunc", self.populationSize)
    
    def rankRoutes(self):
        routeRank = {}
        for i in range(len(self.population)):
            routeRank[i] = self.calcFitness(self.population[i])[0]        
        return sorted(routeRank.items(), key = operator.itemgetter(1), reverse=True)
    
    
    def geneticAlgorithm(self):
        print("Initial distance: " + str(1/self.rankRoutes()[0][1]))  
        progress = []
        progress.append(1/self.rankRoutes()[0][1])
        for i in range(0, self.totalGenerations):
            print("Generation:", i)
            self.nextGeneration()
            progress.append(1/self.rankRoutes()[0][1])
            
        print("Final distance: " + str(1/self.rankRoutes()[0][1]))
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








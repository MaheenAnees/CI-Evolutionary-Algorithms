# # class Knapsack(EA):
# #   def __init__(self, path,  childrenSize = 10, generations = 500 , mutationRate_ = 0.5, noOfIteration_ =10,  size= 20):
# #     self.nodeListKSP = self.KSChromosomes("/content/f2_l-d_kp_20_878")
# #     self.max = self.nodeListKSP["Information"][1]
# #     self.population = []
# #     self.populationSize = size
# #     self.dimension = self.nodeListKSP["Information"][0]
# #     self.noOfChildren = childrenSize
# #     self.noOfGeneration = generations
# #     self.mutationRate = mutationRate_
# #     self.noOfIteration = noOfIteration_

# #     for _ in range(self.populationSize):
# #       chromosome = []
# #       for _ in range(self.dimension):
# #         chromosome.append(random.choice([0,1]))  
# #       self.population.append(chromosome)

# #   def fitness(self, individual):
# #     weights = 0
# #     val =0
# #     for i in range(self.dimension):
# #       if individual[i]!=0:
# #         val +=1
# #         weights += self.nodeListKSP[i]

# #     return (val, weights)

# #   def crossover(self, parent1, parent2):
# #     child = [random.choice([0,1]) for _ in range(self.dimension)]
    
# #     geneA = int(random.random() * len(parent1))
# #     geneB = int(random.random() * len(parent1))
    
# #     startGene = min(geneA, geneB)
# #     endGene = max(geneA, geneB)

# #     child[startGene: endGene] = parent1[startGene:endGene]
# #     return child

#   def KSChromosomes(self, path):
#     infile = open(path, "r")
#     first = infile.readline().split()
#     itemCapacity = int(first[0])
#     weightCapacity = int(first[1])
#     chromosome ={"Information": (itemCapacity_, weightCapicity_)}
#     for _ in range(itemCapacity):
#       node = infile.readline().split()
#       chromosome[_] = int(node[1])
    
#     return chromosome

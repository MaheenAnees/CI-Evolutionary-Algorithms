class GA:
    def _init_(self):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.iterations = iterations
        self.dimension = dimension

    def initializePopultaion(self):
        population = []
        for i in range(0, self.populationSize):
            population.append(createChromosome(self.dimension))

    def createChromosome(self):
        pass

    def calcFitness(self):
        pass
    
    def mutate(self):
        pass

    def crossOver(self):
        pass

    def selection(self):
        pass








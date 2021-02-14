from geneticAlgo import *
from knapsack import *
from tsp import *

def readForTSP(path):
    # Open input file
    infile = open(path, 'r')
    # # Read instance header
    name = infile.readline().strip() # NAME
    comment1 = infile.readline().strip()
    comment2 = infile.readline().strip()
    fileType = infile.readline().strip()
    dimension = infile.readline().strip().split()[2] # DIMENSION
    edgeWeightType = infile.readline().strip().split()[1] # EDGE_WEIGHT_TYPE
    infile.readline()
    # Read node list
    nodelist = []
    n = int(dimension)
    for i in range(0, n):
        node, x,y = infile.readline().strip().split()
        nodelist.append([int(node),float(x), float(y)])

    # Close input file
    infile.close()
    return nodelist

def readForKnapsack(path):
    infile = open(path, 'r')
    totalItems, weightCapacity = infile.readline().strip().split()
    data = {"Info":(int(totalItems),int(weightCapacity))}
    for i in range(int(totalItems)):
        node = infile.readline().strip().split()
        data[i] = (int(node[0]), int(node[1]))
    infile.close()
    return data





# data = readForTSP('question1\qa194.tsp')
# obj = TSP(data, 30, 10, 0.5, 10, 194, 1000)
# obj.geneticAlgorithm()

data = readForKnapsack('question1\\f2_l-d_kp_20_878')
obj = Knapsack(data, 30, 10, 0.5, 10, 100)
obj.geneticAlgorithm()

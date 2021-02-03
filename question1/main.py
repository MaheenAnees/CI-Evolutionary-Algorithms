from geneticAlgo import *
from knapsack import *
from tsp import *


# Open input file
infile = open('qa194.tsp', 'r')
# print(infile.read())

# # Read instance header
name = infile.readline().strip() # NAME
comment1 = infile.readline().strip()
comment2 = infile.readline().strip()
fileType = infile.readline().strip()
dimension = infile.readline().strip().split()[2] # DIMENSION
edgeWeightType = infile.readline().strip().split()[1] # EDGE_WEIGHT_TYPE
infile.readline()

# print(dimension)
# Read node list
nodelist = []
n = int(dimension)
for i in range(0, n):
    x,y = infile.readline().strip().split()[1:]
    nodelist.append([float(x), float(y)])

# Close input file
infile.close()

print(nodelist)
print(len(nodelist))
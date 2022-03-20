#version 0.1
#Objective = To find a string of length 10 whose sum of difference in ASCII value between successive letters is exactly 100
import random
import string

def randomStringGenerator(N):
    t = ''.join(random.choices(string.ascii_uppercase, k = N))
    return t

# Initial Population
population = []
for i in range(100):
    candSol = randomStringGenerator(10)
    population.append(candSol)



# Calculate Fitness

fitness = []
for candSol in population:
    #todo : maybe we can optimize using two pointers
    ascii_values = [ord(character) for character in candSol]
    sumDiffAscii = 0
    for i in range(9):
        sumDiffAscii += abs(ascii_values[i]-ascii_values[i+1])
    fitness.append(sumDiffAscii)



# Selection

unsatSoln = []
satisfiedSoln = []
unsatFitness = []
satisfiedFitness = []
bestPop = []
bestFitness = []

for fitVal in range(len(fitness)):
    if(fitness[fitVal]==100):
        satisfiedSoln.append(population[fitVal])
        satisfiedFitness.append(fitness[fitVal])
    else:
        unsatSoln.append(population[fitVal])
        unsatFitness.append(abs(fitness[fitVal]-100))

bestPop = unsatSoln[:]
bestFitness = unsatFitness[:]

bestPop.sort()
bestFitness.sort()
bestPop = bestPop[::-1]
bestFitness = bestFitness[::-1]

bestPop = bestPop[:10]
bestFitness = bestFitness[:10]



# Crossover
# Say we have option to select multiple methods

# Implementation of first method [SPLITTING INTO TWO EQUAL HALVES]
for i in range(9):
    # Selecting next two best candSol each time [pairs (0,1), (2,3) and so on]
    k1 = bestPop[i]
    k2 = bestPop[i+1]
    # Performing Crossover
    t = k1[:]
    k1 = k2[5:] + k1[5:]
    k2 = k1[:5] + k2[:5]

# Implementation of second method [SPLITTING INTO 3 HALVES [3-4-3]]
'''for i in range(9):
    # Selecting next two best candSol each time [pairs (0,1), (2,3) and so on]
    k1 = bestPop[i]
    k2 = bestPopp[i+1]
    # Performing Crossover
    t = k1[:]
    k1 = k1[:2] + k2[2:7] + k1[7:]
    k2 = k1[:2] + k1[2:7] + k2[7:]
'''

        
        
# Mutation
for i in range(1):
    k1 = random.randrange(0, 10)
    k2 = random.randrange(0, 10)
    while(k1==k2):
        k1 = random.randrange(0, 10)
        k2 = random.randrange(0, 10)
    print(k1)
    print(k2)
    # Performing swap
    t = bestPop[i][k1]
    print(bestPop[i])
    bestPop[i] = bestPop[i][:k1] + bestPop[i][k2] + bestPop[i][(k1+1):]
    if(k2!=9):
        bestPop[i] = bestPop[i][:k2] + t + bestPop[i][(k2+1):]
    else:
        bestPop[i] = bestPop[i][:k2] + t
    print(bestPop[i])

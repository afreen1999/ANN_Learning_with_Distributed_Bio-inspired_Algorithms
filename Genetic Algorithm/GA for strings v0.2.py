# Objective - String with difference in values = 100
# for e.g.:- |a-z| = |1-26| = 25
# So - AZAZAZAZAZ [one of the solutions which is not currect]

import random
import string


def randomStringGenerator(N):
    t = ''.join(random.choices(string.ascii_uppercase, k = N))      # generates a random string of size N
    return t

  
  
# Initial Population
def initialPopulation(sizePop):                                     # size of population => initial population size [Number of strings]
    population = []
    
    sizeString = 10                                                 # size of string = 10 (e.g. :-  ACSOIKNSNV)
        
    for i in range(sizePop):
        candSol = randomStringGenerator(sizeString)                 # generating all strings for the initial population
        population.append(candSol)
        
    return population


  
# Calculate Fitness
def Fitness(population):
    fitness = []                                                    # stores fitness of the entire population
    
      
    
    for candSol in population:
        ascii_values = [ord(character) for character in candSol]    # e.g. :- [65, 67, 83, 79, 73, 75, 78, 83, 78, 86] for ACSOIKNSNV
        sumDiffAscii = 0
        
        maxv = 25*9                                                 # maximum difference possible between each adjacent positions = ord(Z)-ord(A)
                                                                    # i.e., 90-65 = 25 
                                                                    # for a string of size 10 - there can be 9 adjacent pairs 
                                                                    # i.e, total maximum difference possible = 25*9 [e.g. - AZAZAZAZAZ]

        minv = 0                                                    # minimum difference possible between each adjacent position [when both are same]
                                                                    # e.g - ord(A)-ord(A) = 0
                                                                    # i.e, total minimum difference possible = 0*9 = 0 [e.g. - AAAAAAAAAA]
        
        
        # Calculating the fitness (in our case, the total difference for a string) 
        for i in range(len(candSol)-1):
            diff = abs( ascii_values[i] - ascii_values[i+1] )
            sumDiffAscii += diff
        
        # calculating the normalized fitness  
        fitness_val = (sumDiffAscii - minv)/(maxv - minv)          # fitness = |(difference - min) / (max - min)|
                                                                   # fitness_val ∈ [0,1]  (some value equal to or between 0 and 1)
        fitness.append(fitness_val)
        
    return fitness


  
# Selection
def Selection(population):
  return population[:10]                                          # we return the top ten elements or parents as the best population




# Crossover
def Crossover(bestPop):
    children = []
    
    # Crossover method used [SPLITTING INTO TWO HALVES]
    for i in range(len(bestPop)):
        
        # Selecting next two best candSol each time [pairs (0,1), (0,2), ..., (1,0), (1,2), .... (9,1),(9,2), ...,  and so on]
        for j in range(len(bestPop)):
            if(i!=j):                                               # to avoid pairs like (0,0), (1,1), (2,2), ... 
                child1 = bestPop[i][:]
                child2 = bestPop[j][:]
                
                # Performing Crossover
                k = random.randint(0,len(bestPop[i]))
                child1 = child1[:k] + child2[k:]
                child2 = child1[k:] + child2[:k]
                children.append(child1)
                children.append(child2)        
                
    return children
  
  
  

# Mutation
def mutation(bestPop):
    
    i = random.randint(0, len(bestPop)-1)                           # Selecting a random string from the best population
    print(i, len(bestPop))
    k = random.randrange(0, len(bestPop[i]))
    t = random.randrange(65, 91)
    t = chr(t)
    sol = list(bestPop[i])
    sol[k]=t
    bestPop[i] = "".join(sol)
    return bestPop
   
    
    
    
# Taking individual chromosomes to fitness level
from matplotlib import pyplot as plt
def main():
    sizePop = 100
    target = 100   # The difference we wish to acheive
    iterations = 0
    
    # Step 1: Generating the initial population
    population = initialPopulation(sizePop)
    
    values = []                                                    # Will contain the final set of values
    
    while(iterations < 100):                                       # Maximum Iteration Count = 100
        print("--------------GENERATION "+str(iterations)+"-----------")
        iterations+=1
        
        # Step 2: Calculate Fitness
        fitness = Fitness(population)
        
        # sorting population based on fitness
        
        population = [x for y, x in sorted(zip(fitness, population), reverse=True)]
        
        fitness = [x for x, y in sorted(zip(fitness, population), reverse=True)]

        print(fitness[:10])        
        print(population[:10])
        
        values.append(fitness[0])
        
        if(abs(fitness[0]*25*9-target)<5):
            print('Found')
            print(population[0])
            break
        
        # Step 3: Selection
        bestPop = Selection(population)
        
        # Step 4: Crossover
        children = Crossover(bestPop)
        
        # Step 5: Mutation
        children = mutation(children)
        
        # Elitism
        elitRate = 0.1
        temp1 = int(elitRate*len(bestPop))
        temp2 = len(children) - temp1
        bestPop = bestPop[:temp1]
        population = bestPop + children
        
        
    print(population[0])
    ascii_values = [ord(character) for character in population[0]]
    sumDiffAscii = 0
    for i in range(len(population[0])-1):
        diff = abs( ascii_values[i] - ascii_values[i+1] )
        sumDiffAscii += diff   
    print(sumDiffAscii)
    
    plt.plot(values)
    plt.show()
    
   

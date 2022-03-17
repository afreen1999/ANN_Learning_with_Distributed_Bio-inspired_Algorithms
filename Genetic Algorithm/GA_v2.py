import random
import string
def randomStringGenerator(N):
    t = ''.join(random.choices(string.ascii_uppercase, k = N))
    return t

  
  
# Initial Population
def initialPopulation(sizePop):
    population = []
    
    sizeString = 10
    
    for i in range(sizePop):
        candSol = randomStringGenerator(sizeString)
        population.append(candSol)
        
    return population


  
# Calculate Fitness
def Fitness(population):
    fitness = []
    
    # fitness = |(diff - min) / (max - min)|
    
    '''
    # To find the max and min value over the entire population
    
    minAscPairs = [] # list to store min value of ascii for each candidate solution
    maxAscPairs = []
    for candSol in population:
        ascii_values = [ord(character) for character in candSol]
        temp = ascii_values[:]
        temp.sort()
        maxv = temp[-1]
        minv = temp[0]
        minAscPairs.append(minv)
        maxAscPairs.append(maxv)
    minAscPairs.sort()
    maxAscPairs.sort()
    minAscPairs = minAscPairs[::-1]
    maxAscPairs = maxAscPairs[::-1]
    minv = minAscPairs[0]
    maxv = maxAscPairs[-1]
    '''
    
    
    for candSol in population:
        ascii_values = [ord(character) for character in candSol]
        sumDiffAscii = 0
        
        maxv = 25*9
        minv = 0
        
        for i in range(len(candSol)-1):
            diff = abs( ascii_values[i] - ascii_values[i+1] )
            sumDiffAscii += diff
        
        fitness_val = (sumDiffAscii - minv)/(maxv - minv)
        fitness.append(fitness_val)
        
    return fitness


  
# Selection
def Selection(population):
  return population[-10:]




# Crossover
# Say we have option to select multiple methods
def Crossover(bestPop):
    children = []
    # Implementation of first method [SPLITTING INTO TWO EQUAL HALVES]
    for i in range(len(bestPop)):
        # Selecting next two best candSol each time [pairs (0,1), (0,2), ..., ..., (9,1),(9,2), ...,  and so on]
        for j in range(len(bestPop)):
            if(i!=j):
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
    # Random number of candidate solution chosen
    i = random.randint(0, len(bestPop)-1)
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
    
    population = initialPopulation(sizePop)
    
    values = []
    while(iterations < 100):
        print("--------------GENERATION "+str(iterations)+"-----------")
        iterations+=1
    
        fitness = Fitness(population)
        
        population = [x for y, x in sorted(zip(fitness, population))]
        
        fitness = [x for x, y in sorted(zip(fitness, population))]

        print(fitness[-10:])        
        print(population[-10:])
        
        values.append(fitness[-1])
        
        if(abs(fitness[-1]*25*9-target)<5):
            print('Found')
            print(population[-1])
            break
        
        bestPop = Selection(population)
        children = Crossover(bestPop)
        children = mutation(children)
        
        # Elitism
        elitRate = 0.1
        temp1 = int(elitRate*len(bestPop))
        temp2 = len(children) - temp1
        bestPop = bestPop[:temp1]
        population = bestPop + children
    print(population[-1])
    ascii_values = [ord(character) for character in population[-1]]
    sumDiffAscii = 0
    for i in range(len(population[-1])-1):
        diff = abs( ascii_values[i] - ascii_values[i+1] )
        sumDiffAscii += diff   
    print(sumDiffAscii)
    
    plt.plot(values)
    plt.show()
    

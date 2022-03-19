import random
import string
from matplotlib import pyplot as plt

class GeneticAlgorithm():
    
    def __init__(self, size_Population=2, n_iterations=100, elicitation_rate = 0.01, mutation_rate=0.0001, target = 100):
        # public data members
        self.elicitation_rate = elicitation_rate
        self.n_iterations = n_iterations
        self.mutation_rate = mutation_rate
        self.size_Population = size_Population    
        self.target = target
    
    def __randomStringGenerator(self, N):
        t = ''.join(random.choices(string.ascii_uppercase, k = N))      # generates a random string of size N
        return t

    
    # Initial Population
    def initialPopulation(self):                             # size of population => initial population size [Number of strings]
        population = []
        
        sizeString = 10                                                 # size of string = 10 (e.g. :-  ACSOIKNSNV)
            
        for i in range(self.size_Population):
            candSol = self.__randomStringGenerator(sizeString)               # generating all strings for the initial population
            population.append(candSol)
            
        return population


    
    # Calculate Fitness
    def Fitness(self, population):
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
                                                                        # i.e, total minimum difference possible = 25*9 [e.g. - AAAAAAAAAA]
            
            
            # Calculating the fitness (in our case, the total difference for a string) 
            for i in range(len(candSol)-1):
                diff = abs( ascii_values[i] - ascii_values[i+1] )
                sumDiffAscii += diff
            
            # calculating the normalized fitness  
            sumDiffAscii = abs(sumDiffAscii - 100)
            fitness_val = 1-((sumDiffAscii - minv)/(maxv - minv))      # fitness = |(difference - min) / (max - min)|
                                                                    # fitness_val ∈ [0,1]  (some value equal to or between 0 and 1)
            fitness.append(fitness_val)
            
        return fitness


    
    # Selection
    def Selection(self, population):
        return population[:10]                                          # we return the top ten elements or parents as the best population


    # Crossover
    def Crossover(self, bestPop):
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
    def mutation(self, bestPop):
        mutRate = self.mutation_rate
        while(int(mutRate)==1):
            mutRate*=10
        chance = random.randint(1,int(mutRate)+1)
        if(chance == mutRate):
            i = random.randint(0, len(bestPop)-1)                           # Selecting a random string from the best population
            print(i, len(bestPop))
            k = random.randint(0, len(bestPop[i])-1)
            t = random.randint(65, 90)
            t = chr(t)
            sol = list(bestPop[i])
            sol[k]=t
            bestPop[i] = "".join(sol)
        return bestPop
    
        
        
        
    # Taking individual chromosomes to fitness level
    def main(self):
                
        # Step 1: Generating the initial population
        population = self.initialPopulation()
        iterations = 0
        values = []                                                    # Will contain the final set of values
        
        while(iterations < self.n_iterations):                         # Maximum Iteration Count = 100
            print("--------------GENERATION "+str(iterations)+"-----------")
            iterations+=1
            
            # Step 2: Calculate Fitness
            fitness = self.Fitness(population)
            
            # sorting population based on fitness
            
            population = [x for y, x in sorted(zip(fitness, population), reverse=True)]
            
            fitness = [x for x, y in sorted(zip(fitness, population), reverse=True)]

            print(fitness[:10])        
            print(population[:10])
            
            
            ascii_values = [ord(character) for character in population[0]]
            sumDiffAscii = 0
            for i in range(9):
                diff = abs( ascii_values[i] - ascii_values[i+1] )
                sumDiffAscii += diff
            values.append(fitness[0])
            
            if(abs(sumDiffAscii-self.target)==0):
                print('Found')
                print(population[0])
                break
            
            # Step 3: Selection
            bestPop = self.Selection(population)
            
            # Step 4: Crossover
            children = self.Crossover(bestPop)
            
            # Step 5: Mutation
            children = self.mutation(children)
            
            # Elitism
            elitRate = self.elicitation_rate
            temp1 = int(elitRate*len(bestPop))
            bestPop = bestPop[:temp1]
            temp2 = int(elitRate*len(bestPop))+len(children)
            population = children + bestPop
            population = population[:temp2]
            
        print(population[0])
        ascii_values = [ord(character) for character in population[0]]
        sumDiffAscii = 0
        for i in range(len(population[0])-1):
            diff = abs( ascii_values[i] - ascii_values[i+1] )
            sumDiffAscii += diff   
        print(sumDiffAscii)
        
        plt.plot(values)
        plt.show()

ga=GeneticAlgorithm(3)          #arguments - size_Population, n_iterations, elicitation_rate, mutation_rate, target
ga.main()

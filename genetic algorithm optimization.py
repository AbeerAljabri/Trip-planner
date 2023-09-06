
import random
import numpy as np
from random import choice
import matplotlib.pyplot as plt
class activeties:
    def __init__(self, name, type , cost):
        self.name = name
        self.type = type
        self.cost = cost
 
#------------------------create activetyList---------------------------------#
activetyList = []
activetyList.append(activeties('Boulevard City', 'E' ,450 ))
activetyList.append(activeties('Boulevard World', 'E' ,550 ))
activetyList.append(activeties('Winter Wonder land ', 'E' ,300 ))
activetyList.append(activeties('Middle Beast', 'E' ,350 ))
activetyList.append(activeties('Riyadh Front', 'S' ,500 ))
activetyList.append(activeties('U Walk', 'S' ,400 ))
activetyList.append(activeties('The Zone', 'S' ,350 ))
activetyList.append(activeties('The Park Avenue', 'S' ,600 ))
activetyList.append(activeties('Albujairi', 'S' ,700 ))
activetyList.append(activeties('River Walk', 'S' ,400 ))
activetyList.append(activeties('Granada Mall', 'S' ,350 ))
activetyList.append(activeties('Centria Mall', 'S' ,900 ))
activetyList.append(activeties('Al Maigliah', 'S' ,200 ))
activetyList.append(activeties('Riyadh Park', 'S' ,550 ))
activetyList.append(activeties('Al Nakheel Mall', 'S' ,450 ))
activetyList.append(activeties('The Kingdom mall', 'S' ,500 ))
activetyList.append(activeties('Sky Bridge', 'E' ,70 ))
activetyList.append(activeties('Rawdat Tinhat', 'N' ,50 ))
activetyList.append(activeties('Camp Daliah', 'N' ,750 ))
activetyList.append(activeties('Horseback Safari', 'N' ,200 ))
activetyList.append(activeties('Hiking', 'N' ,300 ))
activetyList.append(activeties('Red Sands Trip', 'N' ,200))
activetyList.append(activeties('King Khaled Royal Reserve', 'N' ,350 ))
activetyList.append(activeties('Edge of the World', 'N' ,300 ))
activetyList.append(activeties('Nofa Wild Life Park', 'N' ,100 ))
activetyList.append(activeties('Al Thumamah', 'N' ,300 ))
activetyList.append(activeties('Rawdat Kharaim', 'N' ,400 ))
activetyList.append(activeties('Camping', 'N' ,1000 ))
activetyList.append(activeties('Resorts', 'N' ,1700 ))
activetyList.append(activeties('Perfume Expo', 'E' ,700 ))
activetyList.append(activeties('Theatre Shows', 'E' ,800 ))
activetyList.append(activeties('Swimming with Dolphine', 'E' ,550 ))
activetyList.append(activeties('Concert', 'E' ,700 ))
activetyList.append(activeties('Ramez Experience', 'E' ,200 ))
activetyList.append(activeties('Crystal Maze', 'E' ,300 ))
activetyList.append(activeties('Escape Room', 'E' ,100 ))



name = input('Welcome to Riyadh Season Trip Planner! What is your name?')
print('Hi ' + name + '!')

while True:
    try:   
        day1 = int(input('Please enter number of activities you prefer to do in Day1(1 or 2):'))
    except ValueError:
        print("Not an integer! Please enter an integer!!!!!")
        continue
    if ( day1 > 2 ) or ( day1 < 1 ):
         print('Please enter only(1 or 2)!!!!!')
         continue
    else:
        break
while True:
    try:   
        day2 = int(input('Please enter number of activities you prefer to do in Day2(1 or 2):'))
    except ValueError:
        print("Not an integer! Please enter an integer!!!!!")
        continue
    if ( day2 > 2 ) or ( day2 < 1 ):
         print('Please enter only(1 or 2)!!!!!')
         continue
    else:
        break
while True:
    try:   
        day3 = int(input('Please enter number of activities you prefer to do in Day3(1 or 2):'))
    except ValueError:
        print("Not an integer! Please enter an integer!!!!!")
        continue
    if ( day3 > 2 ) or ( day3 < 1 ):
         print('Please enter only(1 or 2)!!!!!')
         continue
    else:
        break
nomberOfActivity =  day1+day2+day3

while True:  
    type = input('Please enter your activity preference (E for Exciting, S for Shopping & Restaurants and N for Nature)')
    if (type.__eq__('E') ) or ( type.__eq__('S') ) or (type.__eq__('N')):
        break
    else:
        print('Please enter only( E or S or N )!!!!!')
        continue
    
while True:
    try:   
        budget = int(input('Please enter your budget'))
    except ValueError:
        print("Not an integer! Please enter an integer!!!!!")
        continue
    else:
        break


#-----------------------------------InitialPopulation-------------------------------------#

population = []
s = 20
for i in range(s) :
    indv = [] 
    population.append(indv)

#distribute activiteis randomly for each individual
for individual in population:
      n = random.randint(3,6)
      for i in range(n):
         n1 = random.randint(0,35)
         while ( n1 in individual):
             n1 = random.randint(0,35)
         individual.append(n1)



#------------------------------------Compute_Fitness-----------------------------------#

def Fitness (Individual):
 
    totalActivity = 0
    totalType= 0
    totalCost= 0

    for i in Individual:
          totalActivity = len(Individual)
          if ( type.__eq__(activetyList[i].type) ):
             totalType = totalType+1
          totalCost = totalCost + activetyList[i].cost

 ################-----nomber of activity-----################
        
          if ( totalActivity == nomberOfActivity):
              w1 = 1*0.25
          else:
              if ( totalActivity > nomberOfActivity):
                w1 =(nomberOfActivity/totalActivity)*0.25
              else:
                 w1 =(totalActivity/nomberOfActivity)*0.25
        
#####################----Type---############################# 
         
          w2 = (totalType/totalActivity)*0.5

#####################----cost----############################
      
          if ( totalCost <= budget ):
             w3 = 1*0.25
          else:
             w3 = (budget/totalCost)*0.25

    return w1+w2+w3

#Compute the fitness score of the initial population:
def compute_fitnes(population):
    fitness_score = []
    for Individual in population:
         fitness_score.append(Fitness(Individual))
    return fitness_score
#print(fitness_score)


#------------------------------------Selection using roulette_wheel-----------------------------------#

def roulette_wheel_selection(population):
    # Computes the totallity of the population fitness
    population_fitness = sum([Fitness(Individual) for Individual in population])

    # Computes for each chromosome the probability 
    chromosome_probabilities = [Fitness(Individual)/population_fitness for Individual in population]
    #print(chromosome_probabilities)
   
    # Selects one chromosome based on the computed probabilities
    selectedIndivisual = random.choices(population, chromosome_probabilities)

    return selectedIndivisual[0]
   

#------------------------------------Crossover-----------------------------------#

def Crossover ( a , b ):
# Crossover propality is 0.9
   if (random.random() < 0.9): 
      p = random.randint(1,5) 
      c =  a[0:p] + b[p:]
      d =  b[0:p] + a[p:]
      return c ,d
   return a,b


#------------------------------------mutation-----------------------------------# 

def mutation(Individual):

 # Choose random gene for mutation
 index = random.randrange(len(Individual))
 # Check for a mutatio
 p = random.random()
 # Mutation propality is 0.01
 if  p < 0.05:
    newValue = random.randint(0,35)
    while ( newValue in Individual):
             newValue = random.randint(0,35)
    Individual[index] =  newValue
 return Individual


#------------------------------------Replacement-----------------------------------# 

def replacement(population1):
  
    next_generation = []
   
    for i in range(10):
       #  two chromosomes are selected
        parent1 = roulette_wheel_selection(population1)
        parent2 = roulette_wheel_selection(population1)

        # crossover on the (pair) of two chromosomes 
        ChildrenList = Crossover(parent1, parent2)

        # mutation applied for the two indiviual 
        child1= mutation(ChildrenList[0])
        child2= mutation(ChildrenList[1])

       #compute fittness score for each child
        fitness_scorechild1 = Fitness(child1)
        fitness_scoreChild2 = Fitness(child2)

        
        fitnes_score = []
        fitnes_score =  compute_fitnes(population1)
        #find indivisual with minumun fitness
        n = fitnes_score.index(min(compute_fitnes(population1)))


        # check if the child1 is better than selected minimum indivisual
        if (fitness_scorechild1 > min(compute_fitnes(population1)) ):
             # Replace minimum indivisual whith child1
             population1[n] = child1
            

        fitnes_score = compute_fitnes(population1) 
        n = fitnes_score.index(min(compute_fitnes(population1)))
        # check if the child2 is better than selected minimum indivisual
        if (fitness_scoreChild2 > min(compute_fitnes(population1)) ):
            # Replace minimum indivisual whith child2
             population1[n] = child2

        next_generation = population1

        
    return next_generation


#------------------------------------create_generations-----------------------------------# 

def create_generations():

 avrageFittnes = []
 numberOfgeneration = []
 
 #create first generation
 generation = replacement(population)

 #loop until termination codition happened (reach maximum generations number (20000) or find the solution)
 for  i in range(20000):
    generation = replacement(generation)
    #compute population fitnes for plot
    population_fitness = sum([Fitness(Individual) for Individual in generation])
    avrageFittnes.append(population_fitness/20)
    numberOfgeneration.append(i)
    #print('genaration ' , i ,  'avarage :' ,avrageFittnes[i] )
    # Compute error value
    if ( 1 - avrageFittnes[i] < 0.00000001):
        break
   
 max=0
 #find best solution indivisual in last generation
 for indivisual in generation:
     if(Fitness(indivisual )> max):
        max= Fitness(indivisual )
        solution= indivisual
 #print('max fitness',max)
 print("*****************************************************")
 print("Your trip plan is ready! Your plan is presented below.")
 #print(solution)

 i =0
 j=0
 while ( i < day1):
       print("Day 1: " , activetyList[solution[j]].name )
       i =i+1
       j = j+1
 i =0
 while ( i < day2 and j != len(solution)):
       print("Day 2: ", activetyList[solution[j]].name)
       i =i+1
       j = j+1
 i =0
 while ( i < day3 and j != len(solution)):
       print("Day 3: " , activetyList[solution[j]].name )
       i =i+1
       j = j+1
  

 plt.plot(numberOfgeneration,avrageFittnes, marker='o')
 plt.yscale('linear')
 plt.title("GA Performance")
 plt.xlabel("Generation")
 plt.ylabel("Fitness")
 plt.show()

create_generations()

















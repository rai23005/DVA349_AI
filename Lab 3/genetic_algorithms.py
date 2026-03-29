
from share_function import tsp_route
from share_function import route_length
from share_function import grafh_history

import random


#skapa en population av slumpmässiga rutter
def create_population(pop_size, num_locations, dist):
    population = []
    for _ in range(pop_size):
        route = create_random_route(num_locations)
        fitness = route_length(tsp_route(route), dist)
        population.append((route, fitness))
    return population


# Skapa en slumpmässig rutt, förutom start 
def create_random_route(n):
    
    route = list(range(1, n))
    random.shuffle(route)
    return route



#Korsa föräldrar
def crossover(parent_1_route, parent_2_route):
    parent_length = len(parent_1_route)

    #kopiera en del av parent_1_route och lägg den i child
    start, end = sorted(random.sample(range(parent_length), 2))
    child = [None] * parent_length
    child[start:end] = parent_1_route[start:end]

    # Fyller resterande från parent_2_route i child, i ordning, och hoppar över de som redan finns i child
    p2_index = 0
    for i in range(parent_length):
        if child[i] is None:
            while parent_2_route[p2_index] in child:
                p2_index += 1
            child[i] = parent_2_route[p2_index]

    return child

#Mutationtation av en rutt
def mutation(child):

    # #Bestäm sannolikheten för mutationn, mellan 0.01% och 10%
    probability = random.uniform(0.001, 0.10)


    # ##två svaps i rutten, med sannolikheten
    # if random.random() < 0.2:  
    #     i, j = random.sample(range(len(child)), 2)
    #     child[i], child[j] = child[j], child[i]
    #     k, l = random.sample(range(len(child)), 2)
    #     child[k], child[l] = child[l], child[k]
    #     m, n = random.sample(range(len(child)), 2)
    #     child[m], child[n] = child[n], child[m]
        

    if random.random() < probability:
        i, j = sorted(random.sample(range(len(child)), 2))
        child[i:j] = reversed(child[i:j])
    return child


#skap ett barn genom crossover och mutation
def create_child(parent_1, parent_2, dist):

    route1 = parent_1[0]
    route2 = parent_2[0]

    child_route = crossover(route1, route2)

    child_route = mutation(child_route)

    child_fitness = route_length(tsp_route(child_route), dist)

    return (child_route, child_fitness)



#selektion av de bästa rutterna
def tournament_selection(population):
    tournament = random.sample(population, 5)
    tournament.sort(key=lambda x: x[1])  # sortera på fitness
    return tournament[0]   # returnerar (route, fitness)

#Huvudfunktionen för genetiska algoritmen
def genetic_algoritm(locations, dist, pop_size, generations):
    population = create_population(pop_size, len(locations), dist)

    fitness_calculations = pop_size

    history = []

    for gen in range(generations):


        #Ta reda på den bästa rutten i populationen
        population.sort(key=lambda x: x[1])
        shortest_distans = population[0][1]
        fitness = 1.0 / shortest_distans
        history.append(fitness*1000)

        #Kommit under distans 9000, stoppa algoritmen
        if shortest_distans < 9000:
            print("\n***Confetti***")
            print("Reach distan under 9000!")
            break

        #Skapa nästa generation, spara den bästa rutten från nuvarande generationen
        next_generation = []
        next_generation.append(population[0])  
        next_generation.append(population[1])


        #Mix and match för att skapa barn tills vi har en full nästa generation
        while len(next_generation) < pop_size:

            parent_1 = tournament_selection(population)
            parent_2 = tournament_selection(population)
            child = create_child(parent_1, parent_2, dist)
            next_generation.append(child)
            fitness_calculations += 1


            # Gjort 250,000 fitnessberäkningar, stoppa algoritmen
            if fitness_calculations >= 250000:
                print("Reached max 250,000 fitness calculations.")
                population = next_generation
                population.sort(key=lambda x: x[1])
                return population[0], history, fitness_calculations

       
        population = next_generation  

    #Få ut den bästa rutten och historia för att plotta
    population.sort(key=lambda x: x[1])
    return population[0], history, fitness_calculations   



def start_GA(locations, dist, pop_size, generations):
    print("\n##################################################################################################\n")
    print("LAb 3 -  Genetic Algorithms (GA)")

    best_route, history, fitness_calculations = genetic_algoritm(locations, dist, pop_size, generations )

    format_fittnes_cal = '{:,.0f}'.format(fitness_calculations).replace(',', ' ')

    print(f"\nBest Route: {tsp_route(best_route[0])}")
    print(f"Lenght distans on route: {best_route[1]}")
    print(f"Number of fitness calculations:  {format_fittnes_cal}")
    grafh_history(history, title="Shortest Distance Over Generations in Genetic Algorithms")


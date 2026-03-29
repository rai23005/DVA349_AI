from share_function import tsp_route
from share_function import route_length
from share_function import grafh_history

import random

#Skapa en initial pheromone-matris för alla platser par
def create_initial_pheromone_matrix(num):
    pheromone = [[1.0 for _ in range(num)] for _ in range(num)]
    
    for i in range(num):
        pheromone[i][i] = 0.0
    
    return pheromone

#räkna ut heuristic information 1 / distans r->s
def calculate_heuristic_information(distance_matrix):
    num=len(distance_matrix)
    heuristic_info = [[0.0 for _ in range(num)] for _ in range(num)]
    
    for i in range(num):
        for j in range(num):
            if i != j:
                heuristic_info[i][j] = 1.0 / distance_matrix[i][j]
    
    return heuristic_info

#ant Probabilistic rule   
def calculate_probabilities(current_location, available_locations, pheromone_matrix, heuristic_info, alpha=1.0, beta=2.0):
    total_pheromone = 0.0
    probabilities = []

    #Beräkna sannolikheten för varje tillgänglig plats baserat på pheromone och heuristic information
    for location in available_locations:
        pheromone = pheromone_matrix[current_location][location] ** alpha
        heuristic = heuristic_info[current_location][location] ** beta
      
        value_of_phero_heris=pheromone * heuristic
        
        probabilities.append(value_of_phero_heris)
        total_pheromone += value_of_phero_heris


    # Normalisera sannolikheterna, vilken plats som har högst sannolikhet att väljas
    return [p / total_pheromone for p in probabilities]


#Vilkan lokation skall besöka nästa gång
def chose_next_location():
    next_location = None

    return next_location

#en myras vägkonstruktion
def ant_path_construction(pheromone_matrix, heuristic_info, distance_matrix, alpha, beta):
    
    num_loc = len(distance_matrix)
    path = [0]  
    visited = set(path)


    #Vilka platser som är tillgängliga att besöka och vilken plats som har högst sanolikhet att väljas
    while len(visited) < num_loc:
        current_location = path[-1]
        available_locations = [i for i in range(num_loc) if i not in visited]

        probabilities = calculate_probabilities(current_location, available_locations, pheromone_matrix, heuristic_info, alpha, beta)
        
        next_location = random.choices(available_locations, weights=probabilities)[0]
        
        path.append(next_location)
        visited.add(next_location)

    #Åter till startplatsen för att sluta ruten
    path.append(0)    
    return path

#uppdatera pheromone-matrisen baserat på den bästa rutten och dess längd
def pheromone_update(pheromone_matrix, all_routes, all_lengths, evaporation_rate):

    num_locations = len(pheromone_matrix)
    
    #Avdusning av pheromone
    for i in range(num_locations):
        for j in range(num_locations):
            pheromone_matrix[i][j] *= (1 - evaporation_rate)  

    # Pherome som varje myra lägger till baserat på sin rutt och dess längd
    for k in range(len(all_routes)):  # varje myra
        route = all_routes[k]
        length = all_lengths[k] 

        delta = 1.0 / length  

        for i in range(len(route) - 1):
            r = route[i]
            s = route[i + 1]

            pheromone_matrix[r][s] += delta
            pheromone_matrix[s][r] += delta


#huvud funktion för ACO algoritmen
def aco_algorithm(locations, distance_matrix, num_ants=30, num_iterations=500, alpha=1.0, beta=2.0, evaporation_rate=0.5):

    num_location=len(locations)
    pheromone_matrix = create_initial_pheromone_matrix(num_location)
    heuristic_info = calculate_heuristic_information(distance_matrix)

    best_route = None
    best_fitness = 0
    best_length = float('inf')

    history = []

    for iteration in range(num_iterations):
        all_routes = []
        all_lengths = []


        if best_length < 9000:
                print("\n***Confetti***")
                print("Reach distan under 9000!")
                break

        for ant in range(num_ants):
            route = ant_path_construction(pheromone_matrix, heuristic_info, distance_matrix, alpha, beta)
            length = route_length(route, distance_matrix)

            all_routes.append(route)
            all_lengths.append(length)

            fitness = 1.0 / length

            if fitness > best_fitness:
                best_fitness = fitness
                best_length = length
                best_route = route

        pheromone_update(pheromone_matrix, all_routes, all_lengths, evaporation_rate)

        history.append(best_fitness*1000)  
      



    return best_route, best_length, history

def start_ACO(locations, distance_matrix, num_ants, num_iterations, alpha=1.0, beta=2.0, evaporation_rate=0.5):

    print("\n##################################################################################################\n")
    print("LAb 3 -  Ant Colony Optimization (ACO)")

    best_route, best_length, history = aco_algorithm(locations, distance_matrix, num_ants, num_iterations, alpha, beta, evaporation_rate)

    print(f"\nBest Route: {best_route}")
    print(f"Best Length: {best_length}")
    grafh_history(history, "ACO - Shortest Distance Over Iterations")

    
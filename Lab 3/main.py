from loadfile import loadfile   
from genetic_algorithms import start_GA
from ant_colony_optimization import start_ACO
from share_function import compute_distance_matrix


def main():

        location = loadfile("Assignment_3_berlin52.tsp")
        distans_matrix=compute_distance_matrix(location)


        pop_size = 150
        generations = 1000


        num_ants=10
        num_iterations=100
        alpha=1.0
        beta=2.0
        pheromene_evaporation_rate=0.5

        start_GA(location, distans_matrix, pop_size, generations)
        start_ACO(location, distans_matrix, num_ants, num_iterations, alpha, beta, pheromene_evaporation_rate)

       
       
   
if __name__ == "__main__":

    main()
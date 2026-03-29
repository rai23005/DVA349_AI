from .loadFilePartTwoy import load_spain_map
from .createmap import createmap
from .greedy_best_first_search import greedy_best_first_search
from .a_star_search import a_star_search



def partTwo_pathfinding(start_city, goal_city):

    edges, straight_paths = load_spain_map("Assignment 1 Spain map.txt")

    mapdirection = createmap(edges)


    print("\n##################################################################################################\n")
    print("Part 2: Pathfinding in Spain Greedy & A*\n")
    print(f"Greedy Best-First Search from {start_city} to {goal_city}:\n")
     
    greedy_best_first_search(mapdirection, straight_paths, start_city, goal_city)
   
    print("Part 2: Pathfinding in Spain (A*-search)\n")
    print(f"A* Search from {start_city} to {goal_city}:\n")

    a_star_search(mapdirection, straight_paths, start_city, goal_city)
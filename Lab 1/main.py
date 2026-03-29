
from part_One.part_One_knapsack import partOne_knapsack
from part_Two.part_Two_pathfinding import partTwo_pathfinding

def main():

    print("\n##################################################################################################\n")
    print("LAb 1")
    partOne_knapsack()

    startCity = "Malaga"
    goalCity = "Valladolid"
    partTwo_pathfinding(startCity, goalCity)    
   
if __name__ == "__main__":

    main()
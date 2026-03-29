

def greedy_best_first_search(map, heuristic,current_city, goal_city):

    if current_city not in map:
        print(f"Error: Start city '{current_city}' does not exist in the map.")
        return

    if not map[current_city]:
        print(f"Error: Start city '{current_city}' has no neighbors to move to.")
        return

    if goal_city not in map:
        print(f"Error: Goal city '{goal_city}' does not exist in the map.")
        return

    city_alrady_visited = set()
    road_selection = []
    movecount = 0
    cost_to_reach_goal = 0


    while current_city != goal_city:
        print(f"We are at city: {current_city}")
        city_alrady_visited.add(current_city)
        road_selection.append(current_city)

        neighbors = map[current_city]        
        best_neighbor = None
        best_heuristic = None  


        for neighbor in neighbors:
            heuristic_value = heuristic[neighbor]
            print(f"Neighbor: {neighbor}, Heuristic value: {heuristic_value}")

        for neighbor in neighbors:              
            if neighbor in city_alrady_visited: 
                print(f"Already visited, {neighbor}")
                continue  

            heuristic_value = heuristic[neighbor] 
            if best_heuristic is None or heuristic_value < best_heuristic:
                best_heuristic = heuristic_value
                best_neighbor = neighbor
                

            if best_neighbor is None:
                print(f"No path found to the city: {current_city}. Stopping search.")
                break

        print(f"\nBest neighbor to move to: {best_neighbor} with heuristic {best_heuristic}\n")
        movecount += 1
        cost_to_reach_goal += map[current_city][best_neighbor]
        current_city = best_neighbor
    
    
    print("\n**************************************************************************************************\n")
    road_selection.append(goal_city)
    print(f"Goal city {goal_city} reached in {movecount} moves! Cost to reach goal: {cost_to_reach_goal}\nRoad taken: {' -> '.join(road_selection)}\n")
    print("\n**************************************************************************************************\n")


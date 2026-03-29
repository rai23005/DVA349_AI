import heapq

def a_star_search(map, heuristic, current_city , goal_city):

    if current_city  not in map:
        print(f"Error: Start city '{current_city }' does not exist in the map.")
        return

    if not map[current_city ]:
        print(f"Error: Start city '{current_city }' has no neighbors to move to.")
        return

    if goal_city not in map:
        print(f"Error: Goal city '{goal_city}' does not exist in the map.")
        return

    city_alrady_visited = set()
    
    best_f_value_for_city = {city: float('inf') for city in map}
    best_f_value_for_city[current_city] = 0
    
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[current_city ], current_city , 0, [current_city]))
   

    while priority_queue:
        f_value, current_city, g_cost_so_far, road_selection = heapq.heappop(priority_queue)

        print(f"\nWe are at city: {current_city }, cost so far (g): {g_cost_so_far}, Heuristic value h(n): {heuristic[current_city ]} f(n): {f_value}")
        
        if current_city  == goal_city:
            print("\n**************************************************************************************************\n")
            print(f"\nGoal reached!\nTotal Cost to reached  {g_cost_so_far}")
            print(f"Road taken: {' -> '.join(road_selection)}")
            print("\n**************************************************************************************************\n")
            break
      
        if current_city  in city_alrady_visited:
            continue

        city_alrady_visited.add(current_city )

        for neighbor, distance in map[current_city ].items():

            uppdate_g_value = g_cost_so_far + distance      
            uppdate_f_value = uppdate_g_value + heuristic[neighbor]
           
            if  uppdate_f_value < best_f_value_for_city[neighbor]:
                best_f_value_for_city[neighbor] = uppdate_f_value
                
                heapq.heappush(priority_queue, (uppdate_f_value, neighbor, uppdate_g_value, road_selection + [neighbor]))

        print("\nPriority Queue State:")
        for f_value, city, g, path in sorted(priority_queue):
            print(f"City: {city},\t f(n)={f_value}")
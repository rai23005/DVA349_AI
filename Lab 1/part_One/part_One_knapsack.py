from .loadFilePartOne import load_knapsack_file
from .BreadthFirstSearch import bfs_knapsack
from .DepthFirstSearch import dfs_knapsack

def partOne_knapsack():

    items, capacity = load_knapsack_file("Assignment 1 knapsack.txt")
    benefit_BFS, bagofHolding_BFS, sack_weight_BFS = bfs_knapsack(items, capacity)
    benefit_DFS, bagofHolding_DFS, sack_weight_DFS = dfs_knapsack(items, capacity)

    print("\n##################################################################################################\n")
    print("Part 1: The Knapsack Problem (BFS & DFS)\n")
    print(f"Capacity: {capacity}")
    print(f"Items loaded: {len(items)}\n")

    print("BFS result:")
    print(f"Benefit: {benefit_BFS}")
    print(f"Items Selected: {bagofHolding_BFS}")
    print(f"Weight of sack: {sack_weight_BFS}\n")

    print("\nDFS result:")
    print(f"Benefit: {benefit_DFS}")
    print(f"Items Selected: {bagofHolding_DFS}")
    print(f"Weight of sack: {sack_weight_DFS}\n")
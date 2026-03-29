
def dfs_knapsack(items, capacity):
    stack = []
   
    stack.append((0, 0, 0, []))

    best_benefit = 0
    best_combination = []
    best_weight = 0


    while stack:
        index, current_weight, current_benefit, selected_items = stack.pop()

        if current_weight > capacity:
            continue

        if index == len(items):
            if current_benefit > best_benefit:
                best_benefit = current_benefit
                best_combination = selected_items
                best_weight = current_weight
            continue

        item = items[index]
        
        stack.append((
            index + 1,
            current_weight + item['weight'],
            current_benefit + item['benefit'],
            selected_items + [item['id']]))

        
        stack.append((
            index + 1,
            current_weight,
            current_benefit,
            selected_items))
        
    return best_benefit, best_combination, best_weight
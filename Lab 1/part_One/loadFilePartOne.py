def load_knapsack_file(file_path):
    items = []
    capacity = None
    reading_items = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith('MAXIMUM WEIGHT'):
                capacity = int(line.split(':')[1].strip())

            elif line.startswith('ID'):
                reading_items = True
                continue

            elif line == 'EOF':
                break           

            elif reading_items and line:
                item_id, benefit, weight = map(int, line.split())
                items.append({'id': item_id, 'benefit': benefit, 'weight': weight})



    return items, capacity
    
def load_spain_map(file_path):
    edges = []
    straight_paths = {}

    reading_edges = False
    reading_straight_paths = False
   
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("NAME") or line.startswith("TYPE") or line.startswith("COMMENT"):
                continue  

            if line.startswith('A B'):
                reading_edges = True
                reading_straight_paths = False
                continue

            if line.startswith('Straight line'):
                reading_edges = False
                reading_straight_paths = True
                continue

            if reading_edges:
                nodeA, nodeB, edge_distance = line.split()
                distance = int(edge_distance)
                edges.append({"from": nodeA, "to": nodeB, "distance":distance})

            elif reading_straight_paths:
                city, straight_distance = line.split()
                distance_str_paths = int(straight_distance)
                straight_paths[city] = distance_str_paths

    return edges, straight_paths
    
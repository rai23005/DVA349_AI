import math

#distans mellan två lokcationer
def euclidean_distance(location_1, location_2):
    return math.sqrt((location_1['x'] - location_2['x'])**2 +
                     (location_1['y'] - location_2['y'])**2)

def compute_distance_matrix(locations):
    n = len(locations)
    dist_matrix = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(locations[i], locations[j])
    
    return dist_matrix

#skapa en runt med start och slut
def tsp_route(route):
    return [0] + route + [0]

#räkna ut ruten längd
def route_length(route, dist):
    total = 0
    for a,b in zip(route, route[1:]):
        total += dist[a][b]
    return total


def grafh_history(history, title):
    import matplotlib.pyplot as plt

    plt.plot(history)
    plt.title(title)
    plt.xlabel("Generation")
    plt.ylabel("Fittness")
    plt.grid()
    plt.show()

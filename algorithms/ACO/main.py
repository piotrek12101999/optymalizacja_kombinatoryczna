import math

from algorithms.ACO.ACO import ACO, Graph


def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


def main_aco(file):
    cities = []
    points = []
    with open(file) as f:
        for index, line in enumerate(f.readlines()):
            if index != 0:
                city = line.split(' ')
                cities.append(dict(index=int(city[0]), x=int(city[1]), y=int(city[2])))
                points.append((int(city[1]), int(city[2])))

    cost_matrix = []
    rank = len(cities)
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)
    aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 2)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)
    return points, path, cost

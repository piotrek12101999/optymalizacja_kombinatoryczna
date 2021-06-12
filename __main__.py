from algorithms.ACO.main import main_aco
from algorithms.Greedy.main import main_greedy
from utils.plot import plot

if __name__ == "__main__":
    file = "data_sets/berlin52.txt"
    # points, path, cost = main_greedy(file)
    points, path, cost = main_aco(file)
    plot(points, path)
    print(cost)

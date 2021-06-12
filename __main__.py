from algorithms.ACO.main import main_aco
from algorithms.Greedy.main import main_greedy
from utils.plot import plot


def get_best_result(file_name, attempts):
    best_result = {}
    for _ in range(attempts):
        points, path, cost = main_aco(file_name)
        if 'cost' in best_result:
            if cost < best_result['cost']:
                best_result['points'] = points
                best_result['path'] = path
                best_result['cost'] = cost
        else:
            best_result['points'] = points
            best_result['path'] = path
            best_result['cost'] = cost

    return best_result


if __name__ == "__main__":
    file = "data_sets/berlin52.txt"

    # points, path, cost = main_greedy(file)
    # plot(points, path)

    best_result = get_best_result(file, 2)
    print(best_result['cost'])
    plot(best_result['points'], best_result['path'])


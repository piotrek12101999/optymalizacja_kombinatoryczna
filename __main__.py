from utils.load_file import load_file
from utils.get_vertex_number import get_vertex_number
from utils.calculate_time import calculate_time
from algorithms.Greedy import Greedy

if __name__ == "__main__":
    file = 250
    plot_points = []
    struct = []
    file_name = "data_sets/tsp{0}.txt".format(file)
    lines = load_file(file_name)
    vertex_number = get_vertex_number(lines, struct, plot_points)

    greedy = Greedy(plot_points, struct, vertex_number)
    time, results = calculate_time(greedy.get_results)
    print(time, results)
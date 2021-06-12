from utils.load_file import load_file
from utils.get_vertex_number import get_vertex_number
from algorithms.Greedy.Greedy import Greedy


def get_points(lines):
    points = []
    for index, line in enumerate(lines):
        if index != 0:
            split_line = line.split(" ")
            points.append((int(split_line[1]), int(split_line[2].replace('\n', ''))))
    return points


def main_greedy(file):
    plot_points = []
    struct = []
    lines = load_file(file)
    vertex_number = get_vertex_number(lines, struct, plot_points)

    greedy = Greedy(plot_points, struct, vertex_number)
    path, cost = greedy.get_results()
    points = get_points(lines)
    return points, path, cost

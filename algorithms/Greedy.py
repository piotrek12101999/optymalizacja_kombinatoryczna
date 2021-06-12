import math


class Greedy:
    def __init__(self, plot_points, struct, vertex_number):
        self.plot_points = plot_points
        self.struct = struct
        self.vertex_number = vertex_number

    def calculate_vertex(self, index):
        min_value = 0
        min_index = 0

        for i in range(self.vertex_number):
            if not self.struct[i].get("available"):
                continue

            tmp = math.sqrt(
                (self.struct[i].get("X") - self.struct[index].get("X")) ** 2 + (self.struct[i].get("Y") - self.struct[index].get("Y")) ** 2)

            if tmp < min_value or min_value == 0:
                min_value = tmp
                min_index = i

        self.struct[min_index]["available"] = False
        return min_index, min_value

    def get_results(self):
        vertex_actual_index = 0
        result_v = []
        result_d = 0

        result_v.append(self.struct[vertex_actual_index].get("index"))
        self.struct[0]["available"] = False

        for i in range(self.vertex_number - 1):
            vertex_actual_index, vertex_distance_tmp = self.calculate_vertex(vertex_actual_index)

            result_v.append(self.struct[vertex_actual_index].get("index"))
            result_d = result_d + vertex_distance_tmp

        result_d = result_d + math.sqrt((self.struct[0].get("X") - self.struct[vertex_actual_index].get("X")) ** 2 + (
                    self.struct[0].get("Y") - self.struct[vertex_actual_index].get("Y")) ** 2)

        return round(result_d)


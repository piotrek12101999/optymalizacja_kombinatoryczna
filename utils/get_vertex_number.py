def get_vertex_number(lines, struct, points):
    i = 0
    vertex_number = 0

    for line in lines:
        if i == 0:
            vertex_number = int(line.rstrip("\n"))
            i = i + 1
            continue

        line_tmp = line.rstrip("\n").split(" ")
        struct_tmp = {"index": int(line_tmp[0]), "X": int(line_tmp[1]), "Y": int(line_tmp[2]), "available": True}
        points.append([line_tmp[1], line_tmp[2]])
        struct.append(struct_tmp)

    return vertex_number

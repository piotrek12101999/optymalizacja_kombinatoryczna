def load_file(file_name):
    file = open(file_name, "r")
    lines_raw = file.readlines()
    file.close()

    return lines_raw




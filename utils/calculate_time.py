import time


def calculate_time(callback):
    time_start = time.time()
    calculation_result = callback()
    time_end = time.time()
    return time_end - time_start, calculation_result

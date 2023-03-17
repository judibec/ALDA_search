import time
from complexity import constants
from complexity import dataGenerator
from searchMethods import searching as s


def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


def take_times(size, samples_by_size):
    samples = []
    for _ in range(samples_by_size):
        samples.append(dataGenerator.get_random_list(size))
    return [
        take_time_for_algorithm(samples, s.linearSearch),
        take_time_for_algorithm(samples, s.binarySearch),
        take_time_for_algorithm(samples, s.ternarySearch)
    ]


def take_time_for_algorithm(samples_array, sorting_approach):
    times = []
    for sample in samples_array:
        start_time = time.time()
        n = sample[-1]
        sorting_approach(sample.copy(), n)
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]

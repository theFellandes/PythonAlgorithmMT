import time
from numpy.random import randint
import random
from Heap import Heap


def main():
    heap = Heap()
    build_max_heap_report(heap)
    heapsort_report(heap)
    # max_heap_insert_report(heap)
    # heap_extract_max_report(heap)
    # heap_increase_key_report(heap)
    # heap_maximum_report(heap)


def build_max_heap_report(heap: Heap):
    result = []
    peak_value = 1000
    while peak_value <= 100_000:
        arr = randint(0, peak_value, peak_value)

        tic = time.perf_counter()
        heap.build_max_heap(arr)
        toc = time.perf_counter()

        result.append(peak_value)
        result.append(toc - tic)
        peak_value = peak_value + 1000
    print_result('build_max_heap.txt', result, 'ms')


def heapsort_report(heap: Heap):
    result = []
    peak_value = 1000
    while peak_value <= 100_000:
        arr = randint(0, peak_value, peak_value)

        tic = time.perf_counter()
        heap.heapsort(arr)
        toc = time.perf_counter()

        result.append(peak_value)
        result.append(toc - tic)
        peak_value = peak_value + 1000
    print_result('heapsort.txt', result, 'ms')


def max_heap_insert_report(heap: Heap):
    result = []
    arr = []
    peak_value = 1000
    while peak_value <= 100_000:
        for i in range(0, peak_value):
            arr.append(random.randint(0, peak_value))

        tic = time.perf_counter_ns()
        heap.max_heap_insert(arr, random.randint(0, peak_value), len(arr) - 1)
        toc = time.perf_counter_ns()

        result.append(peak_value)
        #microseconds
        result.append((toc - tic) / 1000)
        peak_value = peak_value + 1000
    print_result('max_heap_insert.txt', result, 'microseconds')


def heap_extract_max_report(heap: Heap):
    result = []
    peak_value = 1000
    arr = []
    while peak_value <= 100_000:
        for i in range(0, peak_value):
            arr.append(random.randint(0, peak_value))

        tic = time.perf_counter_ns()
        heap.heap_extract_max(arr, len(arr) - 1)
        toc = time.perf_counter_ns()

        result.append(peak_value)
        result.append((toc - tic) / 1000)
        peak_value = peak_value + 1000
    print_result('heap_extract_max.txt', result, 'microseconds')


def heap_increase_key_report(heap: Heap):
    result = []
    peak_value = 1000
    arr = []
    while peak_value <= 100_000:
        for i in range(0, peak_value):
            arr.append(random.randint(0, peak_value))

        tic = time.perf_counter_ns()
        heap.heap_increase_key(arr, random.randint(0, peak_value), random.randint(0, peak_value))
        toc = time.perf_counter_ns()

        result.append(peak_value)
        result.append((toc - tic) / 1000)
        peak_value = peak_value + 1000
    print_result('heap_increase_key.txt', result, 'microseconds')


def heap_maximum_report(heap: Heap):
    result = []
    peak_value = 1000
    while peak_value <= 100_000:
        arr = randint(0, peak_value, peak_value)

        tic = time.perf_counter_ns()
        heap.heap_maximum(arr)
        toc = time.perf_counter_ns()

        result.append(peak_value)
        result.append((toc - tic) / 1000)
        peak_value = peak_value + 1000
    print_result('heap_maximum.txt', result, 'microseconds')


def print_result(text_name: str, result: list, unit: str):
    index = 0
    with open(text_name, 'w') as f:
        f.write('Size, Time(' + unit + ')\n')
        for line in result:
            if index % 2 == 1:
                f.write(", " + str(line) + "\n")
            else:
                f.write(str(line))
            index = index + 1


if __name__ == '__main__':
    main()

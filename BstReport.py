import time

from BinarySearchTree import Tree
import random


def main():
    # insert_report()
    # inorder_tree_walk_report()
    # search_report()
    # minimum_report()
    # min_report()
    # maximum_report()
    # max_report()
    # successor_report()
    # predecessor_report()
    # ratio_report()
    delete_report()


def insert_report():
    peak_value = 1000
    tree_insert_time = []
    while peak_value <= 100_000:
        bst = Tree()
        tic = time.perf_counter()
        for i in range(0, peak_value):
            bst.tree_insert(random.randint(0, peak_value))
        toc = time.perf_counter()
        tree_insert_time.append(peak_value)
        tree_insert_time.append(toc - tic)
        peak_value = peak_value + 1000
        del bst
    print_result('insert.txt', result=tree_insert_time, unit='ms')


def inorder_tree_walk_report():
    peak_value = 1000
    tree_time = []
    while peak_value <= 100_000:
        bst = Tree()
        root = 0
        for i in range(0, peak_value + 1):
            if i == 0:
                root = random.randint(0, peak_value + 1)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter()
        bst.inorder_tree_walk(root_node)
        toc = time.perf_counter()
        tree_time.append(peak_value)
        tree_time.append(toc - tic)
        peak_value = peak_value + 1000
        del bst
    print_result('inorder_tree_walk.txt', result=tree_time, unit='ms')


def search_report():
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        bst = Tree()
        for i in range(0, peak_value):
            bst.tree_insert(random.randint(0, peak_value))
        tic = time.perf_counter_ns()
        root_node = bst.tree_search(random.randint(0, peak_value))
        toc = time.perf_counter_ns()
        result.append(peak_value)
        result.append((toc - tic) / 1000)
        peak_value = peak_value + 1000
        del bst
    print_result('search2.txt', result=result, unit='micros')


def minimum_report():
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        bst = Tree()
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter_ns()
        bst.tree_minimum(root_node)
        toc = time.perf_counter_ns()
        result.append(peak_value)
        result.append((toc - tic) / 1000)
        peak_value = peak_value + 1000
        del bst
    print_result('minimum.txt', result=result, unit='micros')


def maximum_report():
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        bst = Tree()
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter_ns()
        bst.tree_maximum(root_node)
        toc = time.perf_counter_ns()
        result.append(peak_value)
        result.append((toc - tic) / 1000)
        peak_value = peak_value + 1000
        del bst
    print_result('maximum.txt', result=result, unit='micros')


def successor_report():
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        bst = Tree()
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter_ns()
        bst.tree_successor(root_node)
        toc = time.perf_counter_ns()
        result.append(peak_value)
        result.append((toc - tic) / 1000)
        peak_value = peak_value + 1000
        del bst
    print_result('successor.txt', result=result, unit='micros')


def predecessor_report():
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        bst = Tree()
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter_ns()
        bst.tree_predecessor(root_node)
        toc = time.perf_counter_ns()
        result.append(peak_value)
        result.append((toc - tic) / 1000)
        peak_value = peak_value + 1000
        del bst
    print_result('predecessor.txt', result=result, unit='micros')


def min_report():
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        bst = Tree()
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter()
        bst.tree_min_path_length(root_node)
        toc = time.perf_counter()
        result.append(peak_value)
        result.append((toc - tic) * 1000)
        peak_value = peak_value + 1000
        del bst
    print_result('min_path.txt', result=result, unit='micros')


def max_report():
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        bst = Tree()
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter()
        bst.tree_max_path_length(root_node)
        toc = time.perf_counter()
        result.append(peak_value)
        result.append((toc - tic) * 1000)
        peak_value = peak_value + 1000
        del bst
    print_result('max_path.txt', result=result, unit='micros')


def ratio_report():
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        bst = Tree()
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter()
        bst.tree_ratio_length(root_node)
        toc = time.perf_counter()
        result.append(peak_value)
        result.append((toc - tic) * 1000)
        peak_value = peak_value + 1000
        del bst
    print_result('ratio.txt', result=result, unit='micros')


def delete_report():
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        bst = Tree()
        for i in range(0, peak_value):
            bst.tree_insert(random.randint(0, peak_value))
        tic = time.perf_counter_ns()
        bst.tree_delete(bst.tree_search(random.randint(0, peak_value)))
        toc = time.perf_counter_ns()
        result.append(peak_value)
        result.append((toc - tic) / 1000)
        peak_value = peak_value + 1000
        del bst
    print_result('delete.txt', result=result, unit='micros')


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

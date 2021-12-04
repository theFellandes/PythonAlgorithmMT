import time

from BinarySearchTree import Tree
import random


def main():
    bst = Tree()
    insert_report(bst)
    inorder_tree_walk_report(bst)
    search_report(bst)
    minimum_report(bst)
    min_report(bst)
    maximum_report(bst)
    max_report(bst)
    successor_report(bst)
    predecessor_report(bst)
    ratio_report(bst)
#     DELETE EKSİK


def insert_report(bst: Tree):
    peak_value = 1000
    tree_insert_time = []
    while peak_value <= 100_000:

        tic = time.perf_counter()
        for i in range(0, peak_value):
            bst.tree_insert(random.randint(0, peak_value))
        toc = time.perf_counter()
        tree_insert_time.append(peak_value)
        tree_insert_time.append(toc - tic)
        peak_value = peak_value + 1000
    print_result('insert.txt', result=tree_insert_time, unit='ms')


def inorder_tree_walk_report(bst: Tree):
    peak_value = 1000
    tree_time = []
    while peak_value <= 100_000:
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
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
    print_result('inorder_tree_walk.txt', result=tree_time, unit='ms')


def search_report(bst: Tree):
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        tic = time.perf_counter()
        root_node = bst.tree_search(root)
        toc = time.perf_counter()
        result.append(peak_value)
        result.append(toc - tic)
        peak_value = peak_value + 1000
    print_result('search.txt', result=result, unit='ms')


def minimum_report(bst: Tree):
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter()
        bst.tree_minimum(root_node)
        toc = time.perf_counter()
        result.append(peak_value)
        result.append(toc - tic)
        peak_value = peak_value + 1000
    print_result('minimum.txt', result=result, unit='ms')

def maximum_report(bst: Tree):
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter()
        bst.tree_maximum(root_node)
        toc = time.perf_counter()
        result.append(peak_value)
        result.append(toc - tic)
        peak_value = peak_value + 1000
    print_result('maximum.txt', result=result, unit='ms')


def successor_report(bst: Tree):
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter()
        bst.tree_successor(root_node)
        toc = time.perf_counter()
        result.append(peak_value)
        result.append(toc - tic)
        peak_value = peak_value + 1000
    print_result('successor.txt', result=result, unit='ms')


def predecessor_report(bst: Tree):
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
        root = 0
        for i in range(0, peak_value):
            if i == 0:
                root = random.randint(0, peak_value)
                bst.tree_insert(root)
            else:
                bst.tree_insert(random.randint(0, peak_value))
        root_node = bst.tree_search(root)
        tic = time.perf_counter()
        bst.tree_predecessor(root_node)
        toc = time.perf_counter()
        result.append(peak_value)
        result.append(toc - tic)
        peak_value = peak_value + 1000
    print_result('predecessor.txt', result=result, unit='ms')


def min_report(bst: Tree):
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
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
        result.append(toc - tic)
        peak_value = peak_value + 1000
    print_result('min.txt', result=result, unit='ms')


def max_report(bst: Tree):
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
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
        result.append(toc - tic)
        peak_value = peak_value + 1000
    print_result('max.txt', result=result, unit='ms')


def ratio_report(bst: Tree):
    peak_value = 1000
    result = []
    while peak_value <= 100_000:
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
        result.append(toc - tic)
        peak_value = peak_value + 1000
    print_result('ratio.txt', result=result, unit='ms')


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

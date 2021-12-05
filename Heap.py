import time


class Heap:
    size = 0

    @staticmethod
    def get_parent(index: int):
        """Returns the parent of the node"""
        return (index - 1) // 2

    @staticmethod
    def get_child(index: int, left: bool):
        """Returns the left child or right child by choosing according to bool"""
        if left:
            return 2 * index + 1
        return 2 * index + 2

    def max_heapify(self, arr: list, i: int, n: int):
        """Performs the max heapify operation to given indexed value and last index to
        perform the max heapify operation.
        i=starting index
        n=last index for max heapify"""
        left = self.get_child(i, True)
        right = self.get_child(i, False)

        if left <= n and arr[left] > arr[i]:
            largest = left
        else:
            largest = i

        if right <= n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.max_heapify(arr, largest, n)

    def build_max_heap(self, arr: list):
        """Builds the max heap"""
        n = len(arr) - 1
        for i in range(n//2, -1, -1):
            self.max_heapify(arr, i, n)

    def heapsort(self, arr: list):
        """Performs heapsort to the heap"""
        self.build_max_heap(arr)
        for i in range(len(arr) - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.max_heapify(arr, 0, i - 1)

    @staticmethod
    def heap_maximum(arr: list):
        return arr[0]

    def heap_extract_max(self, arr: list, n: int):
        """Pops the root from the heap"""
        if n < 1:
            Exception("heap underflow")
        maximum = arr[0]
        arr[0] = arr[n]
        self.max_heapify(arr, 0, n-1)
        arr.pop()
        return maximum

    def heap_increase_key(self, arr: list, i: int, key: int):
        if key < arr[i]:
            Exception("new key is smaller than current key")
        arr[i] = key
        while i > 0 and arr[self.get_parent(i)] < arr[i]:
            arr[i], arr[self.get_parent(i)] = arr[self.get_parent(i)], arr[i]
            i = self.get_parent(i)

    def max_heap_insert(self, arr: list, key: int, n: int):
        arr.append(-1)
        self.heap_increase_key(arr, n + 1, key)


def max_heapify_examples(heap: Heap):
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    arr2 = [16, 1, 11, 13, 8, 9, 3, 2, 8, 4]
    arr3 = [1, 14, 11, 13, 8, 9, 3, 2, 8, 4]

    print("arr: ")
    heap.max_heapify(arr=arr, i=1, n=len(arr) - 1)
    for i in arr:
        print(i, end=', ')
    print()
    print("--------------")

    print("arr2: ")
    heap.max_heapify(arr=arr2, i=1, n=len(arr2) - 1)
    for i in arr2:
        print(i, end=', ')
    print()
    print("--------------")

    print("arr3: ")
    heap.max_heapify(arr=arr3, i=0, n=len(arr3) - 1)
    for i in arr3:
        print(i, end=', ')
    print()
    print("--------------")


if __name__ == '__main__':
    heap = Heap()
    # max_heapify_examples(heap)
    arr = [5, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    arr2 = [5, 4, 10, 14, 7, 9]
    arr3 = [9, 3, 2, 8, 1]
    # heap.max_heapify(arr= arr, i= 1, n = len(arr) - 1)
    tic = time.perf_counter()
    heap.build_max_heap(arr)
    toc = time.perf_counter()
    print(arr, end=', ')
    print()
    print((toc - tic) * 1000)

    tic = time.perf_counter()
    heap.build_max_heap(arr2)
    toc = time.perf_counter()
    print(arr2, end=', ')
    print()
    print((toc - tic) * 1000)

    tic = time.perf_counter()
    heap.build_max_heap(arr3)
    toc = time.perf_counter()
    print(arr3, end=', ')
    print()
    print((toc - tic) * 1000)

    tic = time.perf_counter()
    temp = heap.heap_extract_max(arr, len(arr) - 1)
    toc = time.perf_counter()
    print(temp)
    print()
    print(arr, end=', ')
    print()
    print((toc - tic) * 1000)

    tic = time.perf_counter()
    temp = heap.heap_extract_max(arr2, len(arr2) - 1)
    toc = time.perf_counter()
    print(temp)
    print()
    print(arr2, end=', ')
    print()
    print((toc - tic) * 1000)

    tic = time.perf_counter()
    temp = heap.heap_extract_max(arr3, len(arr3) - 1)
    toc = time.perf_counter()
    print(temp)
    print()
    print(arr3, end=', ')
    print()
    print((toc - tic) * 1000)

    print("----###------")
    tic = time.perf_counter()
    print(heap.heap_maximum(arr))
    toc = time.perf_counter()
    print()
    print(arr, end=', ')
    print()
    print((toc - tic) * 1000)

    tic = time.perf_counter()
    print(heap.heap_maximum(arr2))
    toc = time.perf_counter()
    print()
    print(arr2, end=', ')
    print()
    print((toc - tic) * 1000)

    tic = time.perf_counter()
    print(heap.heap_maximum(arr3))
    toc = time.perf_counter()
    print()
    print(arr3, end=', ')
    print()
    print((toc - tic) * 1000)

    print("----@@@@@------")
    tic = time.perf_counter()
    print(heap.max_heap_insert(arr, 20, len(arr) - 1))
    toc = time.perf_counter()
    print()
    print(arr, end=', ')
    print()
    print((toc - tic) * 1000)

    tic = time.perf_counter()
    print(heap.max_heap_insert(arr2, 34, len(arr2) - 1))
    toc = time.perf_counter()
    print()
    print(arr2, end=', ')
    print()
    print((toc - tic) * 1000)

    tic = time.perf_counter()
    print(heap.max_heap_insert(arr3, 80, len(arr3) - 1))
    toc = time.perf_counter()
    print()
    print(arr3, end=', ')
    print()
    print((toc - tic) * 1000)

    print("--------------##---------------")

    tic = time.perf_counter()
    heap.heap_increase_key(arr, 3, 20)
    toc = time.perf_counter()
    print()
    print(arr, end=', ')
    print()
    print((toc - tic) * 1000)

    tic = time.perf_counter()
    heap.heap_increase_key(arr2, 2, 20)
    toc = time.perf_counter()
    print()
    print(arr2, end=', ')
    print()
    print((toc - tic) * 1000)

    tic = time.perf_counter()
    heap.heap_increase_key(arr3, 1, 45)
    toc = time.perf_counter()
    print()
    print(arr3, end=', ')
    print()
    print((toc - tic) * 1000)


    # tic = time.perf_counter()
    # heap.heapsort(arr)
    # toc = time.perf_counter()
    # print(arr, end=', ')
    # print()
    # print((toc - tic) * 1000)
    #
    # tic = time.perf_counter()
    # heap.heapsort(arr2)
    # toc = time.perf_counter()
    # print(arr2, end=', ')
    # print()
    # print((toc - tic) * 1000)
    #
    # tic = time.perf_counter()
    # heap.heapsort(arr3)
    # toc = time.perf_counter()
    # print(arr3, end=', ')
    # print()
    # print((toc - tic) * 1000)
    # print("-----------------------")
    # heap.max_heap_insert(arr, 13, len(arr) - 1)

    # print(temp)

class Heap:
    heap = []
    size = len(heap)

    def Heap(self):
        pass

    def Heap(self, heap_array):
        heap = heap_array

    @staticmethod
    def get_parent(index: int):
        return (index - 1) / 2

    @staticmethod
    def get_child(index: int, left: bool):
        if left:
            return 2 * index + 1
        return 2 * index + 2

    def max_heapify(self, arr: list, i: int, n: int):
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
        n = len(arr) - 1
        for i in range(n//2, 0, -1):
            self.max_heapify(arr, i, n)

    def heapsort(self, arr: list):
        self.build_max_heap(arr)
        for i in range(len(arr) - 1, 1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.max_heapify(arr, 0, i - 1)

    @staticmethod
    def heap_maximum(arr: list):
        return arr[0]

    def heap_extract_max(self, arr: list, n: int):
        if n < 1:
            Exception("heap underflow")
        maximum = arr[0]
        arr[0] = arr[n]
        self.max_heapify(arr, 0, n-1)
        return maximum

    def heap_increase_key(self, arr: list, i: int, key: int):
        if key < arr[i]:
            Exception("new key is smaller than current key")
        arr[i] = key
        while i > 1 and arr[self.get_parent(i)] < arr[i]:
            arr[i], arr[self.get_parent(i)] = arr[self.get_parent(i)], arr[i]
            i = self.get_parent(i)

    def max_heap_insert(self, arr: list, key: int, n: int):
        self.size += 1
        arr[self.size - 1] = - 1
        self.heap_increase_key(arr, n, key)

    def insert(self, value: int):
        self.heap[self.size - 1] = value
        self.build_max_heap(self.heap)

    def print_heap(self):
        for i in self.heap:
            print(i)


if __name__ == '__main__':
    heap = Heap()
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heap.max_heapify(arr= arr, i= 1, n = len(arr) - 1)
    for i in arr:
        print(i)

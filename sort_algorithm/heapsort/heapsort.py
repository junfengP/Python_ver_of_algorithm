#!/usr/bin/env python
# coding=utf-8
from test_data.create_random_data import log_time
from test_data.create_random_data import create_random_data
from test_data.create_random_data import read_random_data
from test_data.create_random_data import save_sorted


class Heap():
    LEFT = lambda self, i: i << 1
    RIGHT = lambda self, i: (i << 1) + 1
    PARENT = lambda self, i: i >> 1
    INFINITE_SMALL = -10001
    INFINITE_LARGE=10001
    def __init__(self, A):
        self.heap_size = 0
        self.A = A[:]

    @log_time
    def heapsort(self):
        self.build_max_heap()
        self.heap_size
        for i in range(len(self.A), 1, -1):  # 从len(B)到2
            temp = self.A[0]  # 交换第1个元素和第i个元素
            self.A[0] = self.A[i - 1]
            self.A[i - 1] = temp
            self.heap_size -= 1
            self.max_heaplify(1)
        return self.A

    def max_heaplify(self, i):
        L = self.LEFT(i)
        R = self.RIGHT(i)
        if L <= self.heap_size and self.A[L - 1] > self.A[i - 1]:  # 数组从0开始，数学模型从1开始,操作数组时，下标全部-1
            largest = L
        else:
            largest = i
        if R <= self.heap_size and self.A[R - 1] > self.A[largest - 1]:
            largest = R
        if largest != i:
            temp = self.A[i - 1]
            self.A[i - 1] = self.A[largest - 1]
            self.A[largest - 1] = temp
            self.max_heaplify(largest)

    def min_heaplify(self, i):
        L = self.LEFT(i)
        R = self.RIGHT(i)
        if L <= self.heap_size and self.A[L - 1] < self.A[i - 1]:  # 数组从0开始，数学模型从1开始,操作数组时，下标全部-1
            smallest = L
        else:
            smallest = i
        if R <= self.heap_size and self.A[R - 1] < self.A[smallest - 1]:
            smallest = R
        if smallest != i:
            temp = self.A[i - 1]
            self.A[i - 1] = self.A[smallest - 1]
            self.A[smallest - 1] = temp
            self.min_heaplify(smallest)

    def build_max_heap(self):
        self.heap_size = len(self.A)
        for i in range(len(self.A) / 2, 0, -1):  # 从len(A)/2 到 1
            self.max_heaplify(i)
        return self.A

    def build_min_heap(self):
        self.heap_size = len(self.A)
        for i in range(len(self.A) / 2, 0, -1):  # 从len(A)/2 到 1
            self.min_heaplify(i)
        return self.A

    def heap_maximum(self):
        return self.A[0]

    def heap_minimum(self):
        return self.A[0]

    def heap_extract_max(self):
        if self.heap_size < 1:
            raise Exception("heap underflow")
        maximum = self.A[0]
        self.A[0] = self.A[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heaplify(1)
        self.A.pop()  # 丢弃最后一个元素
        return maximum

    def heap_extract_min(self):
        if self.heap_size < 1:
            raise Exception("heap underflow")
        minimum = self.A[0]
        self.A[0] = self.A[self.heap_size - 1]
        self.heap_size -= 1
        self.min_heaplify(1)
        self.A.pop()  # 丢弃最后一个元素
        return minimum

    def heap_increase_key(self, i, key):
        if key < self.A[i - 1]:
            raise Exception('new key is smaller than current key')
        self.A[i - 1] = key
        while i > 1 and self.A[self.PARENT(i) - 1] < self.A[i - 1]:
            temp = self.A[i - 1]
            self.A[i - 1] = self.A[self.PARENT(i) - 1]
            self.A[self.PARENT(i) - 1] = temp
            i = self.PARENT(i)
        return self.A

    def heap_decrease_key(self, i, key):
        if key > self.A[i - 1]:
            raise Exception('new key is larger than current key')
        self.A[i - 1] = key
        while i > 1 and self.A[self.PARENT(i) - 1] > self.A[i - 1]:
            temp = self.A[i - 1]
            self.A[i - 1] = self.A[self.PARENT(i) - 1]
            self.A[self.PARENT(i) - 1] = temp
            i = self.PARENT(i)
        return self.A

    def max_heap_insert(self, key):
        self.heap_size += 1
        self.A.append(self.INFINITE_SMALL)
        self.heap_increase_key(self.heap_size, key)
        return self.A

    def min_heap_insert(self, key):
        self.heap_size += 1
        self.A.append(self.INFINITE_LARGE)
        self.heap_decrease_key(self.heap_size, key)
        return self.A

    def max_heap_delete(self,i):
        maximum=self.heap_maximum()
        self.heap_increase_key(i,maximum+1)
        self.heap_extract_max()
        return self.A

    def min_heap_delete(self,i):
        minimum=self.heap_maximum()
        self.heap_decrease_key(i,minimum-1)
        self.heap_extract_min()
        return self.A

    def get_heap(self):
        return self.A


def heap_test():
    data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap = Heap(data)
    print "最大堆:", heap.build_max_heap()
    print "最大元素:", heap.heap_maximum()
    print "取出最大元素:", heap.heap_extract_max()
    print "取出最大元素后的堆:", heap.get_heap()
    print "插入元素16后的堆", heap.max_heap_insert(16)
    print "将第二个元素提升到17:", heap.heap_increase_key(2, 17)
    print "删除第2个元素",heap.max_heap_delete(2)
    print "堆排序", heap.heapsort()

def heap_test2():
    data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap = Heap(data)
    print "最小堆:", heap.build_min_heap()
    print "最小元素:", heap.heap_minimum()
    print "取出最小元素:", heap.heap_extract_min()
    print "取出最小元素后的堆:", heap.get_heap()
    print "插入元素5后的堆", heap.min_heap_insert(5)
    print "将第二个元素降低到-1:", heap.heap_decrease_key(2, -1)
    print "删除第2个元素",heap.min_heap_delete(2)



def sort_test():
    numbers = 100000
    create_random_data(numbers)
    origin_data = read_random_data(numbers)
    heap = Heap(origin_data)
    sorted_data = heap.heapsort()
    save_sorted(sorted_data)
    print "排序前(前10个数据):\n", origin_data[:10]
    print "排序后(前10个数据):\n", sorted_data[:10]


if __name__ == '__main__':
    sort_test()
    heap_test()
    heap_test2()

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

    def __init__(self, A):
        self.heap_size = 0
        self.A = A[:]

    @log_time
    def heapsort(self):
        self.build_max_heap()
        heap_size = self.heap_size  # 保存 heap_size 等排序完后 恢复
        for i in range(len(self.A), 1, -1):  # 从len(B)到2
            temp = self.A[0]  # 交换第1个元素和第i个元素
            self.A[0] = self.A[i - 1]
            self.A[i - 1] = temp
            self.heap_size -= 1
            self.max_heaplify(1)
        self.heap_size = heap_size
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
        max = self.A[0]
        self.A[0] = self.A[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heaplify(1)
        self.A.pop()  # 丢弃最后一个元素
        return max

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

    def max_heap_insert(self, key):
        self.heap_size += 1
        pass

    def get_heap(self):
        return self.A


if __name__ == '__main__':
    # numbers = 10
    # create_random_data(numbers)
    # origin_data = read_random_data(numbers)
    # heap = Heap()
    # sorted_data = heap.heapsort(origin_data)
    # save_sorted(sorted_data)
    # print "排序前(前10个数据):\n", origin_data[:10]
    # print "排序后(前10个数据):\n", sorted_data[:10]
    data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap = Heap(data)
    print "最大堆:", heap.build_max_heap()
    print "最大元素:", heap.heap_maximum()
    print "取出最大元素:", heap.heap_extract_max()
    print "取出最大元素后的堆:", heap.get_heap()
    print "将第二个元素提升到17:", heap.heap_increase_key(2, 17)

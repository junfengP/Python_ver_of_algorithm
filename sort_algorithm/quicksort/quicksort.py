#!/usr/bin/env python
# coding=utf-8
from test_data.create_random_data import log_time
from test_data.create_random_data import create_random_data
from test_data.create_random_data import read_random_data
from test_data.create_random_data import save_sorted
import random


class Quicksort(object):
    @log_time
    def quicksort(self, A):
        B = A[:]  # 保护原始数据
        return self.sort(B, 0, len(B) - 1)

    def sort(self, A, p, r):
        if p < r:
            q = self.partition(A, p, r)
            self.sort(A, p, q - 1)
            self.sort(A, q + 1, r)
            return A

    def partition(self, A, p, r):
        x = A[r]  # 最后一个元素作为pivot
        i = p - 1  # 小于pivot的元素边界
        for j in range(p, r):  # 从p ,p+1,...,r-1
            if A[j] <= x:
                i += 1  # 边界扩张
                A[i], A[j] = A[j], A[i]  # 交换A[i]与A[j]
        # 交换pivot到中心
        A[r], A[i + 1] = A[i + 1], A[r]
        return i + 1


class Randomized_quicksort(Quicksort):
    # 重写sort,调用randomize_partition实现随机化快排
    def sort(self, A, p, r):
        if p < r:
            q = self.randomize_partition(A, p, r)
            self.sort(A, p, q - 1)
            self.sort(A, q + 1, r)
            return A

    def randomize_partition(self, A, p, r):
        i = random.randint(p, r)  # 随机选出pivot
        # 交换pivot至末尾 复用子类 partition
        A[r],A[i]=A[i],A[r]
        return self.partition(A, p, r)


@log_time
def list_sort(B):
    A = B[:]
    A.sort()
    return A


if __name__ == '__main__':
    numbers = 100000
    # create_random_data(numbers)
    # origin_data = read_random_data(numbers)
    origin_data = []
    for _ in range(0, numbers):
        origin_data.append(random.randint(-10000, 10000))
    quick = Quicksort()
    r_quick = Quicksort()
    # sorted_data = quick.quicksort(origin_data)
    r_sorted_data = r_quick.quicksort(origin_data)
    l_sorted_data = list_sort(origin_data)
    # save_sorted(r_sorted_data)
    print "排序前(前10个数据):\n", origin_data[:10]
    print "排序后(前10个数据):\n", r_sorted_data[:10]
    print "list排序后(前10个数据):\n", l_sorted_data[:10]

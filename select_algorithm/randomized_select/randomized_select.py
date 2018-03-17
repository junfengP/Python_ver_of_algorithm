#!/usr/bin/python3
from test_data.create_random_data import log_time
from test_data.create_random_data import create_random_data
from test_data.create_random_data import read_random_data
from test_data.create_random_data import save_sorted
import random
from sort_algorithm.quicksort.quicksort import Randomized_quicksort


class Randomized_select(Randomized_quicksort):
    def Randomized_select(self, B, p, r, i):
        A = B[:]  # 保护原始数据
        return self.select(A, p, r, i)

    def select(self, A, p, r, i):
        if p == r:
            return A[p]
        q = self.randomize_partition(A, p, r)
        k = q - p + 1
        if i == k:
            return A[q]
        elif i < k:
            return self.select(A, p, q - 1, i)
        else:
            return self.select(A, q + 1, r, i - k)


if __name__ == '__main__':
    numbers = 10
    create_random_data(numbers)
    origin_data = read_random_data(numbers)
    select = Randomized_select()
    sort = Randomized_quicksort()
    sorted_data = sort.quicksort(origin_data)
    print("原始数据", origin_data)
    print("排序后", sorted_data)
    print("选择最小元素", select.Randomized_select(origin_data, 0, len(origin_data) - 1, 1))
    print("选择最大元素", select.Randomized_select(origin_data, 0, len(origin_data) - 1, len(origin_data)))
    print("选择第n/2个数", select.Randomized_select(origin_data, 0, len(origin_data) - 1, len(origin_data) // 2))

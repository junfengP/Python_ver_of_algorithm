#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: junfeng
# @contact: junfeng_pan96@qq.com
# @file: fib_heap.py
# @time: 2018/4/10 14:44
# @desc:
from data_structure.binary_search_tree.binary_search_tree import BinaryTreeNode
from math import log2, sqrt
NEG_INFINITE=-1 #负无穷，这里实验数据全部大于0

class FibHeapNode(BinaryTreeNode):
    #    left  right 指向兄弟结点 ; p 指向父亲结点
    #    child  指向一个孩子结点
    #    degree 储存孩子数目
    #    mark   结点自从上一次成为另一个孩子的结点后，是否失去过孩子
    def __init__(self, key, st_info=None, left=None, right=None, p=None):
        if left is None:
            left = self
        if right is None:
            left = self
        BinaryTreeNode.__init__(self, key, st_info, left, right, p)
        self.degree = 0
        self.child = None
        self.mark = False


class FibHeap:

    def __init__(self):
        self.n = 0  # 结点数目
        self.min = None  # 最小结点

    def __insert2RootList(self, x):
        if self.min is None:  # 空堆
            self.min = x
            x.left = x
            x.right = x
        else:  # 结点x插入根堆中
            y = self.min.left  # min结点左边的结点y
            y.right = x  # 建立x与y的关系
            x.left = y
            x.right = self.min  # 建立x与min的关系
            self.min.left = x
            if x.key < self.min.key:  # 更新min结点
                self.min = x
        x.p = None

    def fib_heap_insert(self, x):
        if not isinstance(x, FibHeapNode):
            x = FibHeapNode(x)
        self.__insert2RootList(x)  # 插入堆根链表
        self.n += 1  # 结点数增加

    # 返回堆的最小值
    def get_minimum(self):
        return self.min

    # 堆中弹出最小值
    def fib_heap_extract_min(self):
        if self.n == 0:
            return None
        z = self.min  # 待弹出元素
        if z is not None:
            x = z.child  # 把z的孩子全部加入到堆根链表
            while z.degree:
                self.__insert2RootList(x)
                x = x.left
                z.degree -= 1

            # 从堆根链表中删除z结点
            z.left.right = z.right
            z.right.left = z.left
            if z == z.right:  # 空堆
                self.min = None
            else:
                self.min = z.right  # 没有必要是最小结点 consolidate会解决
                self.consolidate()
            self.n -= 1
        return z

    # 合并堆的根链表
    def consolidate(self):
        # 辅助数组A 记录根结点对应的度数的轨迹
        Dn = int(log2(self.n) // log2((1 + sqrt(5)) / 2))  # floor(log_fi(self.n))    fi=(1+sqrt(5))/2
        A = [None] * (Dn + 1)
        # 堆根链表所有结点 从min结点向左搜索到min.right；注意min结点在过程中会变化
        # endLocation记录终止位置min.right
        endLocation = self.min.right
        w = self.min
        while w != endLocation:
            x = w
            d = x.degree
            w = w.left  # 该结点后续可能成为其他结点孩子，所以必须提前取得其左边结点
            while A[d] is not None:
                y = A[d]  # 另一个结点，与x有相同数量的孩子
                if x.key > y.key:
                    x, y = y, x  # 交换两者保证 x.key < y.key
                self.fib_heap_link(y, x)  # 将y作为x的孩子
                A[d] = None
                d += 1
            A[d] = x
        x = w
        d = x.degree
        while A[d] is not None:
            y = A[d]  # 另一个结点，与x有相同数量的孩子
            if x.key > y.key:
                x, y = y, x  # 交换两者保证 x.key < y.key
            self.fib_heap_link(y, x)  # 将y作为x的孩子
            A[d] = None
            d += 1
        A[d] = x

        # 重建堆根链表
        self.min = None
        for i in range(0, Dn + 1):  # 0 to Dn
            if A[i] is not None:
                self.__insert2RootList(A[i])

    # 将y变成x的孩子
    def fib_heap_link(self, y, x):
        # 将y从根堆中移除
        y.left.right = y.right
        y.right.left = y.left
        if x.child is None:  # x无孩子
            x.child = y
            y.left = y
            y.right = y
        else:
            # 将y添加到x.child的左边
            a = x.child
            b = x.child.left
            # 建立x.child与y的关系
            a.left = y
            y.right = a
            # 建立x.child.left与y的关系
            b.right = y
            y.left = b
        y.p = x
        x.degree += 1
        y.mark = False

    def fib_heap_decrease_key(self, x, k):
        if k > x.key:
            raise ValueError("k is bigger than key!")
        x.key = k
        y = x.p
        if y is not None and x.key < y.key:  # 孩子比父亲小 ，违反最小堆
            self.__cut(x, y)
            self.__cascading_cut(y)
        if x.key < self.min.key:
            self.min = x

    def __cut(self, x, y):
        # 将y的孩子 分离出来，加入到堆根链表中
        if y.degree == 1:
            y.child = None
        else:
            if y.child == x:  # 如果y的孩子指针 指向x
                y.child = x.left
            else:  # 否则不用改变
                pass
            x.left.right = x.right  # x的兄弟结点
            x.right.left = x.left
        y.degree -= 1
        self.__insert2RootList(x)
        x.mark = False

    def __cascading_cut(self, y):
        z = y.p
        if z is not None:
            if y.mark == False:
                y.mark = True
            else:
                self.__cut(y, z)
                self.__cascading_cut(z)

    def fib_heap_delete(self,x):
        self.fib_heap_decrease_key(x,NEG_INFINITE) #假定-1是负无穷
        self.fib_heap_extract_min()

# 类外函数
# 联合两个斐波那契堆
def fib_heap_union(H1, H2):
    # 合并两个斐波那契堆
    if not (isinstance(H1, FibHeap) and isinstance(H2, FibHeap)):
        raise TypeError("Input must be FibHeap!")
    if H1.min is None:  # 若其中一个是空堆，无需合并
        return H2
    if H2.min is None:
        return H1
    H = FibHeap()
    H.min = H1.min
    # 合并H1和H2的根堆
    # H1.min的右边断开与 H2.min左边断开 合并成新的双向链表
    H1_right = H1.min.right
    H2_left = H2.min.left
    # 建立H1.min与H2.min关系
    H1.min.right = H2.min
    H2.min.left = H1.min
    # 建立H1_right与H2_left 关系
    H1_right.left = H2_left
    H2_left.right = H1_right
    if H1.min.key > H2.min.key:
        H.min = H2.min
    H.n = H1.n + H2.n
    return H


if __name__ == '__main__':
    heap = FibHeap()
    heap.fib_heap_insert(3)
    heap.fib_heap_insert(21)
    heap.fib_heap_insert(17)
    heap.fib_heap_insert(15)
    heap.fib_heap_insert(30)
    heap.fib_heap_insert(45)
    #print(heap.fib_heap_extract_min())
    heap.fib_heap_delete(heap.get_minimum())
    print("hello")

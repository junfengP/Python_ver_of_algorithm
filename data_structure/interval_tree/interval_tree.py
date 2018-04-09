#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: junfeng
# @contact: junfeng_pan96@qq.com
# @file: interval_tree.py
# @time: 2018/4/9 10:39
# @desc:

from data_structure.red_black_tree.red_black_tree import RBTreeNode, RBTreeColor, RBTree


class IntervalData:
    def __init__(self, low, high):
        self.low = low
        self.high = high


class IntervalNode(RBTreeNode):
    def __init__(self, low, high, st_info=None):
        if low > high:
            raise ValueError("high point must be higher than low point!")
        else:
            RBTreeNode.__init__(self, low, st_info)
            self.data = IntervalData(low, high)
            self.max = self.data.high

    def __repr__(self):
        return "color:{0},low:{1},high:{2},max:{3},satelite_info:{4}".format(
            "black" if self.color == self.BLACK else "red", str(self.data.low),
            str(self.data.high), str(self.max), str(self.st_info))


class IntervalTree(RBTree):
    def __init__(self):
        self.nil = IntervalNode(low=-1, high=-1)
        self.root = self.nil

    def interval_search(self, i):
        x = self.root
        while x != self.nil and (i.high < x.data.low or i.low > x.data.high):
            if x.left != self.nil and x.left.max >= i.low:
                x = x.left
            else:
                x = x.right
        return x

    def interval_insert(self, x):
        if not isinstance(x, IntervalNode):
            raise ValueError("Input must be an interval node!")
        self.rb_insert(x)
        self.interval_max_fixup(x)
        self.rb_insert_fixup(x)

    def left_rotate(self, x):
        y = RBTree.left_rotate(self, x)
        x.max = max(x.data.high, max(x.left.max, x.right.max))
        y.max = max(y.data.high, max(y.left.max, y.right.max))
        return y

    def right_rotate(self, y):
        x = RBTree.right_rotate(self, y)
        y.max = max(y.data.high, max(y.left.max, y.right.max))
        x.max = max(x.data.high, max(x.left.max, x.right.max))
        return x

    def interval_max_fixup(self, x):
        while x != self.nil:
            x.max = max(x.data.high, max(x.left.max, x.right.max))
            x = x.p

    def interval_delete(self,z):
        self.rb_delete(z)

    def rb_transplant(self, u, v):
        RBTree.rb_transplant(self,u,v)
        self.interval_max_fixup(v)



if __name__ == '__main__':
    tree = IntervalTree()
    tree.interval_insert(IntervalNode(16, 21))
    tree.interval_insert(IntervalNode(8, 9))
    tree.interval_insert(IntervalNode(25, 30))
    tree.interval_insert(IntervalNode(5, 8))
    tree.interval_insert(IntervalNode(17, 19))
    tree.interval_insert(IntervalNode(15, 23))
    tree.interval_insert(IntervalNode(26, 26))
    tree.interval_insert(IntervalNode(0, 3))
    tree.interval_insert(IntervalNode(6, 10))
    tree.interval_insert(IntervalNode(19, 20))
    tree.inorder_tree_walk(tree.get_root())
    print("root is :", tree.get_root())
    print("--------------------divide line--------------------------")
    tree.interval_delete(tree.interval_search(IntervalData(22,25)))
    tree.interval_delete(tree.get_root())
    tree.inorder_tree_walk(tree.get_root())
    print("root is :", tree.get_root())
#!/usr/bin/python3
from data_structure.red_black_tree.red_black_tree import RBTreeNode, RBTree, RBTreeColor


class OSTreeNode(RBTreeNode):
    def __init__(self, value, st_info=None, color=RBTreeColor.BLACK, left=None, right=None, p=None, size=0):
        RBTreeNode.__init__(self, value, st_info, color, left, right, p)
        self.size = size

    def __repr__(self):
        return "value:{0},color:{1},size:{2}".format(
            str(self.value),
            "black" if self.color == self.BLACK else "red",
            self.size)


class OSTree(RBTree):

    def __init__(self):
        self.nil = OSTreeNode(value=None)
        self.root = self.nil

    def os_select(self, x, i):
        r = x.left.size + 1
        if i == r:
            return x
        elif i < r:
            return self.os_select(x.left, i)
        else:
            return self.os_select(x.right, i - r)

    def os_rank(self, x):
        r = x.left.size + 1
        y = x
        while y != self.root:
            if y == y.p.right:
                r += y.p.left.size + 1
            y = y.p
        return r

    def os_insert(self, z):
        if not isinstance(z, OSTreeNode):
            z = OSTreeNode(z, color=self.RED, size=1)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            x.size += 1  # 下降规模扩张
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = self.RED
        self.rb_insert_fixup(z)

    def os_size_fixup(self, z, dir):
        while z.p != self.nil:
            z.p.size += dir
            z = z.p

    def os_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.os_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.os_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            x = y.right
            if y.p != z:
                self.os_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
                self.os_size_fixup(z, +1)
            self.os_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
            y.size = y.left.size + y.right.size + 1
        if y_original_color == self.BLACK:
            self.rb_delete_fixup(x)

    def os_transplant(self, u, v):
        self.rb_transplant(u, v)
        self.os_size_fixup(v, -1)

    def left_rotate(self, x):
        y = RBTree.left_rotate(self, x)
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

    def right_rotate(self, y):
        x = RBTree.right_rotate(self, y)
        x.size = y.size
        y.size = y.left.size + y.right.size + 1


if __name__ == '__main__':
    ost = OSTree()
    for i in range(1, 10):
        ost.os_insert(i)
    print("中序遍历\n")
    ost.inorder_tree_walk(ost.get_root())
    print("root:", ost.get_root())
    ost.os_delete(ost.tree_search(ost.get_root(), 7))
    ost.os_delete(ost.tree_search(ost.get_root(), 4))
    print("中序遍历\n")
    ost.inorder_tree_walk(ost.get_root())
    print("选取第6个元素", ost.os_select(ost.get_root(), 6))
    print("root的秩", ost.os_rank(ost.get_root()))

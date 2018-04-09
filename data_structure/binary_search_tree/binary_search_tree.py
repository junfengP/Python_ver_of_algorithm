#!/usr/bin/python3

class Tree_Node:
    def __init__(self, value, st_info=None, left=None, right=None, p=None):
        self.value = value
        self.left = left
        self.right = right
        self.p = p
        self.st_info = st_info  # 卫星数据

    def __repr__(self):
        return str(self.value)


class BST:

    def __init__(self):
        self.nil = Tree_Node(value=None)
        self.root = self.nil

    def get_root(self):
        return self.root

    def inorder_tree_walk(self, x):
        if x != self.nil:
            self.inorder_tree_walk(x.left)
            print(x)
            self.inorder_tree_walk(x.right)

    def tree_search(self, x, k):
        if x == self.nil or k == x.value:
            return x
        if k < x.value:
            return self.tree_search(x.left, k)
        else:
            return self.tree_search(x.right, k)

    def iterative_tree_search(self, x, k):
        while x != self.nil and k != x.value:
            if k < x.value:
                x = x.left
            else:
                x = x.right
        return x

    def tree_minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def tree_maximum(self, x):
        while x.right != self.nil:
            x = x.right
        return x

    def tree_successor(self, x):
        if x.right != self.nil:
            return self.tree_minimum(x.right)
        y = x.p
        while y != self.nil and x == y.right:
            x = y
            y = y.p
        return y

    def tree_predecessor(self, x):
        if x.left != self.nil:
            return self.tree_maximum(x.left)
        y = x.p
        while y != self.nil and x == y.left:
            x = y
            y = y.p
        return y

    def tree_insert(self, z):
        if not isinstance(z, Tree_Node):
            z = Tree_Node(z)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
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

    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v == self.nil:
            v.p = u.p

    def tree_delete(self, z):
        if z.left == self.nil:
            self.transplant(z, z.right)
        elif z.right == self.nil:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y


if __name__ == '__main__':
    bst = BST()
    for i in range(10, 1, -1):
        bst.tree_insert(i)
    print("树的最小值", bst.tree_minimum(bst.get_root()))
    print("树的最大值", bst.tree_maximum(bst.get_root()))
    print("删除节点4")
    bst.tree_delete(bst.tree_search(bst.get_root(), 4))
    print("节点5的前驱", bst.tree_predecessor(bst.tree_search(bst.get_root(), 5)))
    print("节点5的后继", bst.tree_successor(bst.tree_search(bst.get_root(), 5)))

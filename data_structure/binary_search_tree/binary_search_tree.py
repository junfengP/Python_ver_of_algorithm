#!/usr/bin/env python
# coding=utf-8


class Tree_Node():
    def __init__(self, value, left=None, right=None, p=None):
        self.value = value
        self.left = left
        self.right = right
        self.p = p

    def __repr__(self):
        return str(self.value)


class BST():

    def __init__(self):
        self.T_root = None

    def get_root(self):
        return self.T_root

    def inorder_tree_walk(self, x):
        if x != None:
            self.inorder_tree_walk(x.left)
            print x.value
            self.inorder_tree_walk(x.right)

    def tree_search(self, x, k):
        if x == None or k == x.value:
            return x
        if k < x.value:
            return self.tree_search(x.left, k)
        else:
            return self.tree_search(x.right, k)

    def iterative_tree_search(self, x, k):
        while x != None and k != x.value:
            if k < x.value:
                x = x.left
            else:
                x = x.right
        return x

    def tree_minimum(self, x):
        while x.left != None:
            x = x.left
        return x

    def tree_maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def tree_successor(self, x):
        if x.right != None:
            return self.tree_minimum(x.right)
        y = x.p
        while y != None and x == y.right:
            x = y
            y = y.p
        return y

    def tree_predecessor(self, x):
        if x.left != None:
            return self.tree_maximum(x.left)
        y = x.p
        while y != None and x == y.left:
            x = y
            y = y.p
        return y

    def tree_insert(self, z):
        if not isinstance(z, Tree_Node):
            z = Tree_Node(z)
        y = None
        x = self.T_root
        while x != None:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.T_root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        if u.p == None:
            self.T_root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p

    def tree_delete(self, z):
        if z.left==None:
            self.transplant(z,z.right)
        elif z.right==None:
            self.transplant(z,z.left)
        else:
            y=self.tree_minimum(z.right)
            if y.p!=z:
                self.transplant(y,y.right)
                y.right=z.right
                y.right.p=y
            self.transplant(z,y)
            y.left=z.left
            y.left.p=y


if __name__ == '__main__':
    bst = BST()
    for i in range(10, 1, -1):
        bst.tree_insert(i)
    print "树的最小值", bst.tree_minimum(bst.get_root())
    print "树的最大值", bst.tree_maximum(bst.get_root())
    print "删除节点4"
    bst.tree_delete(bst.tree_search(bst.get_root(),4))
    print "节点5的前驱", bst.tree_predecessor(bst.tree_search(bst.get_root(), 5))
    print "节点5的后继", bst.tree_successor(bst.tree_search(bst.get_root(), 5))


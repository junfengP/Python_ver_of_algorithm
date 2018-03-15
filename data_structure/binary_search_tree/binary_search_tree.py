#!/usr/bin/env python
# coding=utf-8


class Tree_Node():
    def __init__(self, value, LNode=None, RNode=None, PNode=None):
        self.value = value
        self.LNode = LNode
        self.RNode = RNode
        self.PNode = PNode

    def __repr__(self):
        return str(self.value)


class BST():

    def __init__(self):
        self.T_root = None

    def get_root(self):
        return self.T_root

    def inorder_tree_walk(self, x):
        if x != None:
            self.inorder_tree_walk(x.LNode)
            print x.value
            self.inorder_tree_walk(x.RNode)

    def tree_search(self, x, k):
        if x == None or k == x.value:
            return x
        if k < x.value:
            return self.tree_search(x.LNode, k)
        else:
            return self.tree_search(x.RNode, k)

    def iterative_tree_search(self, x, k):
        while x != None and k != x.value:
            if k < x.value:
                x = x.LNode
            else:
                x = x.RNode
        return x

    def tree_minimum(self, x):
        while x.LNode != None:
            x = x.LNode
        return x

    def tree_maximum(self, x):
        while x.RNode != None:
            x = x.RNode
        return x

    def tree_successor(self, x):
        if x.RNode != None:
            return self.tree_minimum(x.RNode)
        y = x.PNode
        while y != None and x == y.RNode:
            x = y
            y = y.PNode
        return y

    def tree_predecessor(self, x):
        if x.LNode != None:
            return self.tree_maximum(x.LNode)
        y = x.PNode
        while y != None and x == y.LNode:
            x = y
            y = y.PNode
        return y

    def tree_insert(self, z):
        if not isinstance(z, Tree_Node):
            z = Tree_Node(z)
        y = None
        x = self.T_root
        while x != None:
            y = x
            if z.value < x.value:
                x = x.LNode
            else:
                x = x.RNode
        z.PNode = y
        if y == None:
            self.T_root = z
        elif z.value < y.value:
            y.LNode = z
        else:
            y.RNode = z

    def transplant(self, u, v):
        if u.PNode == None:
            self.T_root = v
        elif u == u.PNode.LNode:
            u.PNode.LNode = v
        else:
            u.PNode.RNode = v
        if v != None:
            v.PNode = u.PNode

    def tree_delete(self, z):
        if z.LNode==None:
            self.transplant(z,z.RNode)
        elif z.RNode==None:
            self.transplant(z,z.LNode)
        else:
            y=self.tree_minimum(z.RNode)
            if y.PNode!=z:
                self.transplant(y,y.RNode)
                y.RNode=z.RNode
                y.RNode.PNode=y
            self.transplant(z,y)
            y.LNode=z.LNode
            y.LNode.PNode=y


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


#!/usr/bin/env python
# coding=utf-8
from data_structure.binary_search_tree.binary_search_tree import BST
class RBTreeColor():
    BLACK = 1
    RED = 0


class RBTReeNode(RBTreeColor):
    def __init__(self, value, color=RBTreeColor.BLACK, left=None, right=None, p=None):
        self.value = value
        self.left = left
        self.right = right
        self.p = p
        self.color = color

    def __repr__(self):
        return "value:{0},color:{1}".format(
            str(self.value),
            "black" if self.color == self.BLACK else "red")


class RBTree(RBTreeColor,BST):
    def __init__(self):
        self.nil = RBTReeNode(value=None)
        self.root = self.nil

    def left_rotate(self, x):
        y = x.right  # page 177
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.p = y
        x.p = y.p
        if y.p == self.nil:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        x.right = y
        y.p = x

    def rb_insert(self, z):
        if not isinstance(z, RBTReeNode):
            z = RBTReeNode(z, color=self.RED)
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
        z.color = self.RED
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z):
        while z.p.color == self.RED:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == self.RED:  # case 1
                    z.p.color = self.BLACK
                    y.color = self.BLACK
                    z.p.p.color = self.RED
                    z = z.p.p
                elif z == z.p.right:  # case 2
                    z == z.p
                    self.left_rotate(z)
                else:  # case 3
                    z.p.color = self.BLACK
                    z.p.p.color = self.RED
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == self.RED:
                    z.p.color = self.BLACK
                    y.color = self.BLACK
                    z.p.p.color = self.RED
                    z = z.p.p
                elif z == z.p.left:
                    z == z.p
                    self.right_rotate(z)
                else:
                    z.p.color = self.BLACK
                    z.p.p.color = self.RED
                    self.left_rotate(z.p.p)
        self.root.color = self.BLACK

    def rb_transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def rb_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == self.BLACK:
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x):
        while x != self.root and x.color == self.BLACK:
            if x == x.p.left:
                w = x.p.right
                if w.color == self.RED:
                    w.color = self.BLACK
                    x.p.color = self.RED
                    self.left_rotate(x.p)
                    w=x.p.right
                if w.left.color==self.BLACK and w.right.color==self.BLACK:
                    w.color=self.RED
                    x=x.p
                elif w.right.color==self.BLACK:
                    w.left.color=self.BLACK
                    w.color=self.RED
                    self.right_rotate(w)
                    w=x.p.right
                else:
                    w.color=x.p.color
                    x.p.color=self.BLACK
                    w.right.color=self.BLACK
                    self.left_rotate(x.p)
                    x=self.root
            else:
                w = x.p.left
                if w.color == self.RED:
                    w.color = self.BLACK
                    x.p.color = self.RED
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.color == self.BLACK and w.left.color == self.BLACK:
                    w.color = self.RED
                    x = x.p
                elif w.left.color == self.BLACK:
                    w.right.color = self.BLACK
                    w.color = self.RED
                    self.left_rotate(w)
                    w = x.p.left
                else:
                    w.color = x.p.color
                    x.p.color = self.BLACK
                    w.left.color = self.BLACK
                    self.right_rotate(x.p)
                    x = self.root
        x.color=self.BLACK



if __name__ == "__main__":
    rb = RBTree()
    for i in range(1, 10):
        rb.rb_insert(i)
    print "root:", rb.get_root()
    print "inorder:\n", rb.inorder_tree_walk(rb.get_root())
    print "minimum:",rb.tree_minimum(rb.get_root())
    print "maximum:",rb.tree_maximum(rb.get_root())
    print "search 5:",rb.tree_search(rb.get_root(),5)
    rb.rb_delete(rb.tree_search(rb.get_root(),4))
    print "root:", rb.get_root()
    print "root successor:", rb.tree_successor(rb.get_root())
    print "root predecessor:", rb.tree_predecessor(rb.get_root())
    print "inorder:\n", rb.inorder_tree_walk(rb.get_root())
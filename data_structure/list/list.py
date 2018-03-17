#!/usr/bin/python3
from test_data.create_random_data import log_time
from test_data.create_random_data import create_random_data
from test_data.create_random_data import read_random_data
from test_data.create_random_data import save_sorted


class Node:
    def __init__(self, value, nextnode=None, prevnode=None):
        self.value = value
        self.pNode = prevnode
        self.nextnode = nextnode

    def __repr__(self):
        return str(self.value)


class Linked_list():
    def __init__(self):
        self.nil = Node(value=None)
        self.nil.prevnode = self.nil
        self.nil.nextnode = self.nil

    def list_insert(self, x):
        if isinstance(x, Node):
            pass
        else:
            x = Node(value=x)
        x.nextnode = self.nil.nextnode
        self.nil.nextnode.prevnode = x
        self.nil.nextnode = x
        x.prevnode = self.nil

    def list_search(self, k):
        x = self.nil.nextnode
        while x != self.nil and x.value != k:
            x = x.nextnode
        return x


if __name__ == '__main__':
    ls = Linked_list()
    for i in range(1, 10):
        ls.list_insert(i)
    print(ls.list_search(5))

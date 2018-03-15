#!/usr/bin/env python
# coding=utf-8
from test_data.create_random_data import log_time
from test_data.create_random_data import create_random_data
from test_data.create_random_data import read_random_data
from test_data.create_random_data import save_sorted
class Node():
    def __init__(self,value,nNode=None,pNode=None):
        self.value=value
        self.pNode=pNode
        self.nNode=nNode

    def __repr__(self):
        return str(self.value)

class Linked_list():

    def __init__(self):
        self.nil=Node(value=None)
        self.nil.pNode=self.nil
        self.nil.nNode=self.nil

    def list_insert(self,x):
        if isinstance(x,Node):
            pass
        else:
            x=Node(value=x)
        x.nNode=self.nil.nNode
        self.nil.nNode.pNode=x
        self.nil.nNode=x
        x.pNode=self.nil

    def list_search(self,k):
        x=self.nil.nNode
        while x!=self.nil and x.value!=k:
            x=x.nNode
        return x


if __name__=='__main__':
    ls=Linked_list()
    for i in range(1,10):
        ls.list_insert(i)
    print ls.list_search(1)
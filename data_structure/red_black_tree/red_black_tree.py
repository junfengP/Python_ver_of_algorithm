#!/usr/bin/env python
# coding=utf-8

class Tree_Node():
    def __init__(self, value, left=None, right=None, p=None):
        self.value = value
        self.left=left
        self.right=right
        self.p=p
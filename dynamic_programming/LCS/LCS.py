#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: junfeng
# @contact: junfeng_pan96@qq.com
# @file: LCS.py
# @time: 2018/3/19 11:14
# @desc:
import pprint


class LCS:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def LCS_length(self):
        m = len(self.x)
        n = len(self.y)
        # c = [[0] * (n+1)] * (m+1)
        c = [[0 for i in range(n + 1)] for i in range(m + 1)]

        for i in range(1, m + 1):  # from 1 to m
            for j in range(1, n + 1):  # from 1 to n
                if self.x[i - 1] == self.y[j - 1]:  # array start with 0
                    c[i][j] = c[i - 1][j - 1] + 1
                elif c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                else:
                    c[i][j] = c[i][j - 1]
        self.c = c
        return self.c

    def print_lcs(self, i, j):
        if i == 0 or j == 0:
            return
        if self.x[i - 1] == self.y[j - 1]:
            self.print_lcs(i - 1, j - 1)
            print(x[i - 1], end="")
        elif c[i - 1][j] >= c[i][j - 1]:
            self.print_lcs(i - 1, j)
        else:
            self.print_lcs(i, j - 1)


if __name__ == '__main__':
    x = 'ABCBDAB'
    y = 'BDCABA'
    lcs = LCS(x, y)
    c = lcs.LCS_length()
    # pprint.pprint(c)
    lcs.print_lcs(len(x), len(y))

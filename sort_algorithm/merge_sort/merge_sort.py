#!/usr/bin/env python
#coding=utf-8
from test_data.create_random_data import log_time
from test_data.create_random_data import create_random_data
from test_data.create_random_data import read_random_data
from test_data.create_random_data import save_sorted
class Merge_sort():
    @log_time
    def merge_sort(self,A):
        B=A[:] #不在原数据上改动
        return self.sort(B,0,len(B)-1)


    def sort(self,A,p,r):  #对 A[p...r]进行归并排序
        if p<r:
            q=(p+r)/2            #将A[p...r]分成两个子数组
            self.sort(A,p,q)   #对子数组进行归并排序
            self.sort(A,q+1,r)
            self.merge(A,p,q,r)  #合并子数组
            return A

    def merge(self,A,p,q,r):
        INFINITE_MAX=10001 #极大值 标志位
        n1=q-p+1 #左半数组长度
        n2=r-q  #右半数组长度
        L=[]
        R=[]
        for i in range(0,n1):
            L.append(A[p+i])
        for j in range(0,n2):
            R.append(A[q+j+1])
        L.append(INFINITE_MAX)
        R.append(INFINITE_MAX)
        i=0
        j=0
        for k in range(p,r+1):
            if L[i]<R[j]:
                A[k]=L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1

if __name__=='__main__':
    numbers = 100000
    create_random_data(numbers)
    origin_data = read_random_data(numbers)
    merge=Merge_sort()
    sorted_data=merge.merge_sort(origin_data)
    save_sorted(sorted_data)
    print "排序前(前10个数据):\n", origin_data[:10]
    print "排序后(前10个数据):\n", sorted_data[:10]

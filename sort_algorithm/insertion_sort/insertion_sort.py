#!/usr/bin/env python
#coding=utf-8
from test_data.create_random_data import log_time
from test_data.create_random_data import create_random_data
from test_data.create_random_data import read_random_data
#插入排序法，从小到大排序
@log_time
def insertion_sort(array):
    n=len(array)
    if n==0 :
        return None
    for i in range(1,n): #第二个元素开始
        temp=array[i]
        moved_flag=0
        for j in range(i-1,-1,-1): # j 从 [i-1, ...,0]
            if temp < array[j]:
                moved_flag=1
                array[j+1]=array[j]
            else:
                break
        if moved_flag:
            if temp<array[j]:
                array[j] = temp
            else:
                array[j+1]=temp
    return array

if __name__=='__main__':
    numbers=100000
    create_random_data(numbers)
    data=read_random_data(numbers)
    insertion_sort(data)
    with open('sorted_%s.txt'%numbers,'w') as f:
        for rst in data:
            f.write(str(rst)+'\n')
    #print '排序后:\n',data
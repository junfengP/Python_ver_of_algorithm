#!/usr/bin/env python
#coding=utf-8
import random
import time

# 装饰器，记录函数运行时间
def log_time(func):
    def wrapper(*args, **kwargs):
        startTime=time.time()
        func(*args, **kwargs)
        endTime=time.time()
        msecs=(endTime-startTime)*1000
        print func.__name__,' runtime is: ',msecs,' ms'
    return wrapper

#   创建numbers个随机数到文本文件，随机数范围(-10000,10000)
@log_time
def create_random_data(numbers):
    with open('random_int_%s.txt' % numbers, 'w') as f:
        for i in range(1,numbers+1):
            f.write(str(random.randint(-10000,10000))+'\n')
			
#	从文本文件读取numbers个随机数文件，numbers必须和生成的随机数数量相同
def read_random_data(numbers):
    data=[]#结果储存在这里
    with open('random_int_%s.txt' % numbers, 'r') as f:
        temp=f.readline()
        while temp:
            data.append(int(temp.strip('\n')))
            temp=f.readline()
    return data



if __name__=='__main__':
    create_random_data(1000000)
    read_random_data(1000000)


#!/usr/bin/python
# -*- coding:utf-8 -*-
# date:2019-06-23

def maxSubSum(array):
    length = len(array)
    maxSum = 0
    for(i=0;i<length;i++):
        thisSum += array[i]
        if thisSum < 0:
            thisSum = 0
        elif (thisSum > maxSum):
            maxSum = thisSum
    
    return maxSum


def main():
    array = [1,-1,3,-4,7,8,-2,9]
    maxSubsum(array)


if __name__ == "__main__":
    main()
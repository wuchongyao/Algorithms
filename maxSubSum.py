#!/usr/bin/python
# -*- coding:utf-8 -*-
# date:2019-06-23

def maxSubSum(array):
    thisSum = 0
    length = len(array)
    maxSum = 0
    for i in range(length):
        thisSum += array[i]
        if thisSum < 0:
            thisSum = 0
        elif (thisSum > maxSum):
            maxSum = thisSum
    
    return maxSum


def main():
    array = [1,-1,3,-4,7,8,-2,9]
    print(maxSubSum(array))


if __name__ == "__main__":
    main()
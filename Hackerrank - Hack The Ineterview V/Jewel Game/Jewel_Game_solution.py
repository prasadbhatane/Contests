#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING jewels as parameter.
#
class Stack:
    def __init__(self):
        self.items = []
        self.length = 0
        
    def push(self, data):
        self.items.append(data)
        self.length += 1
        
    def pop(self):
        self.length -= 1
        return self.items.pop()
        
    def top(self):
        return self.items[-1]
    
    def is_empty(self):
        return (self.length == 0)
    
    def print_stack(self):
        print(self.items)
    
        
        
def getMaxScore(jewels):
    # Write your code here
    st = Stack()
    pop_flag = False
    score = 0
    for i in jewels:
        #print(st.print_stack())
        if st.is_empty():
            st.push(i)
        elif not st.is_empty():
            if st.top() == i:
                prev_pop = st.pop()
                score += 1
            else:
                st.push(i)
                
    return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        jewels = input()

        ans = getMaxScore(jewels)

        fptr.write(str(ans) + '\n')

    fptr.close()
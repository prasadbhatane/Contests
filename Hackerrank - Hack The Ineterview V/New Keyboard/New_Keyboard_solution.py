#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'receivedText' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING S as parameter.
#
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return
        
    def get_size(self):
        return len(self.items)
    
    def is_empty(self):
        return (len(self.items) == 0)
    
    def peek_or_top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"
    
    def print_stack(self):
        print(self.items)
        
    def get_stack(self):
        return self.items

class ThreeStack:
    def __init__(self):
        self.end_stack = Stack()
        self.h1_stack = Stack()
        self.h2_stack = Stack()
        
    def pop(self, _from):
        if _from == 'end':
            if not self.end_stack.is_empty():
                self.end_stack.pop()
            else:
                self.h2_to_end()
                self.end_stack.pop()
        elif _from == 'home' : self.h1_stack.pop()
        return
    
    def push(self, item, _to):
        if _to == 'end' : self.end_stack.push(item)
        elif _to == 'home' : self.h1_stack.push(item)
        return
    
    def h1_to_h2(self):
        while not self.h1_stack.is_empty():
            self.h2_stack.push(self.h1_stack.pop())
        return
    
    def h2_to_end(self):
        while not self.h2_stack.is_empty():
            self.end_stack.push(self.h2_stack.pop())
        return
    
    def combine_all(self):
        self.h1_to_h2()
        msg = self.h2_stack.get_stack()[::-1] + self.end_stack.get_stack()
        return ("".join(msg))
    
    def show_all3(self):
        print("End : ", end="")
        self.end_stack.print_stack()
        print("H1 : ", end="")
        self.h1_stack.print_stack()
        print("H2 : ", end="")
        self.h2_stack.print_stack()
        
def receivedText(S):
    # WRITE DOWN YOUR CODE HERE
    st = ThreeStack()
    Home = False
    End = True
    Num_lock = False
    for i in S:
        if not (i.isnumeric() and Num_lock):
            if i == '<':
                st.h1_to_h2()
                Home = True
                End = False
            elif i == '>':
                st.h1_to_h2()
                Home = False
                End = True
            elif i == '*':
                if Home:
                    st.pop('home')
                elif End:
                    st.pop('end')
            elif i == '#':
                if Num_lock:
                    Num_lock = False
                else:
                    Num_lock = True
            else:
                if End:
                    st.push(i, 'end')
                elif Home:
                    st.push(i, 'home')

    st.h1_to_h2()
    return(st.combine_all())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    S = input()

    result = receivedText(S)

    fptr.write(result + '\n')

    fptr.close()

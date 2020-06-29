#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMinConnectionChange' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY connection as parameter.
def getMinConnectionChange(connection):
    # Write your code here
    # Write your code here
    ############### counting single nodes ################
    single_set = set()
    v_set = set()
    for i in range(1, len(connection)+1):
        if i == connection[i-1]:
            if connection[i-1] in v_set:
                if connection[i-1] in single_set:
                    single_set.remove(connection[i-1])
            else:
                single_set.add(connection[i-1])
        elif connection[i-1] in single_set:
            single_set.remove(connection[i-1])
                
        v_set.add(connection[i-1])
        
    nodes = len(single_set)
    
    ################ counting single chains ###############
    pi = 0
    sn_count = 0
    while pi < len(connection):
        if pi+1 == connection[pi]:
            sn_count += 1
            connection[pi] = 'v'
        pi += 1
    #print(connection)
    #print(sn_count)
    chains = sn_count - nodes
    
    ############## detecting loops #######################
    pi = 0
    l_count = 0
    cur_set = set()
    
    connection = ['s'] + connection
    for i in range(1, len(connection)):
        if connection[i] != 'v':
            pi = connection[i]
            connection[i] = 'v'
            cur_set.add(i)
            while pi != 'v':
                if pi in cur_set:
                    l_count += 1
                    #print(cur_set)
                    pi = 'v'
                    cur_set = set()
                else:
                    cur_set.add(pi)
                    temp = connection[pi]
                    connection[pi] = 'v'
                    pi = temp
            cur_set = set()
            
    loops = l_count
    print("nodes : ", nodes)
    print("chains : ", chains)
    print("loops : ", loops)
    if nodes == 1 and chains == 0 and loops == 0: return 0
    elif nodes == 0 and chains == 1 and loops == 0: return 0
    elif nodes == 0 and chains == 0: return loops
    else:
        return (nodes + chains + loops - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    connection = list(map(int, input().rstrip().split()))

    result = getMinConnectionChange(connection)

    fptr.write(str(result) + '\n')

    fptr.close()
# Write your code here
N = int(input())
arr = list(map(int, input().split()))

def give_soln(n):
    return ((2**n) - (1 + (n) + (n*(n-1)/2)))

my_dict = dict()
for i in arr:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

count = 0
for side in my_dict:
    if my_dict[side] >=3:
        count += give_soln(my_dict[side])

print(int(count)%(10**9 + 7))

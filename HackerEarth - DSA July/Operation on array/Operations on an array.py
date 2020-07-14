# Write your code here
def query(arr, x, l, r, k):
    for i in range(l-1,r):
        if arr[i] == x:
            k -= 1
        if k == 0:
            print(i+1)
            return
    print(-1)
    return
    

def update(arr, ind, value):
    arr[ind-1] = value


n,x = map(int, input().split())
arr = list(map(int, input().split()))
Q = int(input())
for q in range(Q):
    
    s = input().split()
    if s[0] == '1':
        l,r,k = int(s[1]), int(s[2]), int(s[3])
        query(arr, x, l, r, k)
    else:
        ind, value = int(s[1]), int(s[2])
        update(arr, ind, value)

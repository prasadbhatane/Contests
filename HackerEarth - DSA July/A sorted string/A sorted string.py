def solve (n, s):
    # Write your code here
    nb = []
    for letter in s:
        if letter == 'a':
            nb.append('1')
        elif letter == 'b':
            nb.append('0')
        elif letter == 'c':
            nb.append('-1')

    sum = 0
    count = 0
    for i in range(len(nb)):
        sum = int(nb[i])
        if sum > 0:
            count += 1
        for j in range(i+1, len(nb)):
            sum += int(nb[j])
            if sum > 0:
                count += 1

    return count



n = int(input())
s = input()

out_ = solve(n, s)
print (out_)

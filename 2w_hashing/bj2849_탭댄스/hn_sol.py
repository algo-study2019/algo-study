import sys
n, q = input().spilt()
q = [True for i in range(int(q))]
t = int(input())
leng = [t-1,t+1]
swap = {True:False, False:True}
for line in sys.stdin.read().splitlines():
    line = int(line)
    q[line] = swap[q[line]]
    left = 0
    right = 0
    if q[line-1]

    leng[0] = min(leng[0], line-1)
    leng[1] = max(leng[1], line+1)
    for l in range(leng[0], leng[1]):
        temp =
    print(temp[1]-temp[0])

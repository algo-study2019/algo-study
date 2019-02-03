from collections import deque
n, k = input().split()
v = list(map(int, input().split()))
v = deque(sorted(v))
for _ in range(int(k)):
    mx = v[1]-v[0]
    mn = v[-1]-v[-2]
    if mx>mn : v.popleft()
    else : v.pop()
m = v[-1]-v[0]
for i, v_ in enumerate(list(v)[1:]):
    if m>(v_-v[i]): m = v_-v[i]
print(v[-1]-v[0]+m)

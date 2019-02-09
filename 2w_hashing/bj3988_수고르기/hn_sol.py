from collections import deque
n, k = list(map(int,input().split()))
v = list(map(int, input().split()))
v = sorted(v)
M = 0
m = v[-1]-v[0]
left = right = n//2
ret = deque()
for _ in range(int(n-k)):
    try :
        if ret[0]-v[left] < v[right]-ret[-1] :
            ret.appendleft(v[left])
            m = min(m, ret[1]-ret[0])
            left-=1
        else :
            ret.append(v[right])
            m = min(m, ret[-1]-ret[-2])
            right +=1
    except IndexError :
        ret.append(v[left])
        left-=1
        right+=1
    M = ret[-1]-ret[0]
print(M+m)

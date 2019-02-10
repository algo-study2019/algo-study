from collections import deque
n = int(input())
towers = list(map(int, input().split()))
towers = deque(sorted(towers))
ret = 0
right = n-1
left = 0
floor = 0
numOfTowers = right-left+1
while numOfTowers>0:
        top = towers[right]-floor
        if numOfTowers>top :
            destroy = towers[left]-floor
            floor += destroy
            while towers[left]<=floor:
                left+=1
                if left>right : break
            ret += destroy
        else:
            right -= 1
            ret += 1
        numOfTowers = right-left+1
print(ret)

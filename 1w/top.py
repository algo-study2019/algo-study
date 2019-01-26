from collections import deque
def solution(heights):
    answer = deque()
    length = len(heights)-1
    for hidx, height in enumerate(heights[::-1]):
        hidx = length-hidx
        while 1:
            hidx -= 1
            if hidx <0 :
                answer.appendleft(0)
                break
            if heights[hidx] >height:
                answer.appendleft(hidx+1)
                break
    return list(answer)

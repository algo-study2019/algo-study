from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 1
    remain = deque(truck_weights)
    on = deque()
    on.append((answer,remain.popleft()))
    while len(remain)>0 or len(on)>0:
        answer +=1
        if answer-on[0][0] == bridge_length:
            on.popleft()
        if len(remain)>0 and sum(w for _,w in on)+remain[0] <=weight:
            on.append((answer, remain.popleft()))
    return answer

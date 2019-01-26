def solution(arrangement):
    answer = 0
    stackMemory = False
    stack = 0
    for i, a in enumerate(arrangement):
        if a==")":
            stack -=1
            if stackMemory : answer += stack
            else : answer += 1
            stackMemory = False
        else :
            stack+=1
            if arrangement[i+1] ==")": stackMemory = True
            else : stackMemory = False
    return answer

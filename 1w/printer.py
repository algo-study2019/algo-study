def solution(priorities, location):
    answer = 0
    pointer = 0
    length = len(priorities)-1
    while priorities[location]!=-1:
        if priorities[pointer] == max(priorities):
            answer += 1
            priorities[pointer] = -1
        if pointer==length : pointer = 0
        else : pointer +=1
    return answer

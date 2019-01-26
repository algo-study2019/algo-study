def solution(prices):
    answer = []
    for pointer, price in enumerate(prices):
        temp = 0
        pointer+=1
        while pointer<len(prices):
            temp+=1
            if prices[pointer]<price :
                answer.append(temp)
                break
            pointer+=1
        if pointer == len(prices) : answer.append(temp)
    return answer

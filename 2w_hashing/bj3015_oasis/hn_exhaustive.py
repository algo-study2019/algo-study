import sys
n = int(input())
people = [int(p) for p in sys.stdin.read().splitlines()]
for i, person in enumerate(people):
    temp = 0
    interMax = 0
    for j in range(i+1, n):
        if people[j]>=interMax:
            interMax = people[j]
            temp+=1
        if people[j]>person :break
    answer.append(temp)
print(sum(answer))

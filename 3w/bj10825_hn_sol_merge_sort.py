import sys
sys.setrecursionlimit(20000000)
n = int(input())
students = sys.stdin.read().splitlines()

def merge_sort(origin, dup, key, low, high, ascending=True):
    if high <= low :
        return
    mid = low + (high-low)//2
    merge_sort(origin, dup, key, low, mid, ascending=ascending)
    merge_sort(origin, dup, key, mid+1, high, ascending=ascending)
    merge(origin, dup, key, low, mid, high, ascending=ascending)

def merge(origin, dup, key, low, mid, high, ascending):
    i = low
    j = mid+1
    for k in range(low, high+1):
        if i>mid:
            dup[k] = origin[j]
            j+=1
        elif j > high:
            dup[k] = origin[i]
            i+=1
        elif ascending:
            if origin[i][key] <= origin[j][key]:
                dup[k] = origin[i]
                i+=1
            else :
                dup[k] = origin[j]
                j+=1
        else :
            if origin[i][key] >= origin[j][key] :
                dup[k] = origin[i]
                i+=1
            else:
                dup[k] = origin[j]
                j+=1
    for k in range(low, high+1):
        origin[k] = dup[k]
def createDummy(n):
    return [None for _ in range(n)]

students = [student.split() for student in students]
students = [[s[0]]+list(map(int, s[1:])) for s in students]
sortRules = [(0,True), (3, False), (2, True), (1, False)]
for key, ascending in sortRules:
    dummy = createDummy(n)
    merge_sort(students, dummy, key, 0, n-1, ascending)
for student, _, _, _ in students:
    print(student)

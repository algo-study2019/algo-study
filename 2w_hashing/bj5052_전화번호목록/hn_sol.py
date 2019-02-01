import sys
t = int(input())
data = sys.stdin.read().splitlines()
i = 0
for _ in range(t):
    n = int(data[i])
    lists = data[i+1:i+n+1]
    lists = sorted(lists)
    for l, list_ in enumerate(lists):
        n = len(list_)
        break_ = False
        for other in lists[l+1:]:
            if other[:n] == list_ :
                break_ = True
                break
        if break_ :
            print('NO')
            break
    if not break_ : print('YES')
    i += n+1

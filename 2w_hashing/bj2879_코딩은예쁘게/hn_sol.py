n = int(input())
present = list(map(input().split(), int))
correct = list(map(input().split(), int))

while 1:
    diff = [c-p for p,c in zip(present, correct)]
    if sum(diff)==0 : break
    mx = max(diff)
    mn = min(diff)
    if abs(mx) > abs(mn):
        present = [p-mx for p in present]

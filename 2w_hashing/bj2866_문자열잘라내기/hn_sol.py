import sys
r, c= map(int, input().split())
alpha = sys.stdin.read().splitlines()
beta = ['' for i in range(c)]
count_ = 0
for i in range(c):
    for a in alpha:
        beta[i]+=a[i]
for i in range(1,r):
    set_ = []
    for b in beta:
        set_.append(b[i:])
    len1 = len(set_)
    len2 = len(set(set_))
    if len1>len2 : break
    count_ += 1
print(count_)

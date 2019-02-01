from ctypes import c_wchar
import sys
n = int(sys.stdin.readline())
suffix = c_wchar(sys.stdin.readline().encode('utf-8'))
suffix = [c_wchar(suffix.values[i:]) for i in range(-n,0)]
suffix = sorted(suffix, key=lambda k : k.values)
lcp = [-1]
for s, suf in enumerate(suffix[1:]):
    count_ = 0
    for i,v in enumerate(suffix[s].values):
        if v == suf[i].values : count_ +=1
        else : break
    suffix[s] = count_
print(max(suffix))

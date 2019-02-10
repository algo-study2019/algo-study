import sys
from collections import Counter
n, h = map(int, input().split())
huddles = sys.stdin.read().splitlines()
ups = [h-int(huddle) for i, huddle in enumerate(huddles) if i%2==1]
downs = [int(huddle) for i, huddle in enumerate(huddles) if i%2==0]
ups = sorted(ups)
downs = sorted(downs)
numOfBlocks = 0
minBlock = sys.maxsize
leng = n//2-1
di = 0
ui = 0
for height in range(h):
    if di<leng:
        while height>=downs[di]:
            di+=1
            if di==leng : break
    if ui<leng:
        while height>=ups[ui]:
            ui+=1
            if ui==leng : break
    localMin = 0
    if downs[di]>height :
        localMin += leng+1-di
    if ups[ui]>height :
        localMin += ui
    else :
        localMin += ui+1
    if minBlock > localMin:
        minBlock = localMin
        numOfBlocks = 1
    elif minBlock == localMin:
        numOfBlocks +=1
print(minBlock, numOfBlocks, sep=' ')

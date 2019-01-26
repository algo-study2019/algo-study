from collections import deque
def solution(progresses, speeds):
    answer = []
    devs = deque(progresses)
    speeds = deque(speeds)
    while len(devs)>0:
        devs = deque(dev+speed for dev, speed in zip(devs, speeds))
        ret = 0
        while len(devs)>0 and devs[0]>=100:
            devs.popleft()
            speeds.popleft()
            ret+=1
        if ret >0 : answer.append(ret)
    return answer

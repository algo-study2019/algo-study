# 입력 데이터 처리
N = int(input())
tabNow = list(map(int,input().split()))
tabAnswer = list(map(int, input().split()))

# 풀이를 위한 스택 및 카운터 선언
tabStack = []
tabCount = 0

# 스택으로 문제를 푸는 과정
# 1. 먼저 답과 현재 위치의 차이를 계산한다.
# 2. 스택이 비어있다면, 차이를 스택에 넣는다.
# 3. 아니라면 두 개의 분기로 갈라진다.
#
#	3.1. 차이가 음수인 경우
#		차이가 음수인 경우에는 먼저 현재 스택의 탑이 음수인지, 양수인지 확인한다.
#		
#		3.1.1 스택의 탑이 음수인 경우
#			차이의 값이 탑보다 크다면, 탑에서 차이를 뺀다. 그 후, 차이를 스택에 넣는다.
#			만약 작거나 같다면, 탑을 꺼낸뒤 차이를 스택에 넣는다.
#		3.1.2 스택의 탑이 양수인 경우
#			스택이 빌때까지 탑을 하나하나 꺼내서 카운터에 더한다. 그 후 차이를 스택에 넣는다.
#
#
#	3.2. 차이가 양수인 경우
#		차이가 양수인 경우에도 현재 스택의 탑이 음수인지, 양수인지 확인한다.
#
#		3.2.1 스택의 탑이 음수인 경우
#			스택이 빌때까지 탑을 하나하나 꺼내서 카운터에서 뺀다. 그 후 차이를 스택에 넣는다.
#		3.2.2 스택의 탑이 양수인 경우
#			차이의 값이 탑보다 크다면, 탑을 꺼낸뒤 차이를 스택에 넣는다.
#			만약 작거나 같다면, 탑에서 차이를 뺀다. 그 후, 차이를 스택에 넣는다.
#
# 4. 이후 스택의 값들이 양수라면 카운터에 더하고, 음수라면 뺀다.
# 5. 카운터를 출력한다.

for i in range(N):
	tabMove = tabAnswer[i] - tabNow[i]

	if tabMove < 0:
		if tabStack == []:
			tabStack.append(tabMove)
		else:
			if tabStack[-1] < 0:
				if tabStack[-1] < tabMove:
					tabStack[-1] -= tabMove
					tabStack.append(tabMove)
				else:
					tabStack.pop()
					tabStack.append(tabMove)
			else:
				while tabStack != []:
					tabCount += tabStack.pop()
				tabStack.append(tabMove)
	else:
		if tabStack == []:
			tabStack.append(tabMove)
		else:
			if tabStack[-1] < 0:
				while tabStack != []:
					tabCount -= tabStack.pop()
				tabStack.append(tabMove)
			else:
				if tabStack[-1] < tabMove:
					tabStack.pop()
					tabStack.append(tabMove)
				else:
					tabStack[-1] -= tabMove
					tabStack.append(tabMove)

if tabStack != []:
	while tabStack != []:
		if tabStack[-1] < 0:
			tabCount -= tabStack.pop()
		else:
			tabCount += tabStack.pop()

print(tabCount)
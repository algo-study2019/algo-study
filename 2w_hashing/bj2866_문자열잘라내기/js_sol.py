# 입력 받기
R, C = map(int, input().split(' '))

#해시 테이블 초기화
table = {i: "" for i in range(C)}
string = ""
cnt = 0

#받은 입력을 하나의 문자열로
for i in range(R):
	string += input()

#문자열 해싱
for i in range(len(string)):
	table[i%C] += string[i]

#문제 조건상 처음은 무조건 다르고, 해당 잘라내기를 세지 않으므로 한 줄 잘라내고 시작.
for i in range(C):
	table[i] = table[i][1:]

#해시 테이블을 뒤집어서 중복값을 확인함
revTable = {table[i]: i for i in range(C)}

#중복값이 있거나 테이블이 빌 때까지 잘라내고 뒤집기를 반복
while C <= len(revTable) and table[0] != "":
	for i in range(C):
		table[i] = table[i][1:]
	cnt+=1
	revTable = {table[i]: i for i in range(C)}

#몇번 했는지 출력
print(cnt)	

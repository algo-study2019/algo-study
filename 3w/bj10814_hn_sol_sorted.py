import sys
n = int(input())
members = sys.stdin.read().splitlines()
members = [member.split() for member in members]
members = [[int(m[0]), m[1]] for m in members]
members = sorted(members, key=lambda k:k[0])
for member in members:
    print(member[0], member[1], sep=' ')

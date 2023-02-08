# 상하좌우.py

n = int(input())
data = list(input().split())

# 방향에 따른 좌표 움직임
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
directions = ['L', 'R', 'U', 'D']

# 시작 위치
x, y = 1, 1

for direction in data:
	index = directions.index(direction)
	nx = x + dx[index]
	ny = y + dy[index]

	if nx < 1 or ny < 1 or nx > n or ny > n:
		continue

	x = nx
	y = ny

print(x, y)
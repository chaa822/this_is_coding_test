# 모험가 길드.py
n = int(input())
data = list(map(int, input().split()))
data.sort()

count = 0
result = 0
for i in data:
	count += 1
	if count >= i:
		count = 0
		result += 1
print(result)

# 5
# 2 3 1 2 2
# 문자열 뒤집기.py

counts = [0 for i in range(2)]
data = list(map(int, input()))

number = -1
for num in data:
	if num != number:
		counts[num] += 1
		number = num

counts.sort()
print(counts[0])
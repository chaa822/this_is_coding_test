# 볼링공 고르기.py
n, m = map(int, input().split())
data = list(map(int, input().split()))

# print(n, m)
# print(data)

array = [0] * 11
for x in data:
	array[x] += 1
# print(array)

result = 0
for i in range(1, m + 1):
	n -= array[i]
	result += array[i] * n
print(result)


# 5 3
# 1 3 2 3 2
# 출력 : 8

# 8 5
# 1 5 4 3 2 4 5 2
# 출력 : 25
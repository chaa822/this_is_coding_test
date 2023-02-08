# 곱하기 혹은 더하기.py
data = input()
result = int(data[0])
for i in range(1, len(data)):
	num = int(data[i])
	if result > 1 and num > 1:
		result *= num
	else:
		result += num

print(result)

# 02984 - 576
# 567 - 210
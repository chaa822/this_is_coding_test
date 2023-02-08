# 문자열 재정렬.py

data = input()

number = 0
result = []

for i in data:
	if i.isalpha(): # 알파벳이면
		result.append(i)
	else:
		number += int(i)

result.sort()
if number != 0:
	result.append(str(number))
# print(result)
print(''.join(result))

# K1KA5CB7
# AJKDLSI412K4JSJ9D
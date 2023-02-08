# 럭키 스트레이트.py

data = input()
length = len(data)

summary = 0
for i in range(length // 2):
	num = int(data[i])
	summary += num

for i in range(length // 2, length):
	num = int(data[i])
	summary -= num

if summary == 0:
	print("LUCKY")
else:
	print("READY")
# 거스름 돈.py

coins = [500, 100, 50, 10]

count = 0
input = int(input())
# print(input)

for coin in coins:
	count += input // coin
	input = input % coin

print(count)
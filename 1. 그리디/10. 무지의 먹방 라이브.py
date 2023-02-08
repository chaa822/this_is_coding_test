# 무지의 먹방 라이브.py

import heapq

def solution(food_times, k):
	# 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
	if sum(food_times) <= k:
		return -1

	# 시간이 작음 음식부터 빼야 하므로 우선순위 큐를 이용
	queue = []
	for i in range(len(food_times)):
		heapq.heappush(queue, (food_times[i], i + 1))

	print(queue)

	sum_value = 0	# 먹기 위해 사용한 시간
	previous = 0	# 직전에 다 먹은 음식 시간
	length = len(food_times)	# 남은 음식의 개수

	while sum_value + ((queue[0][0] - previous) * length) <= k:
		now = heapq.heappop(queue)[0]
		sum_value += (now - previous) * length
		length -= 1
		previous = now

	result = sorted(queue, key = lambda x : x[1])
	return result[(k - sum_value) % length][1]

print(solution([3, 1, 2], 5))

# 3 1 2
# 5
# result : 1
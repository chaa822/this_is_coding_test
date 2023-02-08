def solution(inputArray):
	result = inputArray[0] * inputArray[1]
	# print(result)

	for i in range(1, len(inputArray) - 1):
		num = inputArray[i] * inputArray[i + 1]
		result = max(result, num)

	return result

print(solution([3, 6, -2, -5, 7, 3]))
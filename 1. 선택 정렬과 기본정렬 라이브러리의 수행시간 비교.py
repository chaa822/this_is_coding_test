# 선택정렬과 기본정렬 라이브러리의 수행시간 비교

from random import randint
import time

# 배열에 1000개의 정수를 삽입
array = []
for _ in array:
	array.append(randint(1, 100))

# 선택 정렬 프로그램 성능 측정
startTime = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
	min_index = i
	for j in range(i + 1, len(array)):
		if array[min_index] > array[j]:
			min_index = j
		array[i], array[min_index] = array[min_index], array[i]

endTime = time.time()
print("선택 정렬 성능 측정: ", endTime - startTime)

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(1000):
	array.append(randint(1, 100))

# 기본 정렬 라이브러리 성능 측정
startTime = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

endTime = time.time()
print("기본 정렬 라이브러리 성능 측정: ", endTime - startTime)
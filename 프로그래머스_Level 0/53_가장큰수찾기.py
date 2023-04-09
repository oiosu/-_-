# 문제 설명
# 정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항

#     1 ≤ array의 길이 ≤ 100
#     0 ≤ array 원소 ≤ 1,000
#     array에 중복된 숫자는 없습니다.

# 입출력 예
# array 	result
# [1, 8, 3] 	[8, 1]
# [9, 10, 11, 8] 	[11, 2]

# list에서 가장 큰 수와 작은 수를 찾으려면 max(), min()을 사용하면 된다.
# list에서 특정 값의 index 값을 추출하려면 index()를 사용하면 된다.

def solution(array):
    return [max(array), array.index(max(array))]
# 문제 설명
# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 입출력 예
# num_list 	result
# [1, 2, 3, 4, 5] 	[2, 3]
# [1, 3, 5, 7] 	[0, 4]

def solution(num_list: list) -> list:
    answer = [0, 0]
    
    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    
    return answer

if __name__ == '__main__':
    print(solution([1, 2, 3, 4, 5]))  # [2, 3]
    print(solution([1, 3, 5, 7]))     # [0, 4]
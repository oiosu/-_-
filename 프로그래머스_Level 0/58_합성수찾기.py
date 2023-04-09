# 문제 설명
# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
# 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
#     1 ≤ n ≤ 100

# 입출력 예
# n 	result
# 10 	5
# 15 	8

def solution(n):
    #약수의 개수를 담을 리스트와 합성수를 선언
    num = []
    answer = 0
    #2~n까지 약수의 개수를 구한다.
    for i in range(2, n+1):
        for j in range(1, i+1):
            if i % j  == 0:
                num.append(i)
                
        if num.count(i) >= 3:
            answer += 1
    return answer
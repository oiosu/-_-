# 문제 설명
# 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 
# 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
#     0 < num < 1,000,000
#     0 ≤ k < 10
#     num에 k가 여러 개 있으면 가장 처음 나타나는 자리를 return 합니다.

# 입출력 예
# num 	k 	result
# 29183 	1 	3
# 232443 	4 	4
# 123456 	7 	-1


#  find(), index()

# find()
# 찾는 문자가 없는 경우에 -1을 출력한다.
# 문자열을 찾을 수 있는 변수는 문자열만 사용이 가능하다.
# 리스트, 튜플, 딕셔너리 자료형에서는 find 함수를 사용할 수 없다.
# 만일 사용하게 되면 AttributeError 에러가 발생한다.

#index()
# 찾는 문자가 없는 경우에 ValueError 에러가 발생한다.
# 문자열, 리스트, 튜플 자료형에서 사용 가능하고 딕셔너리 자료형에는 사용할 수 없어 AttributeError 에러가 발생한다.

def solution(num, k):
    a = str(num).find(str(k))
    return (a if a == -1 else a+1)
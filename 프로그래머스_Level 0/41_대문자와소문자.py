# 문제 설명
# 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 
# solution 함수를 완성해주세요.

# 제한사항
#     1 ≤ my_string의 길이 ≤ 1,000
#     my_string은 영어 대문자와 소문자로만 구성되어 있습니다.

# 입출력 예
# my_string 	result
# "cccCCC" 	"CCCccc"
# "abCdEfghIJ" 	"ABcDeFGHij"


# 3번째 줄 for문: 문자열 my_string의 각 요소를 isupper()를 이용하여 대문자인지 판단한다.

# 4번째 줄 if문: 만약 isupper()를 이용하여 대문자인지 판단한 결과가 True이면 대문자이기 때문에 lower()를 사용해 소문자로 바꿔주고 answer에 붙인다.

# 6번째 줄: 만약 False면 소문자 이기 때문에 upper()를 사용해 대문자로 바꿔주고 answer에 붙인다.

def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer
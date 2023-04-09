# 문제 설명
# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# 제한사항

#     1 ≤ my_string의 길이 ≤ 100
#     letter은 길이가 1인 영문자입니다.
#     my_string과 letter은 알파벳 대소문자로 이루어져 있습니다.
#     대문자와 소문자를 구분합니다.

# 입출력 예
# my_string 	letter 	result
# "abcdef" 	"f" 	"abcde"
# "BCBdbe" 	"B" 	"Cdbe"


def solution(my_string, letter):
    return ''.join([c for c in my_string if c != letter])

#3.1. replace()
# replace(A, B) : 문자열의 A를 모두 B로 변경함.
# 만약, 처음 발견되는 1개만 변경하고 싶다면, replace(A,B,1)로 하면 됨.

# 3.2. sub()
# sub(regex, replacement, str) : 문자열 str에서 정규표현식 regex에 해당하는 문자들을 모두 replacement로 변경함.
# 문제설명
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

# 힌트 : 문자열의 마지막 5글자를 부분 문자열로 추출하기 
# string = "freecodecamp"
# print(string[-5:]
# 출력된 값 : eCamp
# 참고한 사이트 > https://www.freecodecamp.org/korean/news/how-to-substring-a-string-in-python/

def solution(my_string, n):
    answer = ''
    answer = my_string[-n:]
    return answer

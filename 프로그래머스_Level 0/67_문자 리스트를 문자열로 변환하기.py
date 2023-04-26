# 문제설명 
# 문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.

# print(''.join(array)) # array Element들을 공백없이 붙임
# print(' '.join(array)) # array Element들을 공백을 이용해서 구분
# print('-'.join(array)) # array Element들을 '-' 문자를 이용해서 구분
# print('\n'.join(array)) # 한줄에 하나씩 출력
# 참고한 사이트 : https://hbase.tistory.com/108

# 첫번째 시도 
# def solution(arr):
#     answer = ''
#     answer = join(arr)
#     return answer

# NameError  name 'join' is not defined

# 두번째 시도 (통과)

def solution(arr):
    answer = ''
    return (''.join(arr))

# 문제 설명
# 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 
# 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다.
# a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 나이 age가 매개변수로 주어질 때
# PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

# 제한사항

#     age는 자연수입니다.
#     age ≤ 1,000
#     PROGRAMMERS-962 행성은 알파벳 소문자만 사용합니다.

# 입출력 예
# age 	result
# 23 	"cd"
# 51 	"fb"
# 100 	"baa"


def solution(age):
    answer = ""
    word = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    #index = 0    1    2    3    4    5    6    7    8    9
    
    for i in str(age):
        answer += word[int(i)]
        
    return answer

# 3번째 줄: 알파벳을 word에 저장한다.
# 4번째 줄: 문제에서 a가 0, b = 1, c = 2, d = 3.... j =9 라고 했으니깐 리스트에다가 저장한다.
# 6번째 줄: age를 str형으로 변환하여 각 요소를 i에다가 넣어준다.
# 7번째 줄: word에 str으로 바꿔준 age 를 인덱싱 하기 위하여 int()형으로 바꿔주고 각 인데스에 맞는 값을 answer에 저장한다.
# 1. 문제 설명 
# 각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 
# 각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.

# 입출력 예
# angle 	result
# 70 	    1
# 91 	    3
# 180 	    4

def solution(angle):
        #  예각일 때 1
        if 0 < angle < 90:
               answer = 1
        
        # 직각일 때 2
        elif angle == 90:
               answer = 2

        # 둔각일 때 3
        elif  90 < angle < 180:
                answer = 3
        
        # 평각일 때 4
        elif angle == 180:
               answer = 4
        else:
               print("error")

        return answer
        

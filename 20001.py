S = input()

q = 0  # 변수 선언

while True:
    duck = input()
    if duck == "고무오리 디버깅 끝":
        break
    else: # 문제 or 고무오리 입력

        if duck == "문제": # 문제의 개수 +1
            q += 1

        elif duck == "고무오리": 
            if q == 0: # 문제의 개수가 0개
                q += 2 # 체벌로 2개 +

            else: # 문제의 개수 1개
                q -= 1 # 한 문제 해결 -> 문제의 갯수 -1

if q == 0:
    print("고무오리야 사랑해")

else:
    print("힝구")
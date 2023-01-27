test_case = int(input())

string = []

for i in range(0,test_case): 
    string.append(input())

string = list(set(string)) # 중복단어 제거(set) 및 정렬(list)
string.sort() # 사전 순 정렬
string.sort(key=len) # 길이 순 정렬

for i in string:
    print(i)



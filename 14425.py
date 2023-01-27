S = ['beakjoononlinejudge','startlink','codeplus','sundaycoding','codingsh']

words = ['beakjoon','codeplus','codeminus','startlink','starlink','sundaycoding','codingsh'
'codinghs','sundaycoding','startrink','icerink']


cnt = 0
for word in words:
    if word in S:
        cnt += 1

    print(cnt)

cnt = 0

S = set(S)
for word in words:
    if word in S:
        cnt += 1
    print(cnt)
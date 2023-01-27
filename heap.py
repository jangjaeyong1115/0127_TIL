import heapq
numbers = [0,12345678,1,2,0,0,0,0,32]

heap = []
# 순회

for n in numbers:
    n = int(input())
    # 0이 아니면 heappush
    if n != 0:
        heapq.heappush(heap,n)

    # 0이면 heappop
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)


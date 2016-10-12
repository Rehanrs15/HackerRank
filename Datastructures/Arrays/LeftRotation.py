N,K = map(int,input().split())
L = list(map(int,input().split()))
NewList = L[K:]+L[:K]
for i in NewList:
    print(i,end=" ")
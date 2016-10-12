N,Q = map(int,input().split())
L = list()
for i in range(N):
    L.append([])
lastans = 0
for i in range(Q):
    q,x,y = map(int,input().split())
    if q == 1:
        seq = (x ^ lastans) % N
        L[seq].append(y)
    elif q == 2:
        seq = (x ^ lastans) % N
        n = y%len(L[seq])
        lastans = L[seq][n]
        print(lastans)
#print(L)
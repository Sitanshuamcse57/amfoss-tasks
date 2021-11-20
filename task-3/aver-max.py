t=int(input())
for i in range(t):
    n,k = map(int,(input("")).split())
    p=list(map(float,input().split()))[:n]
    res = [[]]
    if k==0:
        for e in p:
            res += [sub + [e] for sub in res]

        maxValue = max(list(res))
    else:
        for j in range(len(p)):
            p.append(-1*p[j])
        for e in p:
            res += [sub + [e] for sub in res]

        maxValue = max(list(res))
    print(max(maxValue))
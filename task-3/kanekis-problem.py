N=int(input())
Na=list(map(int,input().split()))[:N]
q=int(input())
qA=[]
fP=[]
sP=[]
for i in range(q):
    qA.append(list(map(int,input().split()))[:q])
i=0
for z in range(q):
    for i in range(2):
        t2=qA[z][i]
        fP.append(t2)
    a=fP[0]
    b=fP[1]
    fP.clear()
    sum=0
    j=0
    for j in range (a,b+1,1): 
        sum += Na[j-1]
    sP.append(sum)
y=0
for y in range(len(sP)):
    print(sP[y])
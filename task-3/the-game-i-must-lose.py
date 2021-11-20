N,M = map(int,(input("")).split())

a=[]
ch=0
if N>=1 and M < 1000000:
    for i in range(1,M+1):
        if i%2!=0 and i != N:
            a.append(i)
            ch=ch+1
print(ch)
for x in range(len(a)):
    print(a[x],end=" ")

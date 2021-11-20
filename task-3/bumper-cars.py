X,N = map(int,(input("")).split())
N1,N2,N3 = map(int,(input("")).split())
D1,D2,D3 = map(int,(input("")).split())

fa=[]
if D1==D2:
   a1pd1 = N+1-N1
   a2pd2 = N+1-N2
else:
   if D2<0:
    i = (N1+N2)/2
    a1pd1 = 2*i-1
    a2pd2 = (N2-i)+(N+1-i)
    a3pd3 = N+1-N3 
   else:
    a1pd1 = N1
    a2pd2 = N+1-N2
    a3pd3 = N+1-N3 

fa = [a1pd1,a2pd2,a3pd3]
time1 = int(max(fa))
print(time1)
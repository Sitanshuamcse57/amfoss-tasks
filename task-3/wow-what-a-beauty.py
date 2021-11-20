T=int(input())
for i in range(T):
    a,b,c,d,N = map(int,(input("")).split())
    y=N-1
    x=N-2
    if N<6:
      xx=[a,b,c,d,N]
      z=c*xx[x-1] + d*xx[y-1]
      print(z)
    else:
      z=0
      print(z)
t=int(input())
N,M,V,K = map(int,(input("")).split())
p=list(map(int,input().split()))[:M]

lArray=list(range(N))

for i in range(M):
      ch=p[i]-1
      lArray[(ch-1)]='x'
      lArray[(ch)]='x'
      lArray[(ch+1)]='x'
      
print(lArray)  
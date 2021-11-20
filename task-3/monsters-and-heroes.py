n,m = map(int,(input("")).split())
dn=list(map(int,input().split()))[:n]
dm=list(map(int,input().split()))[:m]
ans=0
ans1=0
for j in range(n):
  while (dn[j] >0):
    ans1 += dn[j]%n
    dn[j]//=n
if ans1%n==0:
  print("YES")
  for i in range(m):
    while (dm[i] >0):
      ans += dm[i]%m
      dm[i]//=m
  print(ans)
else:
  print("NO")
r=int(input(""))
i=0
wt=list(map(int,input().split()))[:r]

i=0
t=0
temp=[]
nTower={}
nTower=set(wt)

for i in nTower:
  t= wt.count(i)
  temp.append(t)

print(max(temp),len(nTower))
p=(int(input()))
pList=list(input())[:p]
rev=""  
i=0
print(p)
for i in pList:
    rev = i + rev
rList=list(rev.strip(" "))
i=0
if pList==rList:
    pList_str=''.join(map(str,pList))
    print(pList_str)
else:
    print(0)
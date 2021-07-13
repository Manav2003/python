n=int(input())
p=q=r=[]
p=input().split()
q=input().split()
r=input().split()
c=0
f=[]
g=[]
h=[]
for x in q:
    if f.count(x)==0:
        f.append(x)
for x in r:
    if g.count(x)==0:
        g.append(x)
for x in p:
    for y in f:
        if int(x)<int(y):
            h.append(y)
j=[]
for y in g:
    j.append(r.count(y))

for x in h:
    i=q.count(x)
    k=0
    for y in g:
        if int(x)<int(y):
            c+=i*j[k]
        k+=1
print(c)
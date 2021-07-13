f=[0]*101
n=input()
lst=[]
lst=input().split()
for y in lst:
    f[int(y)]+=1
y=0
for x in f:
    if x>y:
        y=x
print(y)
n,x=(input()).split()
x,n=[int(x),int(n)]
lst=[]
lst=input().split()
f=[0]*100001
c=0
for y in lst:
    f[int(y)]+=1
for y in lst:
    c=1
    if x-int(y)>0 and x-int(y)<100001:
        if (int(y)*2==x and f[int(y)]>1) or (int(y)*2!=x and f[int(y)]>0 and f[x-int(y)]>0):
            print ("Yes")
            break
    c=0
if c==0:
    print("No")
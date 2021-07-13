n=int(input())
count=0
while count<n:
    s=input()
    if len(s)<11:
        print (s)
    else:
     k=s[0]+str((len(s)-2))+s[len(s)-1]
     print (k)
        
    count+=1

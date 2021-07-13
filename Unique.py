for x in range(0,int(input())):
    k=int(input())
    if(k<1 or k>45):
        print("-1")
    elif(k<10):
        print(k)
    elif(k<18):
        print((k-9)*10+9)
    elif(k<25):
        print((k-17)*100+89)
    elif(k<31):
        print((k-24)*1000+789)
    elif(k<36):
        print((k-30)*10000+6789)
    elif(k<40):
        print((k-35)*100000+56789)
    elif(k<43):
        print((k-39)*1000000+456789)
    elif(k<45):
        print((k-42)*10000000+3456789)
    else:
        print('123456789')
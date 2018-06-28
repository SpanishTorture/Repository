
for n in range(10):
    a=1


print(n)

def Sort(Num):
    for n in range(len(Num)):
        for m in range(n,len(Num)):
            if Num[m]<Num[n]:
                Num[m],Num[n]=Num[n],Num[m]
    return Num
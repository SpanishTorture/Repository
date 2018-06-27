def Sort(Num):
    Count = [0]*(max(Num)+1)
    Solution = list()
    #Counts how many of each number there are in Num
    for n in range(len(Num)):
        Count[Num[n]]+=1

    #Creates ordered list
    for n in range(len(Count)):
        while Count[n]>0:
            Solution.append(n)
            Count[n]-=1
    print(Solution)
    return(Solution)

def Check(Test):
    Test = Sort(Test)
    for n in range(1,len(Test)):
        if Test[n]<Test[n-1]:
            print ("Fail")
            return
    print("Sucess")

#Tests
Test1=[3, 7, 2, 8, 11, 15, 2]
Test2=[3,47,22,81,113,54,2,81,78,1,77,222,7478,21]
Test3=[3057, 2, 614531, 6275, 1549, 5523, 966463, 5751, 3200, 22474, 2, 9307, 7899, 180, 4937, 5849, 92288, 38610, 42693, 85181, 53432, 33234, 65011, 55615, 84925, 37617, 15353, 11042, 9, 11523, 21914, 91634, 38014, 65294, 85786, 98407, 17040, 52998, 46685, 34322]

Check(Test1)
Check(Test2)
Check(Test3)
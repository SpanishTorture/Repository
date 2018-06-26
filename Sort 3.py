def Sort(Num):
    Solution = [None]*(max(Num)+1)

    #Converts the number to a string 
    for n in range(len(Num)):
        if Solution[Num[n]]==None:
            Solution[Num[n]]=str(Num[n])

        #handles duplicate numbers
        else:
            Solution[Num[n]]=str(Solution[Num[n]]) + " " + str(Num[n])

    #prints solution
    for n in range(len(Solution)):
        if Solution[n] != None:
            print (Solution[n], end=" ")
    print("")


#Tests
Test1=[3, 7, 2, 8, 11, 15, 2]
Test2=[3,47,22,81,113,54,2,81,78,1,77,222,7478,21]
Test3=[3057, 2, 614531, 6275, 1549, 5523, 966463, 5751, 3200, 22474, 2, 9307, 7899, 180, 4937, 5849, 92288, 38610, 42693, 85181, 53432, 33234, 65011, 55615, 84925, 37617, 15353, 11042, 9, 11523, 21914, 91634, 38014, 65294, 85786, 98407, 17040, 52998, 46685, 34322]

Sort(Test1)
Sort(Test2)
Sort(Test3)
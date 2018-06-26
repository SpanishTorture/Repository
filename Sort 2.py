import math

def Sort(Num):
    Solution = list()
    for n in range(len(Num)):
        Place, Base, Size = n, 0, math.ceil(n/2) 
        while Size > 0:
            if Solution[Place-Size]>Num[n]:
                Place = Place - Size
            else:
                Base = Base + Size
            Size=math.ceil((Place - Base)/2) 
        Solution.insert(Place, Num[n])
    print(Solution)

Test1=[3, 7, 2, 8, 11, 74, 2]
Test2=[3,47,22,81,113,54,2,81,78,1,77,222,7478,21]
Test3=[3057, 614531, 6275, 1549, 5523, 966463, 5751, 3200, 22474, 2, 9307, 7899, 180, 4937, 5849, 92288, 38610, 42693, 85181, 53432, 33234, 65011, 55615, 84925, 37617, 15353, 11042, 9, 11523, 21914, 91634, 38014, 65294, 85786, 98407, 17040, 52998, 46685, 34322]

Sort(Test1)
Sort(Test2)
Sort(Test3)

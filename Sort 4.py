import math

#Finds a value in the middle range (second tertile). Uses variant of median of median method where groups of three are used. 
def Middle(lst, down, up):
    if len(lst) == 0:
        return lst
    while up-down > 1:
        triple_count = math.floor((up-down)/3)
        if triple_count!= 0:
            for n in range(triple_count):
                #places median of each triple in front.
                if lst[n*3+down] > lst[n*3+down+1]:
                    lst[n*3+down], lst[n*3+down+1] = lst[n*3+down+1], lst[n*3+down]         
                if lst[n*3+down+1] > lst[n*3+down+2]:
                    lst[n*3+down+1], lst[n*3+down+2] = lst[n*3+down+2], lst[n*3+down+1] 
                    if lst[n*3+down] > lst[n*3+down+1]:
                        lst[n*3+down], lst[n*3+down+1] = lst[n*3+down+1], lst[n*3+down]
                lst[n*3+down], lst[n*3+down+1] = lst[n*3+down+1], lst[n*3+down] 
        #handles any remaining numbers at the end.
        if (up-down)%3 == 1:
            triple_count += 1
        if (up-down)%3 == 2:
            triple_count += 1
            if lst[up-1] > lst[up-2]:
                lst[up-1], lst[up-2] = lst[up-2], lst[up-1]
        #groups medians in front and sets [down,up] to reflect their range.
        for n in range(triple_count):
            lst[n], lst[3*n] = lst[3*n], lst[n]
        up=down+triple_count
    return (lst[down])

#orders list so approximated median is in middle, with higher and lower numbers above and below, respectively. Then splits the list along the median.
def Split(lst):
    approx_med, top, bot = Middle(lst,0,len(lst)), 0, 0
    #stops recursion when list is identical or comprises a single variable.
    if max(lst)==min(lst):
        return lst

    #ordering
    while top + bot < len(lst):
        if approx_med != min(lst):
            if lst[bot] >= approx_med:
                lst[bot], lst[len(lst)-top-1] = lst[len(lst)-top-1], lst[bot]
                top += 1
            elif lst[bot] < approx_med:
                bot += 1
        #If median is the min, splits after the median.
        else:
            if lst[bot] > approx_med:
                lst[bot], lst[len(lst)-top-1] = lst[len(lst)-top-1], lst[bot]
                top += 1
            elif lst[bot] <= approx_med:
                bot += 1
    #split
    lst[0:bot],lst[bot:]=Split(lst[0:bot]),Split(lst[bot:])
    return lst

def Sort(lst):
    return Split(lst)
    


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


    # #Reorganizes list. Moves max and min values to upper and lower half, respectively. 
    # for n in range(math.floor(up-down)/2):
    #     if lst[down+n] > lst[up-n]:
    #         lst[down+n],lst[up-n] = lst[up-n], lst[down+n]
    #     #Notes down location of duplicate extremities. These will not be picked as the median.
    #     if lst[down+n] == lst[up-n]:
    #         if lst[down+n] == Max or lst[down+n] == Min:
    #             Except.extend(down+n, up-n)
    #     if (up-down)%2==1
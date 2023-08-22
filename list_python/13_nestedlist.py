lst=[[1,2],[4,5],[50,45]]
"""for i in lst:
    for j in i:
        print(j)"""
#another method to print all numbers
num=[j for i in lst for j in i]
print(num)
#number gt 5
num_gt_5=[j for i in lst for j in i if(j>5)]
print(num_gt_5)
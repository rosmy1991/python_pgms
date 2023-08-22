#smallest missinf element
lst=[3,5]
for i in range(0,len(lst)):
    if(lst[0]!=1):
        print("missing element is one")
        break
    else:
        e1=lst[i]
        e2=lst[i+1]
        if e2-e1 != 1:
            print("missing element is",e1+1)
            break

# for i in range(0,len(lst)):
#     if(lst[0]!=1):
#         print("missing element is 1")
#         break
#     else:
#         e1=lst[i]
#         e2=lst[i+1]
#         if(e2-e1 != 1):
#             print("missing element is",e1+1)
#             break
        

     
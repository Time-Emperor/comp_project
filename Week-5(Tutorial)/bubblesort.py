lst = [2,4,5,1,3,7,0,6]
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            lst[j], lst[j+1]=lst[j+1],lst[j]
print("Sorted list is: ", lst)

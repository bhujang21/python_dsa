alist=[3,1,2,4,6,5]

for i in range(len(alist)):
    for j in range(i+1,len(alist)):
        if alist[i]>alist[j]:
            alist[i],alist[j]=alist[j],alist[i]


print(alist)

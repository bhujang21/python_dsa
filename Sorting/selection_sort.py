a=[5,15,3,12,17,0]

for i in range(len(a)):
    min_value=a[i]
    for j in range(i+1,len(a)):
        if a[j]<min_value:
            min_value,a[j]=a[j],min_value

    a[i]=min_value

print(a)

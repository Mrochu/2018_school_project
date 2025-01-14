def bubble_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a
a = [1235,12,53,-1,0,84,-141]
print(bubble_sort(a))

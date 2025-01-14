def partitionQuickSort(value, start, end):
    pivot = end
    right = end
    left = start
    temp = 0

    while (left < right):
        while ((value[left] < value[pivot]) and (left < right)):
            left = left + 1
        while ((value[right] >= value[pivot]) and (left < right)):
            right = right - 1

        if (left < right):
            print("정렬 범위:", start,"~",end, ",피봇-[", value[pivot], "],Left(", value[left], ")-Right(", value[right], ") 교환 전,", value[start: end])

            temp = value[left]
            value[left] = value[right]
            value[right] = temp

            print("정렬 범위:",start,"~",end, ",피봇-[", value[pivot], "],교환 후,", value[start: end])

    print("정렬 범위:",start,"~",end, ",피봇-[", value[pivot], "],Left(", value[left], ")-Right(", value[right],") 교환 전,",value[start: end])

    temp = value[pivot];
    value[pivot] = value[right];
    value[right] = temp;

    print("정렬 범위:",start,"~",end, ",피봇-[", value[pivot], "],교환 후,", value[start: end])

    return right

def quickSort(value, start, end):
    pivot = 0
    if (start < end) :
        pivot = partitionQuickSort(value, start, end)
        quickSort(value, start, pivot - 1)
        quickSort(value, pivot+1, end)

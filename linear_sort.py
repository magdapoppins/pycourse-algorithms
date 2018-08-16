def linear_sort(a, val):
    for i in range(len(a)):
        if val == a[i]:
            return i
    return None

arr1 = [1, 6, 4, 88, 5]
res1 = linear_sort(arr1, 88)
print("In array, at index: ", res1) 

arr2 = [1, 6, 4, 86, 5]
res2 = linear_sort(arr2, 88)
print("Not in array: ", res2)

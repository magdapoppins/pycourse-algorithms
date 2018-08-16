def insertion_ascending(a):
    for index in range(1, len(a)):
        key = a[index]
        position = index

        while position > 0 and a[position-1] > key:
            a[position] = a[position - 1]
            position = position - 1
            
        a[position] = key

def insertion_descending(a):
    for index in range(1, len(a)):
        key = a[index]
        position = index

        while position > 0 and a[position-1] < key:
            a[position] = a[position - 1]
            position = position - 1
            
        a[position] = key

arr1 = [ 1, 2, 7, 3, 9 ]
insertion_ascending(arr1)
print("Ascending: " + str(arr1))
insertion_descending(arr1)
print("Descending: " + str(arr1))


arr2 = [ 7, 8, 1, 3, 9 ]
insertion_ascending(arr2)
print("Ascending: " + str(arr2))
insertion_descending(arr2)
print("Descending: " + str(arr2))

arr3 = [ 45, 19, 4, 29, 41 ]
insertion_ascending(arr3)
print("Ascending: " + str(arr3))
insertion_descending(arr3)
print("Descending: " + str(arr3))
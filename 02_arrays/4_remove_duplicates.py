# Given a sorted array, remove the duplicates

#use set as auxiliary data structure, Time O(n), Space O(n)
def remove_dup_set(arr):
    b = set()
    for x in arr:
        b.add(x)
    return b

#use sorting and in place, Time O(n), Space O(1)
def remove_dup_in_place(arr) :
    arr.sort()
    i = 0
    for x in arr:
        if x > arr[i]:
            i += 1
            arr[i] = x           
    return i+1

# test set
arr = [1, 5, 3, 6, 3, 5, 6, 1]
b = remove_dup_set(arr)
print(b)

#test in place
arr1 = [1, 1, 2, 2, 2, 5, 6, 6]
k = remove_dup_in_place(arr1)
print("unique elements: " + str(k))
for i in range(0, k):
    print(arr1[i], end = ' ')
print()
# Given an array, remove the duplicates

#use set as auxiliary data structure, Time O(n), Space O(n)
def remove_dup_set(arr):
    new_set = set()
    for x in arr:
        new_set.add(x)
    return new_set

#use sorting and in place, Time O(nlogn), Space O(1)
def remove_dup_in_place(arr) :
    arr.sort()
    i = 0
    for x in arr:
        if x != arr[i]:
            i += 1
            arr[i] = x           
    return i+1

# test using set
arr = [1, 5, 3, 6, 3, 5, 6, 1]
set = remove_dup_set(arr)
print(set)

#test using sort and in place
new_length = remove_dup_in_place(arr)
print("number of unique elements: " + str(new_length))
for i in range(0, new_length):
    print(arr[i], end = ' ')
print()
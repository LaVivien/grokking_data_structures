# calculate the average of the numbers in an array.

#Time O(n), Sapce O(1)
def get_average(arr):
    n = len(arr)
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
    return sum/n

# test
arr = [14, 28, 33, 16, 5] 
print(get_average(arr))


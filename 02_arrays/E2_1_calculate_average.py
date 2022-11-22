# calculate the average of the numbers in an array.

#Time O(n), Sapce O(1)
def get_average(arr):
    count = 0
    sum = 0
    for x in arr:
        sum += x
        count += 1
    return sum/count

# test
arr = [14, 28, 33, 16, 5] 
print(get_average(arr))

arr = [4.12, 8.2, 3, 6.4, 5.2] 
print(get_average(arr))


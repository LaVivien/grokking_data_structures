# Find all pairs of integers within an array which sum to a specified value.

#Use sort and two pointers, Time O(n*logn), Space O(1)
def two_sum(arr, target):
    arr.sort()
    low = 0
    high = len(arr) - 1
    while (low < high):
        sum = arr[low] + arr[high]
        if (sum == target):
            print(arr[low], arr[high])
            low += 1
            high -= 1
        elif (sum < target): 
            low += 1
        else:
            high -= 1	  

#test
arr = [1, 2, 3, 4, 5]
sum = 6  
two_sum(arr, sum)

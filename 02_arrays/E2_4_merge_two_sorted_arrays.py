# Merge two sorted array into one sorted array. Can you do in place?

#Merge in place, Time O(m+n), Space O(1)
def merge_in_place(a, b, m, n) :
    k = m + n - 1
    i = m - 1 
    j = n - 1 		
    while j >= 0 and i >= 0: 
        if a[i] > b[j]: 										
            a[k] = a[i] 			
            k-=1; i-=1
        else:
            a[k] = b[j] 				
            k-=1; j-=1

# assign extra space at the end, m is the occupied cells
a1 = [0, 4, 5, 19, 21, 33, 36, 38, 61, 0, 0, 0, 0, 0]
m = 9
b1 = [1, 2, 7, 30, 40]
n = 5
merge_in_place(a1, b1, m, n)
print(a1)
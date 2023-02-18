my_deque = __import__('6_deque')

# Use deque and list, Time O(n), n is number of elements, Space O(k), k stored in deque
def max_sliding_window(arr, k):
    n = len(arr)
    result = [] # use list as output result
    if n == 0:
        return result
    dq = my_deque.Deque() 
    for i in range(n):
        while not dq.is_empty() and arr[dq.get_last()] <= arr[i]:
            dq.delete_last()
        dq.insert_last(i)
        if dq.get_first() <= i - k:
            dq.delete_first()
        if i >= k - 1:
            result.append(arr[dq.get_first()])
    return result

#test
if __name__ == "__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    print(max_sliding_window(arr, k))

 

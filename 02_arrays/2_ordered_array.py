class OrderedArray:

    #Constructor, Time O(1), Space O(1)
    def __init__(self, size):
        self.length = 0
        self.array = [None]*size
        self.maxSize = size

    #Add one element, Time O(n), Space O(1), n is array length
    def insert(self, value):
        if self.length == self.maxSize :
            print ("reach max size!")
            return
        i = self.length -1
        while i >= 0 and self.array[i] > value:
            self.array[i+1] = self.array[i]
            i -= 1
        self.array[i+1] = value
        self.length += 1

    #Delete by key, Time O(n), Space O(1)
    def delete(self, key) :
        i = self.binary_search(key)
        if i < 0 :
            print("delete key not found")
            return False
        else :
            for j in range (i, self.length-1, +1): 
                self.array[j] = self.array[j+1]
            self.length -= 1         
            return True
       
    #Binary search, Time O(logn), Space O(1)
    def binary_search(self, key) :
        low = 0
        high = self.length - 1	
        while (low <= high) :
            mid = low + (high-low)//2
            if self.array[mid] == key : 
                return mid
            elif key < self.array[mid] :
                high = mid - 1				
            else :
                low = mid + 1	
        return -1

    #Print array, Time O(n), Space O(1)
    def print(self) :
        for i in range(0, self.length, +1): 
            print(self.array[i], end = ' ' )
        print()

    def len(self) :
        return self.length    

arr = OrderedArray(6)
arr.insert(0)
arr.insert(1)
arr.insert(19)
arr.insert(25)
arr.insert(25)
arr.insert(-6)        
arr.insert(4)
arr.print()     
print("The length: " + str(arr.len()))   

#Search
key = 25
print("Found " + str(key) + " at index: " + str(arr.binary_search(key)))

#delete
arr.delete (-29)
arr.delete (0)
arr.print()    
print("The length: " + str(arr.len()))  

#insert again
arr.insert(8)
arr.print()
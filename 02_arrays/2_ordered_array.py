class OrderedArray:

    #Constructor, Time O(1), Space O(1)
    def __init__(self, size):
        self.num_items = 0
        self.array = [None]*size
        self.maxSize = size

    #Add one element, Time O(n), Space O(1), n is array length
    def insert(self, value):
        if self.num_items == self.maxSize :
            print ("Reach max size, cannot add.")
            return
        i = self.num_items -1
        while i >= 0 and self.array[i] > value:
            self.array[i+1] = self.array[i]
            i -= 1
        self.array[i+1] = value
        self.num_items += 1

    #Delete by key, Time O(n), Space O(1)
    def delete(self, key) :
        del_index = self.binary_search(key)
        if del_index < 0 :
            print("Item not found, return")
            return
        for i in range (del_index, self.num_items-1, 1): 
            self.array[i] = self.array[i+1]
        self.num_items -= 1         
      
    #Binary search, Time O(logn), Space O(1)
    def binary_search(self, key) :
        low = 0
        high = self.num_items - 1	
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
        for i in range(0, self.num_items, 1): 
            print(self.array[i], end = ' ' )
        print()

    def num_of_items(self) :
        return self.num_items    

#test
ordered_array = OrderedArray(6)
ordered_array.insert(0)
ordered_array.insert(1)
ordered_array.insert(19)
ordered_array.insert(25)
ordered_array.insert(25)
ordered_array.insert(-6)        
ordered_array.insert(4)
ordered_array.print()     
print("The length: " + str(ordered_array.num_of_items()))   

#Search
key = 25
print("Found " + str(key) + " at index: " + str(ordered_array.binary_search(key)))

#delete
ordered_array.delete(-29) # non-existing value
ordered_array.delete(0)
ordered_array.print()    
print("The length: " + str(ordered_array.num_of_items()))  

#insert again
ordered_array.insert(8)
ordered_array.print()
print("The length: " + str(ordered_array.num_of_items()))  
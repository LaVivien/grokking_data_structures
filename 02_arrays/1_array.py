class Array:

    #Constructor, Time O(1), Space O(1)
    def __init__(self, size):
        self.num_items = 0
        self.array = [None]*size
        self.max_size = size

    #Add one element at back, Time O(1), Space O(1)
    def add(self, value) :
        if self.num_items == self.max_size :
            print ("Reach max size, cannot add.")
            return
        self.array[self.num_items] = value
        self.num_items += 1

    #Delete by key, Time O(n), Space O(1), n is array length
    def delete (self, key) :
        del_index = self.search(key)
        if del_index == -1 : 
            print("Item not found, return.")
            return        
        for i in range(del_index, self.num_items-1, 1):        
            self.array[i] = self.array[i+1]
        self.num_items -= 1

    #Search by key, return the index of the first found, Time O(n), Space O(1)
    def search(self, key) :
        for i in range(0, self.num_items, 1) : 
            if self.array[i] == key: 
                return i
        return -1

    #Print elements in array, Time O(n), Space O(1)
    def print(self) :
        for i in range(0, self.num_items, 1): 
            print(self.array[i], end = ' ' )
        print()

    #Return the number of items in the array, Time O(1), Space O(1)
    def num_of_items(self) :
        return self.num_items

#test
array = Array(5); 
array.add(3)
array.add(5) 
array.add(7)
array.add(1)
array.add(9)
array.add(6)
array.print()
print("The length: " + str(array.num_of_items()))

#search by key
key1 = 10
print("find index of " + str(key1) + ": " + str(array.search(key1)))
key2 = 7
print("find index of " + str(key2) + ": " + str(array.search(key2)))

#delete by key
array.delete(key2)
array.print()
print("The length: " + str(array.num_of_items()))



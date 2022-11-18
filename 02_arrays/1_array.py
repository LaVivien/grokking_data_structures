class Array:

    #Constructor, Time O(1), Space O(1)
    def __init__(self, size):
        self.length = 0
        self.array = [None]*size
        self.max_size = size

    #Add one element at back, Time O(1), Space O(1)
    def add(self, value) :
        if self.length == self.max_size :
            print ("reach max size!")
            return
        self.array[self.length] = value
        self.length += 1

    #Delete by key, Time O(n), Space O(1), n is array length
    def delete (self, key) :
        i = self.search(key)
        if i == -1 : 
            print("key not found!")
            return        
        for j in range(i, self.length-1, +1):        
            self.array[j] = self.array[j+1]
        self.length -= 1

    #Search by key, Time O(n), Space O(1)
    def search(self, key) :
        for i in range(0, self.length, +1) : 
            if self.array[i] == key: 
                return i
        return -1

    #Print array, Time O(n), Space O(1)
    def print(self) :
        for i in range( 0, self.length, +1): 
            print(self.array[i], end = ' ' )
        print()

    def len(self) :
        return self.length

array = Array(5); 
array.add(3)
array.add(5) 
array.add(7)
array.add(1)
array.add(9)
array.add(6)
array.print()
print(array.len())

#search by key
key1 = 10
print("find index of " + str(key1) + ": " + str(array.search(key1)))
key2 = 7
print("find index of " + str(key2) + ": " + str(array.search(key2)))

#delete by key
array.delete(key2)
array.print()
print(array.len())



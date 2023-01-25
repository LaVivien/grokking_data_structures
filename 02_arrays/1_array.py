class Array:

    #Constructor, Time O(1), Space O(1)
    def __init__(self, size):
        self.num_items = 0
        self.array = [None]*size
        self.max_size = size

    #Add one element at back, Time O(1), Space O(1)
    def add(self, value):
        if self.num_items == self.max_size:
            print ("Reach max size, cannot add.")
            return
        self.array[self.num_items] = value
        self.num_items += 1

    # get the item by index,Time O(1), Space O(1) 
    def get(self, index):
        return self.array[index]

    #Delete by key, Time O(n), Space O(1), n is array length
    def delete(self, key):
        del_index = self.search(key)
        if del_index == -1: 
            print("Item not found, return.")
            return        
        for i in range(del_index, self.num_items-1):        
            self.array[i] = self.array[i+1]
        self.num_items -= 1

    #Search by key, return the index of the first found, Time O(n), Space O(1)
    def search(self, key):
        for i in range(0, self.num_items): 
            if self.array[i] == key: 
                return i
        return -1

    #Print elements in array, Time O(n), Space O(1)
    def print(self):
        for i in range(0, self.num_items): 
            print(self.array[i])

    #Return the number of items in the array, Time O(1), Space O(1)
    def num_of_items(self):
        return self.num_items
    
    # sort using a simple bubble sort, Time O(n^2), Space O(1)
    def sort(self):
        for i in range(0, self.num_items):
            for j in range (0,  self.num_items-i-1) : 
                if self.array[j] > self.array[j+1]: 
                    self.swap(j, j+1)

    # swap two elements, Time O(1), Space O(1)
    def swap(self, i, j) :
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    #remove duplicates in place, Time O(n^2), Space O(1)
    def remove_dup_in_place(self) :
        self.sort()
        i = 0
        for j in range(0, self.num_items):
            x = self.array[j]
            if x != self.array[i]:
                i += 1
                self.array[i] = x           
        self.num_items = i+1

#test
if __name__ == '__main__':
    array = Array(10); 
    array.add(3)
    array.add(5) 
    array.add(7)
    array.add(1)
    array.add(5) 
    array.add(9)
    array.add(5) 
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

    #sort 
    array.sort()
    array.print()
    print("The length: " + str(array.num_of_items()))

    # remove duplicates
    array.remove_dup_in_place()
    array.print()
    print("The length: " + str(array.num_of_items()))


class Matrix :

	#constructor, Time O(m*n), Space O(m*n), 
    #m is number of rows, n is length of number of columns 
    def __init__(self, input) :
        self.rows = len(input)
        self.columns = len(input[0])
        self.matrix = [[0 for j in range(self.columns)] for i in range(self.rows)]
        for  i in range (0, self.rows):
            for j in range(0, self.columns):
                self.matrix[i][j] = input[i][j]     
	
	#Time O(1), Space O(1)
    def update_cell(self, r, c, value) :
        self.matrix[r][c] = value
	
	#Search in un-sorted matrix, Time O(m*n), Space O(1)
    def search_matrix(self, key) :
        for i in range(0, self.rows) :
            for j in range (0, self.columns):
                if self.matrix[i][j] == key:
                    return [i, j]
        return [-1,-1]
	
	#Search in sorted matrix, two pointers, Time O(m+n), Space O(1)
    def search_sorted_matrix(self, key):
        row = 0
        col = len(self.matrix[0]) - 1
        while row < self.rows and col >= 0: 
            if (self.matrix[row][col] == key) :
                return [row,col]
            elif (self.matrix[row][col] < key) :
                row += 1 
            else : 
                col -= 1 
        return [-1,-1]
	
	#print matrix, Time O(m*n), Space O(1)
    def display(self):
        for i in range(0, self.rows) :
            s = ''
            for j in range (0, self.columns):    
                s += str(self.matrix[i][j]) + ' '
            print(s)
	    
# test
input = [[ 1,  3,  5,  7,  9],
         [11, 13, 15, 16, 20],
         [21, 22, 23, 24, 25],
         [30, 32, 35, 40, 45]]

matrix = Matrix(input)
matrix.display()

#search
key = 15
b = matrix.search_matrix(key)
print("Find "+ str(key) + " (linearsearch) at: " + str(b[0]) + "," + str(b[1]))

b1 = matrix.search_sorted_matrix(key)
print("Find "+ str(key) + " (binary search) at: " + str(b1[0]) + "," + str(b1[1]))
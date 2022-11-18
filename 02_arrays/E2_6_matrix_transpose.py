#Write a function to output the transpose of a matrix.

#Time O(mxn), Space O(nxm)
def transpose(x) :
    rows = len(x)
    cols = len(x[0])
    y = [[0 for j in range(rows)] for i in range(cols)]
    for j in range(0, cols):
        for i in range(0, rows):
            y[j][i] = x[i][j]
    return y

# test
board =[[1,8,3,5],
        [4,1,3,3],
        [2,2,1,5]]
t = transpose(board)
for i in range(0, len(t)) :
    s = ''
    for j in range (0, len(t[0])):    
        s += str(t[i][j]) + ' '
    print(s)

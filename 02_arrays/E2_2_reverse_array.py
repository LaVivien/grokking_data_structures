#Write a function to reverse an array of numbers

#Use extra array, Time O(n), Space O(n)
def reverse_array(arr) :
    n = len(arr)
    result = [None]*n # extra array
    j = n-1       
    for i in range(0, n):
        result[j] = arr[i]
        j -= 1
    return result

# test reverse numbers
arr =[4, 2, 5, 2, 6]
rev = reverse_array(arr)
print(rev)

# test reverse string
str = "String"
str_array = list(str) # convert string to list of characters
rev_str = reverse_array(str_array) 
print(rev_str)

#test reverse words
words = "This is a string"
words_array = words.split(' ') #convert string into list of string
rev_words = reverse_array(words_array) 
print(rev_words)

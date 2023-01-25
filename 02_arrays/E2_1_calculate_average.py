# calculate the average of the numbers in an array.

# use Array class, Time O(n), Sapce O(1)
my_array = __import__('1_array')
def get_average_array(arr):
    count = arr.num_of_items()
    sum = 0
    for i in range(0, count):
        x = arr.get(i)
        sum += x
    return sum/count

#test use Array class
grade_array = my_array.Array(5)
grade_array.add(14)
grade_array.add(28)
grade_array.add(33)
grade_array.add(16)
grade_array.add(5)
print(get_average_array(grade_array))




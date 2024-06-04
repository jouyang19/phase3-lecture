# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# simple for loop (no indices)
# for item in my_list:
#     print(item)

## For loops with indices

# range(start index, end index)
# for i in range( 0 , 5 ):
#     print(i, my_list[i])

# Using len() instead of -1 to iterate over whole list
# for i in range( 0 , len(my_list) ):
#     print(i, my_list[i])
    
## map
# my_list = [ 1, 2, 3, 4, 5]

# def double(numbers):
#     """Double every number in numbers"""
#     new_list = [] # create empty list
#     for num in numbers: # loop over every num
#         new_num = num * 2 # transforming the number
#         new_list.append(new_num) # add to new list
#     return new_list

# print(my_list)
# print(double(my_list))
        
    
## filter
# my_list = [ 1, 2, 3, 4, 5, -1, -2, 6, 7, -8]

# def get_pos(numbers):
#     """Returns a new list with negative numbers filtered out"""
#     new_list = [] # create empty list
#     for num in numbers: # loop over existing list
#         if num > 0: #check condition
#             new_list.append(num) # add num to new list   
#     return new_list

# print(my_list)
# print(get_pos(my_list))
        

my_list = [
        {
        'name': 'David',
        'age': 12
    },
    {
        'name': 'joe',
        'age': 55
    },
        {
        'name': 'Anne',
        'age': 48
    }
]

current_max = my_list[0] # using default value of my_list[0] to avoid NoneType error when using None as value
for current_item in my_list:
    if current_item['age'] > current_max['age']: 
        current_max = current_item
        
print(current_max)
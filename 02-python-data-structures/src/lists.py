my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# TODO Test if an element exists in `my_list`
'a' in my_list
# TODO Add element to the end
my_list.append('h')
# TODO Insert element at an index
# my_list.insert(index, value)
my_list.insert(0, 'X')
# TODO Merge two lists together
[ 1 , 2 ] + my_list
[ 1 , 2 ] + [ 3 , 4 ]
# TODO Duplicate a list
copy = my_list.copy()
# TODO Index lookup
# array[index]
my_list[2] # = c
my_list[-1] # = g
# TODO Slice
# my_list[index start:index end]
my_list[0:3] # = ['a', 'b', 'c']
# TODO Get length
len(my_list) # = 7
# TODO Get min/max
min(my_list)
max(my_list)
# TODO Find index of an element
# my_list.index('element') Only finds first instance
my_list.index('g') # = 6
# TODO Count number of instances of an element
# my_list.count('element')
my_list.count('b')
# TODO Remove element from list
my_list.pop() #removes last element from my list
my_list.pop(0) # my_list.pop(index) removes element from index
# TODO Sorting (with and without a key)

# TODO sorted() vs .sort()
my_list.sort() # sorts the list in place
my_list.sort( reverse = True ) # to reverse the sort order
sorted(my_list, reverse=True) # Makes a copy and sorts in reverse order; Does not mutate original list
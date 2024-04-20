import array
arr = array.array("f", (1.0, 1.5, 2.0, 2.5))
print(arr[1])
print(arr[2])
print(arr[0])

# list 
# use square bracket [] 
# mutable, can have any data types
# list() - list constructor
list_example = list(('this', 'is', 'a', 'list'))
print(list_example)

this_list = ['apple', 'banana', 'orange', 'apple']
print(this_list)

# tuple 
# use round bracket ()
# ordered, unchangeable, allows duplicates
# tuple with one item tuple - remember the comma after the item
tuple1 = (1, ) 
tuple2 = (1 ) 
print(tuple1)
print(type(tuple2))
# any data types
tuple_mix = (1, 'hi', True)
print(tuple_mix)
# tuple(()) - tuple constructor
this_tuple = tuple((1,2,3,4))
print(this_tuple)
print(len(this_tuple))
print(type(this_tuple))

# set 
# unordered, unchangeable, unindexed, but can remove or add items
# no duplicates allowed (False and 0 are treated the same, True and 1 are treated the same) 
#  can have different types of data in a set 

thisset = {"apple", "banana", "cherry"}
set1 = {True, 1, 0, False}

print(thisset)
print(set1)
print(len(set1))

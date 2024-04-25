thisset = {"apple", "banana", "cherry", True, 1, 2, 0, False}

print(thisset)


#set constructor 
set_ex_1 = set(("this","is","another","set"))
print(set_ex_1)

fruits_set = {"apple", "banana", "cherry"}

for fruit in fruits_set:
    print(fruit)

print("banana" in fruits_set)
print("coconut"  in fruits_set)

#add an item 
fruits_set.add("watermelon")
print(fruits_set)

food_list = {"rice", "noodles", "beef"}
fruits_set.update(food_list)
print(fruits_set)

# joining sets

set1 = {"a", "b", "c"}
set2 = {1,2,3}
# set3 = set1.union(set2) 
# set3 = set1 | set2 
# print(set3)
print(set1)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
# new_set = set1 | set2 | set3 | set4 
new_set = set1.union(set1, set2, set3, set4)
print(new_set)

type_set = { 1,2,3,4,5} 
type_set2 = type_set.copy()
type_set2.add(9)
print(type_set2)
print(type(type_set2))
type_list = ["one", "two", "three"]

set_list_combo = type_set.union(type_list)


print(set1.isdisjoint(set2))
# nested loops

nums = [1,2,3,4,5]
str_1 = 'abcde'
# for num in nums:
#     for letter in str_1: 
#         if letter == 'c':
#             print('skip')
#             continue
#         print(num, letter)

# for num in nums: 
#     while num < 4: 
#         for letter in str_1:
#             print(num, letter)
#         num +=1 

# for i in range(len(nums)): 
#     print(nums[i])

thislist = ["apple", "banana", "cherry"]
# i = 0 
# while i < len(thislist): 
#     print(thislist[i])
#     i += 1

#list comprehension 
# [print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

newlist = [x for x in fruits if "o" in x]
print(newlist)
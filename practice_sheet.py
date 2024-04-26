# print(type(3.0))

# a = 1
# A = 2 
# print(a)
# print(A)

# my_list = ("apple", "banana", "orange")
# x,y,z = my_list
# print(x, y, z)
# print(my_list)

# y = 2.8 
# z = int(y)
# print(z)

# import random
# print(random.randrange(1,10))

# txt = "Hello World"
# x = txt[2:2]
# x = txt[2:3]
# x = txt[2:4]
# x = txt[2:5]
# print(x)
# new_txt = " This is a test. "
# print(new_txt)
# print(new_txt.strip())

courses = ['History', 'Math', 'Physcis', 'CompSci']

# print(courses)
# courses.reverse()
# print(courses)
courses.sort()
print(courses)
courses.sort(reverse = True)
print(courses)
# courses.insert


# print('Math'in courses)
# print('Math'in courses)

# for subject in courses:
#     print(subject)

# for index,subject in enumerate (courses):
#     n1 , n2 = index, subject 
#     print("The index: % s, and % s" % (n1, n2))

# courses_list = ['History', 'Math', 'Physcis', 'CompSci']
# courses_str = ' - '.join(courses_list)
# print(courses_str)
# new_courses_list = courses_str.split(' - ')
# print(new_courses_list)


# '''
# .intersection(), .difference(), .union() methods
# '''

# course_set1 = {'History', 'PE', 'Art', 'English'}
# course_set2 = {'PE', 'Math', 'Chemistry'}

# print(course_set1.intersection(course_set2))
# print(course_set1.difference(course_set2))
# print(course_set1.union(course_set2))

# print('Math' in course_set2)
# # course_set1.pop()
# # course_set1.add("Math")
# print(course_set1)
# print(len(course_set1)) # 4
# print(len(course_set1.intersection(course_set2))) # 1
# print(course_set1.intersection(course_set2))
# print(len(course_set1.difference(course_set2))) # 3
# print(course_set1.difference(course_set2))
# print(len(course_set1.union(course_set2))) # 6


#make a for loop using index i 
alist = ["a", "b", "c", "d", "e"]
for i in range(len(alist)): 
    print(alist[i])

#make a for loop using list comprehension
blist = ["x1", "y", "z1"]
blist_new = [ letters for letters in blist if "1" in letters]
print(blist_new)

#make a while loop 
clist = ["1a","2b","3c","4d","5e","6f","7g"]
i = 0 
while i < len(clist): 
    print (clist[i])
    i += 1 


my_list = [ "basketball", "soccer", "football", "waterpolo"]
# ball_list = [sports for sports in my_list if "ball" in sports]
# ball_list2 = [sports for sports in my_list if True]
ball_list2 = [ reply if reply == "basketball" else "no" for reply in my_list]
# print(ball_list)
print(ball_list2)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1.append(list2)

print(type(list3))
print(list3)
print(type(list1))
print(list1)

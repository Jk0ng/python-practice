student = {'name': 'Joseph', 'age': 25, 'courses': ['Math', 'CompSci'] }

student['phone'] = '555-555-5555'
print(student)
student.update({'name': 'Joseph Kong', 'age': 26}) # update several k:v pairs at the same time

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
   
    print("This is the %s: %s pair " % (key, value)) #modulo string formatting
    print(f'This is the {key} and {value}')  # f string string-interpolation



del(student['phone']) # delete a key:value pair
course_taking = student.pop('courses') # use a .pop() method to remove a key:value pair and set it to a variable
# print(course_taking)
# print(student)
# print(student['name'])
# print(student.get('name'))
# print(student.get('phone', 'Not Found'))


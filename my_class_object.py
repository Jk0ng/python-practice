class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self): 
        print("My name is " +  self.name + ", and my age is " + self.age)

a = Person("joseph", "25")
print(type(a))
print(a.name)
print(a.age)
a.my_func()
print( 0 % 3 )
print( 1 % 3 )
print( 2 % 3 )
print( 3 % 3 )
print([-1] * 3)

class Parent: 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self): 
        print(self.first_name, self.last_name)

x = Parent("Joseph", "Kong")
x.print_name()

class Child(Parent):
    pass

y = Child("Kong", "Joseph")
y. print_name()
    
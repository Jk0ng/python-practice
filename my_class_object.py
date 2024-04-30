# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def my_func(self): 
#         print("My name is " +  self.name + ", and my age is " + self.age)

# a = Person("joseph", "25")
# print(type(a))
# print(a.name)
# print(a.age)
# a.my_func()
# print( 0 % 3 )
# print( 1 % 3 )
# print( 2 % 3 )
# print( 3 % 3 )
# print([-1] * 3)

# class Parent: 
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def print_name(self): 
#         print(self.first_name, self.last_name)

# x = Parent("Joseph", "Kong")
# x.print_name()

# class Child(Parent):
#     pass

# y = Child("Kong", "Joseph")
# y. print_name()
    
class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w

    def introduce_self(self):
        print("My name is " + self.name)

class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.isSitting = i

    def sit_down(self):
        print("My name is " + self.name)


r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "aggressive", True)

p1.robot_owned = r2
p2.robot_owned = r1


p1.robot_owned.introduce_self()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_nodes(head):
    current_node = head
    count = 1 
    while current_node.next is not None:
        current_node = current_node.next
        count += 1
    return count

a = Node(6)
b = Node(3)
c = Node(4)
d = Node(2)
e = Node(1)
f = Node(1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
print(count_nodes(a))
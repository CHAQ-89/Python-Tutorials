class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def print_name(self):
        print(self.fname, self.lname)
person = Person('Chu', 'Quyet')
person.print_name()
class Student(Person):
    def __init__(self, fname, lname, age):
        #Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.age = age
    def welcom(self):
        print(f'Welcom {self.fname} {self.lname}, {self.age} year old')
person = Student('Chu', 'Thien Minh', 2)
person.welcom()

# class First:
#     def getClass(self):
#         print("Class Fist")
#         super().getClass()

# class Second:
#     def getClass(self):
#         print("Class Second")
        
# class Third(First, Second):
#     def getClass(self):
#         super().getClass()

# third = Third()
# third.getClass()
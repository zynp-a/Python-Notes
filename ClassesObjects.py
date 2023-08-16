class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def greeting(self):
        print("Hi, my name is", self.name)


p1 = Person("Zeynep", 22)

print(p1.name)  # Zeynep
print(p1.age)  # 22

p1  # Zeynep(22)

p1.greeting()  # Hi, my name is Zeynep


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        # Person.__init__(self, name, age)


s1 = Student("Jane", 27)
s1  # Jane(27)

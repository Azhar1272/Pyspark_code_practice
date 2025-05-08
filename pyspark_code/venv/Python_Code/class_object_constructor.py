# creating class
class car:
    
    # initialize constructor
    def __init__(self, number):
        self.double_number = number * 2
        self.triple_number = number * 3

    # Method 1
    def double_result(self):
        print(f"convert to double {self.double_number}")

    # Method 2
    def triple_result(self):
        print(f"convert to triple {self.triple_number}")

    
# Create objects (instances)
o = car(5)

# Use objects
o.double_result()


'''Example 2'''
class Field:
    def __init__(self):
        self.__value = None

    def get_value(self):
        """
        Returns the current value of the field.
        """
        return self.__value

    def set_value(self, new_value):
        """
        Sets a new value to the field.
        """
        self.__value = new_value


f = Field()
f.set_value(42)
print(f.get_value())  # Output: 42

'''Example 3'''

class SchoolMember:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show(self):
        raise NotImplementedError("Subclasses must implement this method")


class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades: int):
        super().__init__(name, age)
        self.grades = grades

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"


teacher = Teacher("Mr.Snape", 40, 3000)
print(teacher.name)  # "Mr.Snape"

persons = [teacher, Student("Harry", 16, 75)]

for person in persons:
    print(person.show())



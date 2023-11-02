class Student:
    amount_of_students = 0
    print("Hi")
    def __init__(self, height=160):
        self.height = height
        print(self)
        Student.amount_of_students +=1
    def grow(self, height=1):
        self.height+=height


Jax= Student()
Lili = Student(height = 170)
Jax.grow(height=15)
print(Jax.amount_of_students)
print(Student.amount_of_students)
print("Jax", Jax.height)
print("Lili", Lili.height)

first_student = Student()
Student.__init__(self = first_student)





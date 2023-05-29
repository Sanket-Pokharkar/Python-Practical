# This is an example of non parameterized construtor
print("hello ")
class student():
    count=0
    def __init__(self):
        student.count=student.count+1

v1= student()
v2 = student()
v3 = student()
v4 = student()
print("The no of object in class is ",student.count)
                    
            
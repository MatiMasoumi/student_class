class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.grades=[]

    def add_grade(self,grade):
        """
        add grade to the grades list
        """
        if 0<=grade<=100:
            self.grades.append(grade)
        else:
            print('Grade must between 0 and 100.')
    def calculate_average(self):
        """
        calcukate the average of grades.
        """
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def display_details(self):
        """
        Display student details
        """
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Grades:{self.grades}")
        print(f"Average grade:{self.calculate_average():.2f}")
        
if __name__=="__main__":
    Student1=Student('Alice',20)
Student2=Student('Bob',22)

Student1.add_grade(85)
Student1.add_grade(90)
Student1.add_grade(78)

Student2.add_grade(92)
Student2.add_grade(88)
Student2.add_grade(78)

Student1.display_details()
print()
Student2.display_details()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"the name of person is :{self.name}\nage is :{self.age}")
class Student(Person):
    def __init__(self,name,age,roll_no,cgpa):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.cgpa=cgpa
    def display(self):
        super().display()
        print(f"Rollno is :{self.roll_no}\ncgpa is :{self.cgpa}")
class GraduateStudent(Student):
    def __init__(self,name,age,roll_no,cgpa,research_topic,supervisor):
        self.research_topic=research_topic
        self.supervisor=supervisor
        super().__init__(name,age,roll_no,cgpa)
    
    def display(self):
        super().display()
        print(f"the research topic is :{self.research_topic}\nSupervisor is :{self.supervisor}")
       
gs=GraduateStudent(
                  "basil",
                   19,
                   54,
                   3.7,
                   "ML",
                   "dr.Ahmed")
gs.display()
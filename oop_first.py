class Student:
    def __init__(self,name,age,clas):
        self.ism = name
        self.yosh = age
        self.sinf = clas
    
    def printinfoofstudent(self):
        print(f"""
        Name : {self.ism}
        Age: {self.yosh}
        Class: {self.sinf}
        """)


student1 = Student("Aziz",15,5)
student2 = Student("Qodir",45,7)

student1.printinfoofstudent()
student2.printinfoofstudent()

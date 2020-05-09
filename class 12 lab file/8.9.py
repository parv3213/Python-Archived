import pickle
class Student:
    def __init__(self,rno=0,name=" "):
        self.rollno=rno
        self.name=name
        self.marks1,self.marks2,self.marks3=0.0,0.0,0.0
    def readMarks(self):
        print "Enter marks of 3 subject"
        self.marks1=float(raw_input("Subject1:"))
        self.marks2=float(raw_input("Subject2:"))
        self.marks3=float(raw_input("Subject3:"))
    def display(self):
        print "Students details are:"
        print "Roll number :",self.rollNo
        print "Name :",self.name
        print "Marks in 3 subjects :",self.marks1,self.marks2,self.marks3
stud1=Student(13,"Rohan")
stud2=Student(15,"Nitya")
stud1.readMarks()
stud2.readMarks()
file1=open("student1.log","wb")
pickle.dump(stud1,file1)
pickle.dump(stud2,file1)
file1.close()

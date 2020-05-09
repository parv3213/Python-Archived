import pickle
class student:
     def __init__(self,rno=0,name=""):
          self.nollno=rno
          self.name=name
          self.marks1,self.marks2,self.marks3=0.0,0.0,0.0

     def readmarks(self):
          print "Enter marks of 3 subjects"
          self.marks1=float(raw_input("Suject1:"))
          self.marks2=float(raw_input("Suject2:"))
          self.marks3=float(raw_input("Suject3:"))
          

     def display(self):
          print "Student detials are"
          print "Rollno:",self.rollno
          print "Name:",self.name
          print "Marks in 3 sujects:",self.marks1,self.marks2,self.marks3
stud1=student(13,"Rohan")
stud2=student(25,"Nitya")
stud1.readmarks()
stud2.readmarks()
file1=open("student1.log","wb")
pickle.dump(stud1,file1)
pickle.dump(stud2,file2)
file1.close()

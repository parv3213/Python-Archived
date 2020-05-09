class Student:
    num_of_students=0
    Class_teacher="Mrs. David"
    def __init__(a,rno,name,mks):
        a.rollNo=rno
        a.name=name
        a.marks=mks
        a.grade=""
        Student.num_of_students+=1
    def calcGrade(a):
        if a.marks>=80:
            a.grade="A+"
        elif a.marks>=70:
            a.grade="A"
        elif a.marks>=60:
            a.grade="B"
        elif a.marks>=50:
            a.grade="C"
        elif a.marks>=40:
            a.grade="D"
        else:
            a.grade="E"
#Main
stud1=Student(12,"Nitin",68.5)
stud2=Student(14,"Joseph",80.25)
stud3=Student(16,"Zain",59.5)
stud4=Student(18,"Nimrat",47.5)

print "Student' details recorded so for for",Student.num_of_students,"students"

stud1.calcGrade()
print "Grade of rollnumber",stud1.rollNo,"-",stud1.name,"is:",stud1.grade
stud2.calcGrade()
print "Grade of rollnumber",stud2.rollNo,"-",stud2.name,"is:",stud2.grade

stud3.calcGrade()
print "Grade of rollnumber",stud3.rollNo,"-",stud3.name,"is:",stud3.grade
stud4.calcGrade()
print "Grade of rollnumber",stud4.rollNo,"-",stud4.name,"is:",stud4.grade




        
        

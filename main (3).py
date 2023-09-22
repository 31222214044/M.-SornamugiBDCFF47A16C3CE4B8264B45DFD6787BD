class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
def sort_student(student_list):
#sort the list of students in descending order of cgpa 
   sorted_students  = sorted(student_list,
                             key= lambda  student: student.cgpa,
                             reverse=True)
   return sorted_students
# example usage
students = [Student("riya","A123",7.8),
            Student("kavi","A124",8.5),
            Student("abi","A125",9.2),
            Student("keerti","A126",9.9)]
sorted_students = sort_student(students)
#print the sorted list of student 
for student in sorted_students:
   print("Name:{},Roll Number:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))
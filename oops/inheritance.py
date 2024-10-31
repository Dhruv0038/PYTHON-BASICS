class Employee:
    company="amazon"
    def show(self):
     print(f"The name of the employer is {self.company}")

class skills:
   language="python"
   language2="java"
   def show2(self):
      print(f"The languages known by the employee are {self.language} , {self.language2}")

class programmer(Employee, skills): # this is an example of inheritance and multiple inheritance as one class here have multiple parent classes
   company="aws"
   def showlanguage(self):
      print(f"The name of the company is {self.company}. The language of the programmer is {self.language}")

class salary(programmer): # this is an example of multilevel inheritance as this takes content from another class programmer and that class is taking content from two other classes
   salary= 4000000
   def sal(self):
      print(f"The salary of the employee is {self.salary}")





# a= programmer()
# print(a.showlanguage())
# b=Employee()
# b.show()
c= salary()
c.sal()
c.show2()
c.show()
c.showlanguage()

class Employee:
  def __init__(self):
    print("constructor of employee")
  a=1

class Programmer(Employee):
  def __init__(self):
    print("constructor of programmer")
  b=2

class Manager(Programmer): 
  def __init__(self):
    super().__init__() #this here will print the constructor of the super class too like here the constructor of both Programmer class and Manager class will be printed but without this statement there will be no constructor of Programmer in the output 
    print("constructor of manager")
  c=3

o=Employee()
print(o.a)

o=Programmer()
print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)
   
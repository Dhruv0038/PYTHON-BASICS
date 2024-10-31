class Employee:
  a=1
  @classmethod
  def show(cls):
      print(f"The class attribute of a is {cls.a}")


e=Employee()
e.a=45
e.show()
"""
the classmethod helps in fixing the value of an attribute to
a particular which is given in the class and not in the object
so using this the value of that attribute will stay the same as 
in the class even if we specify it in the object.
"""
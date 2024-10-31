class employee:
    language ="py"
    salary= 12000000
   
    def __init__(self, name, salary ,language): # this is a dunder method which is automatically called when you make a new object of one class
        self.name= name
        self.salary= salary
        self.language= language

    def getinfo(self):#you can use anything other than self here as it is just to parameterise without self it give error as we would have written getinfo() which is empty and when we try to call it ,it will be like employee.getinfo(dhruv) where we have given a parameter so it wont work as we have not taken parameterised function so self is like a variable
      print(f"the language is {self.language}.the salary is {self.salary}")

    @staticmethod#static method is used when we are not using any instance attribute or not using any self
    def hello():
       print("hello")

# dhruv =employee()

# dhruv.name ="Dhruv Singh Solanki"

# print(dhruv.name,"\n", dhruv.language)
"""here name is an object attribute (instance attribute) but salary and
language are class attributes because they directly belong
to the 
and instance attribute is always given prference over the 
class attribute
"""
# dhruv.language="java"
# employee.getinfo(dhruv) # dhruv.getinfo() also same thing if we write this then also it will be converted to employee.getinfo(dhruv)
 


nanao = employee("nanao", 2000000, "java")
print(nanao.name, nanao.salary, nanao.language)
nanao.hello()

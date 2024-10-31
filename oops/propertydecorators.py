# this also shows the concept of abstraction and encapsulation
class Employee:

  @property
  def name(self):
    return f"{self.fname} {self.lname} {self.lname2}"
  
  @name.setter
  def name (self,value):
    self.fname=value.split(" ")[0]# the split helps in spliting the contents of a string and store them in a list  , the [0] specifies the indexing the split occurs at " " or at space
    self.lname=value.split(" ")[1]
    self.lname2=value.split(" ")[2]

e=Employee()
e.name="Dhruv Singh Solanki"
print(e.fname, e.lname ,e.lname2)
"""
here we just take the namee of a person as it is and then
convert it to first name lastname and lastname2 then we 
can get any of these by printing separately as we stored them separately
"""
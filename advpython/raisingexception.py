# a= int(input("enter a number:"))
# b= int(input("enter second number:"))

# if(b==0):
#     raise ZeroDivisionError("Hey our program is not meant to divide a number by zero")
# else:
#     print(f"The division of a/b is {a/b}")


try:
  a= int(input("Hey, Enter a number:"))
  print(a)

except ValueError as v: # the except is catch in c programming language
  print(v)
  print("value error")

else:# this else will only run if our try statement runs ,if the except runs then the else wont run
   print("we are inside the else")

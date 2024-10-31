try:
  a= int(input("Hey, Enter a number:"))
  print(a)

except ValueError as v: # the except is catch in c
  print(v)
  print("value error")


except Exception as e :
   print("Thank you")


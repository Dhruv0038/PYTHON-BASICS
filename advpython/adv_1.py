# walrus operator
# if(n:= len([1,2,3,4,5])) > 3: # this helps in assigning two values like here we take the value of n= length of the string and then see if it is grater than 3 or not
#     print(f"List is too long ({n} elements, expected<=3)")


# # externally specifying the type of any variable in python
# n: int = 5
# name: str ="Dhruv"

# def sum(a: int, b:int) -> int: # this takes a and b as integer and then return an int value
#     return a+b

# # #  match case condition
# def http_status(status):
#     match status:
#         case 200:
#             return "ok"
#         case 484:
#             return "not found"
#         case 500:
#             return "Internal server error"
#         case _:
#             return "unknown status"
        
# print(http_status(200))

# merging a dictionary
# dict1={"a":1 , "b":2}
# dict2={"b":3,"c":4}
# merged= dict1|dict2
# print(merged)

   

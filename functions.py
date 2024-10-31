# def avg(): #function definition
#     a= int(input("enter the first number: "))
#     b= int(input("enter the second number: "))
#     c= int(input("enter the third number: "))

#     average = (a+b+c)/3
#     print(average)
    # return "al capone"
    # return average # here i use this to stor the value of average in a variable which on looking below you will find is a

# a=avg() # here a will store whatever return value you use
# print(a)

# avg() #function call

#  parameterised functions
# def greeting1( name , ending):
#     print("good day,"+ name)
#     print(ending)
    # return "all good"# without this return the function wont give any value (it will give out "none" in terminal) if it is put inside another variable, but now it will return a value if  put inside another variable which will be the original function value with the value in return and for here it is all good
    
# greeting1( "Dhruv" , "thank you") 
# greeting1("garry", "welcome")
# a = greeting1("kyouichiro","passout")
# print(a)

# default argument
# def greeting2( name , ending="thank you"): # here ending is by default thank you so it is a default argument , will only be printed if there is no user given argument for the function 
#     print(f"good day, {name}")
#     print(ending)

# greeting2("light", "go away")# here if the value is given by the user so the output will show user value else it will show default value
# greeting2("light")


# def rem(l, word):
#     n=[]
#     for item in l:
#         if not(item==word):# not keyword used for indicating of negation like here we are trying to say that if item is not equal to word
#             n.append(item.strip(word))# strip used to remove that particular item from the strings in the list
#     return n

# l=["lou","loid","arcane","cane"]
# print(rem(l,"ou"))

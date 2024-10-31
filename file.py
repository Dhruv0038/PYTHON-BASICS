import random
# from random import randint you can use this to directly use the randintt function and not use it like random.randint()
# f=open("filesample.txt")
# data= f.read()
# print(data)
# f.close()

""" the code below will crearte a file of given name and 
open it in write mode by use of the "w"
and then write the desired content in that file 
then close it so if you now look you will have a file created 
into your folder which has the sentence in it that is written in the st
"""
# st= "Hey jin you are amazing"
# f = open("file.txt","w")
# f.write(st)
# f.close()
# f=open("file.txt")
# data= f.read()
# print(data)
# f.close()

# f=open("file.txt")
# print(f.read())
# f.close()  

# #same can be written using with statement like this:
# with open("file.txt") as f:
#     print(f.read())

# # you dont have to explicitly close the file here

# print(random.randint(1,34)) # here the randint allows us to choose a random number from the upper given limit to lower given limit which here is 1 and 34 but we got to use it with the random module

# code to find a word in a file and return on which line it is present
# file_name = "file.txt"
# word = "hello"

# with open(file_name, 'r') as file:
#     lines = file.readlines()
#     for num, line in enumerate(lines, 1): # enumerate gives us the value like a tuple for eg if we want the line number and the line with it it will give us (1 ,"line 1") so because of that we gave the num and line in enumerate so the number will be stored into num and the line will be the line. Enumerate is just a built in function of python that give the numbering and we can specify from where the numbering starts like here we have given 1 as a starting no. if we have given 2 then it would start counting from 2
#         if word in line:
#             print(f"Word '{word}' found at line {num}")
#             break
#     else:
#         print(f"Word '{word}' not found in the file")


file_name="file.txt"
word="hello"
with open (file_name,"r") as file:
    for num , line in enumerate(file, 1):
        if word in line:
            print(f"The word {word} is present  , in the line number {num}")
            break
    
    else:
            print(f"the word {word} is not present in the file")

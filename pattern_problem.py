#problem1
# i=int(input("enter number of rows:"))
# for  i in range (1,i+1):
#         print(i*"*")

#problem2
# i=1
# print(i,end=" " ) #the end=" "stops the print statement from switching to a new line and helps in printing both the space and * in the same line

# n= int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     print(" "* (n-i),end="")
#     print("*"*(2*i-1), end="")
#     print("")

# problem3
n=int(input("enter the number:"))
for i in range(1,n+1):
    if (i==1 or i==n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")
        



    

   
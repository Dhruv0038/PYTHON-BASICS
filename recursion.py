#  recursion is a function calling itself again and again for eg:-
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n* factorial(n-1)
    
# n= int(input("enter a number: "))
# print(f"the factorial for the given number is ,{factorial(n)}")
''' what recursion is doing here
if n=5 then it goes like this in recursion
5 * factorial(5-1)
5*4*factorial(4-1)
5*4*3*factorial(3-1)
5*4*3*2*factorial(2-1)
5*4*3*2*1 now as we already defined thst if n=1 or 0 
so the function should return 1 so it will return 1 and stop here
'''
def sumofnumbers(n):
    if(n==0 or n==1):
        return n
    else:
        return( n + sumofnumbers(n-1))
    
n= int(input("enter a number: "))
print(f"The sum of the first {n} digits of the natural number group is, {sumofnumbers(n)}")
    


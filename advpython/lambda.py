# def square(n):
#     return n*n
   

# square = lambda x: x*x # single variable
# sum = lambda a,b,c: a+b+c# multi variable
# print(square(5))
# print(sum(1,2,3))


# a=["Dhruv", "Rahul", "Ravi"]
# final="::".join(a)
# print(final)

# map example
l=[1,2,3,4,5]
m=[1,2,3,4,5]
n=[1,2,3,4,5]

square= lambda a,b,c: a+b+c

sqlist = map(square,l,m,n)
print(list(sqlist))

#  filter example
# def even(n):
#     if (n%2 == 0):
#         return True
#     return False

# onlyeven = filter(even,l)
# print(list(onlyeven))

# l=[1,2,3,4,5]

# square= lambda x: x*x

# sqlist = map(square,l,m,n)
# print(list(sqlist))


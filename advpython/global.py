a=83 # this is a global variable
def fun():
    # global a # if we write global a here then this a becomes global variable which means a's value will remain 3 until specified
    a=3 # this is a local variale which is unique to the function
    print(a)

fun()
print(a)
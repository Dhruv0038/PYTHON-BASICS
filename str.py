a= 'abcd'
b="abcd"
c='''multi line 
string'''
print(a.endswith("cd"))
print(a.startswith("ab"))
name = input("enter your name  ")
print(f"good afternoon {name}" ) #we have to put an f before string if we want it to show some input taken by console
# you can replace string elements by using .replace function
print(a.replace("a","b"))# should give the output bbcd
#  string are immutable which means you can not change them by running functions on them the function chang ethe sting for that moment only
# but if you try to print that sting again by using its name then that will give you the same unchanged string


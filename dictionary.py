dic1={
    "a1": 44,
    "a2":45,
    "\"a3\"":46,# this is how to print double quotes in python
}
print(dic1, type(dic1))
print(dic1["a1"])
print(dic1.get("apple"))# returns none
print(dic1["apple"])# gives error
# dictionary is mutable
s={1,2,3}# this is a set it is just like dictionary but does not have the key value pair and have simple objects 
e= set() #an empty set
c={}# this is an empty dictionary
# set does not have repeating elements
# list are mutable which means that they will change if a change is made in them
# they will be changed fully and will not print the unchanged list if they are given the print command 
l1= ["black","orange","blue","red","white"]
print(l1[0])
print(l1[1:3])
l1.append(12345)
print(l1)
l1.insert(5, 345)
print(l1)
l1.pop(2)
print(l1) 


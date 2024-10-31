try:
    a= int(input("Enter a number:"))
    print(a)


except Exception as e:
    print(e)


finally: # finally always runs whether we go in except of run in try but then what is the difference between the finally and a normal print statement at the end that too will always run. The main difference arises when we write an exception in a function it wont run a normal print statement at the end then but if we put something in the finally block it will always come out in output in that function  
    print("We are inside finally")
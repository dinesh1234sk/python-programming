name=input("enter your name:")

print("hello,"+name+"!")

age=int(input("enter your age:"))
print("you will be ",age+1,"next year")
price=float(input("enter the price"))
discount=price*0.1
print("discount is:,",discount)


answer=input("are you a student?yes or no?")
is_student=answer=="yes"
if is_student:
    print("welcome student")
else:
    print("hello guest")

def greet():
    print("welcome to python functions!")
greet()
greet()
greet()
def greet_user(name):
   print("hello",name)
greet_user("ramesh")
greet_user("dinesh")
greet_user("raj")
def square(num):
    return num*num
result=square(6)
print("square:",result)
result=square(6)
print("square:<result")
print(square(10))
print(square(100))
def get_max(a,b):
    if a>b:\
        return a
    else:
        return b
max_value=get_max(40,50)
print("maximum:",max_value)
def greet_user(name):
    print("Hello,"+name+"!")
names=["alice","bob","charlie"]
for name in names:
    greet_user(name)
def greet_default(name="guest"):
    print("hello",name)
greet_default()
greet_default("ravi")
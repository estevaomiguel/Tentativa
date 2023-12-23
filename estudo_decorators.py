#Understanding fucntions

def hi(name = "yasoob"):
    return f"hi {name}"

print(hi())

greet = hi

print(greet())

del hi

print(greet())

#Defining functions inside other functions

def hi(name = "yasoob"):
    print("now you are inside hi() function")

    def greet():
        return "now you are inside greet() function"
    def welcome():
        return "now you are inside welcome() function"

    print(greet())
    print(welcome())
    print("Now your back in the hi() function")


hi()
#This shows that when I call the hi() fucntion, the greet() and the welcome() fuctions ar also called
#But if I can't call a function that inside another. If I try to call greet() it will give me an error

def outer(x):
    def inner(y):
        return x + y
    return inner

add_seven = outer(7)
print(add_seven(6))


def my_decorator(func):
    def func_modified(y):
        return func(5,y)
    return func_modified

@my_decorator
def add_five(x,y):
    return x + y

print(add_five(6))


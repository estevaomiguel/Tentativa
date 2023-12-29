def decorator(function):
    def wrapper(a ,b):
        result = function(a, b)
        print("I am going to divide a and b")
        try:
            return result
        except ZeroDivisionError:
            print("The denominator cannot be zero!")
    return wrapper




@decorator
def divide(a, b):
    return a / b

print(divide(4, 0))

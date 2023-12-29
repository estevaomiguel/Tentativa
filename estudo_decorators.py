def  new_decorator(function):
    def wrapper(x,y):
        result = function(x,y)
        return result * 2
    return wrapper


@new_decorator
def func(x, y):
    return x + y

print(func(2,3))

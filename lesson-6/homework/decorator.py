def check(func):
    def wrapper(a,b):
        try:
            print(func(a,b))
        except ZeroDivisionError:
            print("Denominator can't be zero")
    return wrapper
@check
def div(a,b):
    return a/b
# div=check(div(a,b))
div(6,2)
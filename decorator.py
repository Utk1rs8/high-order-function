# nested function
# def fun1(x):
#     def fun2(y):
#         return(x+y)
#     return(fun2)
# var1=fun1(5)
# var2=var1(5)
# print(var2)


# function that returns function
# def add(x,y,z):
#     return(x+y+z)
# def cal(fun,x,y,z):
#     return fun(x,y,z)
# var1=cal(add,5,4,3)
# print(var1)


# without decorator
# def outer_fun(fun):
#     def inner_fun(x,y):
#         x=x+10
#         y=y+10
#         print("mail function called")
#         return fun(x,y)
#     return inner_fun
# def main_fun(x,y):
#     return x+y
# var1=outer_fun(main_fun)
# var2=var1(5,6)
# print(var2)


# with decorator
def outer_fun(fun):
    def inner_fun(x,y):
        x=x+10
        y=y+10
        print("mail function called")
        return fun(x,y)
    return inner_fun
@outer_fun #decorator function
def main_fun(x,y):
    return x+y
a=main_fun(5,6)
print(a)
# import sys
# 
# def divide(x, y):
#     
# #     def check():
# #         if y <= 0:
# #             print "Cannot divide by zero"
# #             sys.exit()
# #     
# #     check()
#     try: 
#         print 'x/y = ', x/y
#     except Exception as e:
#         print e
# 
# # divide (4,2)
# divide (4, 0)
#------------------------------decorator1----------------------------------------
# def outer(x):
#     def inner():
#         print "Inner func"
#         print x
#     return inner
# var = outer(1)
# 
# var()
# print type(var)
# outer(2)()
#------------------------------decorator2----------------------------------------
# def outer(func):
#     def inner():
#         func()
#         print "Inner func"
#         return "Returning from foo"
#         
#     return inner
# 
# @outer
# def foo():
#     print "Inside foo"
# 
# print foo()
# # var = outer(foo)
# # print var()
# -------------------------------decorator3---------------------------------------
# def outer(func):
#     def inner(x):
# #         func()
#         print "Inner func"
#         return func(x)
#         
#     return inner
# 
# # @outer
# def foo(x):
#     print "Inside foo"
#     print "value of x + 2 = ", x+2
# 
# # print foo()
# var = outer(foo)
# print var(2)
# 
# foo(2)
# -------------------------------decorator4---------------------------------------
def outer(func):
    def inner(*args, **kwargs):
        print "from inner, *args = {}, **kwargs = {}".format(args, kwargs)
        return func(*args, **kwargs)        
    return inner
    
def foo(x):
    print "from foo"
    print "value of x = ",x

@outer
def foo1(x, y, z):
    print "from foo1"
    print "value of x = ",x
    print "value of y = ",y
    print "value of z = ",z
    
foo(1)
print ""
foo1(1,2,z = 3)
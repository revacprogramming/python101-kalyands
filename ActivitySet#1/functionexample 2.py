    # nested function
def f1():
    def inner(a,b):
        print("the sum of two numbers",a+b)
        print("the average of two numbers",a+b/2)
        inner(10,30)
        inner(20,30)
        inner(30,50)
            
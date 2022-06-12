#parameters


def sum(*n,name):
    result = 0
    for x in n:
        result = result+x 
        print("the sum by",name,":",result)
        
sum(name="kalyan")
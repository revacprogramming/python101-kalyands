# Conditional Execution

hrs = float(input("Enter Hours:"))
rate =float(input("enter the rate"))
if hrs<=40:
    gpay=hrs*rate
    print("",gpay)
else:
    epay=(hrs-40)*rate*1.5+40*rate
    print(epay)     
    
       

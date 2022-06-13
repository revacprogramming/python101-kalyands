# Swap function
def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
newList = [10,20,30,40,50]
print(newList(swapList))
def test_prime(n):
  if (n==1):
    return false
  elif (n==2):
    return true;
  else:
    for  x in range(2,n):
      if(n%2==0):
        return false
    return true

print(test_prime(8))    
    
  
      
 

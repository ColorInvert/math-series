def fibonacci(n):
  
  #if our recursion, or our startpoint is at 1 or below, return it's value.
  if n <= 1:
    return n

  #if not, recursively return the number input twice, offset by 2 in one iteration, and offset by 1 in another, added together. 
  else:
    return(fibonacci(n-1) + fibonacci(n-2))


def lucas(n):
  
  #hardcoded offset of the first 2 values, differentiating from fibonacci.
  if n == 0:
    return 2
  elif n == 1:
    return 1


  else:
    return(lucas(n-1) + lucas(n-2))



def sum_series(n,x=0,y=1):

  #return n normally if optional values not used, act like fibonacci
  if ((n <= 1) and (x==0) and (y==1)):
    return n
  
  #Set the 0th and 1st values to x and y. Due to the defaults defined, no inputs acts like fibonacci as mentioned above
  if n == 0:
    return x
  elif n == 1:
    return y

  else:
    return(sum_series(n-1,x,y) + sum_series(n-2,x,y))
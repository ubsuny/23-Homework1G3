#Example: 10 divided by 3:
def restoring_division(numerator, denominator):
  quotient = 0 #answer to division problem, set to zero for now
  #set the remainder to the numerator, 10 (this will get subtracted later)
  remainder = numerator

  #as long as the remainder (currently 10)...
  #is big enough to be subtracted by the denominator (3) we can run this code:
  while remainder >= denominator:
    
    #this counts each individual time 3 can go into 10
    quotient += 1
    
    #after the first subtraction, the remainder is set to 7, from (10 - 3)
    remainder -= denominator

  #after it subtracts 3 times, it cannot subtract anymore, meaning the quotient is 3
  #we can also return the remainder, which is anything that is left over
  #will return (3,1)
  return quotient, remainder
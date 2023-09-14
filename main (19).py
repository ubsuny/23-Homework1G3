def division(x,y):
  if y == 0:
    return "ERROR"
  else:
    return x/y

assert (division(2,1)) == 2
assert (division(0,5)) == 0
assert (division(1,2)) == 0.5
assert (division(1,0)) == "ERROR"
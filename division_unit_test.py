def division(x,y):
  if y == 0:
    return "ERROR"
  else:
    return x/y

print(division(2,1))
print("should return 2")
print("---")
print(division(0,5))
print("should return 0")
print("---")
print(division(1,2))
print("should return 0.5")
print("---")
print(division(1,0))
print("should return ERROR")
print("---")
print(division(1,0))
print("should return ERROR")
print("---")
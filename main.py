def sum(a, b):
  return a + b
  
def minus(a, b):
  return a - b

def multiply(a, b):
  return a * b

def division(a, b):
 return a / b

def operations(fnum, snum):
  if operation == '+':
    return sum(firstnum, secondnum)
  if operation == '-':
    return minus(firstnum, secondnum)
  if operation == '*':
    return multiply(firstnum, secondnum)
  if operation == '/':
    return division(firstnum, secondnum)


firstnum = int(input("Enter first num: "))
print("+ \n- \n* \n/")
operation = input("Pick an operation: ")
secondnum = int(input("Enter second num: "))
output = operations(firstnum, secondnum)
print(output)
nextstep = input(
  f"press y for continue with {output} and n for starting over: ")
while (nextstep == 'y'):
  firstnum = output
  print("+ \n- \n* \n/")
  operation = input("Pick an operation: ")
  secondnum = int(input("Enter second num: "))
  output = operations(firstnum, secondnum)
  print(output)
  nextstep = input(
    f"press y for continue with {output} and n for starting over: ")
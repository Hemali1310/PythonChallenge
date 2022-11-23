def firstcapital(fname, lname):
  firstname = fname.title()
  lastname = lname.capitalize()
  print(firstname)
  print(lastname)

fname = input("Enter first name: ")
lname = input("Enter last name: ")
firstcapital(fname, lname)

# def my_function(a):
#   if a < 40:
#     return
#     print("Terrible")
#   if a < 80:
#     return "Pass"
#   else:
#     return "Great"
# print(my_function(25))
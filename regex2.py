import re

email = input("Unesite mail: ")
regex = "(^[a-zA-Z].*)[.]([a-zA-Z].*)@fpmoz.sum.ba$" 
result = re.match(regex, email)

edu = input("Unesite eduId: ")
regex1 = "^([a-zA-Z])([a-zA-Z].*)[0-9]*@sum.ba$"
result1 = re.match(regex1, edu)

if result:
  print("Email tocan")
  if result1:
    print("EduId tocan")
  else:
    print("EduId nije tocan")  
else:
  print("Email nije tocan")
  if result1:
    print("EduId tocan")
  else:
    print("EduId nije tocan") 

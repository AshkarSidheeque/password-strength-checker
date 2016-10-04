import re
p = raw_input("Enter a password:  ")

x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not p[0].isalpha():
        break
    elif not re.search("[a-z]",p):
        break
    
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break

    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")
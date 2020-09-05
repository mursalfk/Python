regex = r"[A-Za-z0-9!#%&*\$\.]{8,20}" 

for example in passwords:
    if re.search(regex, example):
      	print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      	print("The password {pass_example} is invalid".format(pass_example=example))     

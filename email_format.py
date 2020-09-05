regex = r"[A-Za-z0-9!#%&*\$\.]+@\w+\.com"

for example in emails:
    if re.match(regex, example):
      	print("The email {email_example} is a valid email".format(email_example=example))
    else:
      	print("The email {email_example} is invalid".format(email_example=example))   

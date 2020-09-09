#first Calculat
num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the First Number: "))
opr = input("Add, Subtract, Multiply, Divide? Please type the complete word")
res = 0
if (int(num1) and int(num2) == 0):
    print("Invalid Inputs")
else:
    if opr == "Add":
        res = num1 + num2
        print(res)
    elif opr == "Subtract":
        res = num1 - num2
        print(res)
    elif opr == "Multiply":
        res = num1 * num2
        print(res)
    elif opr == "Divide":
        res = num1 / num2
        print(res)
    else:
        print("Invalid Operator")

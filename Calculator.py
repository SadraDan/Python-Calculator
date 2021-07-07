num1 = float(input("Enter the first Number: "))

op = input("Enter the Operator: ")

num2 = float(input("Enter the Second Number: "))

if op == "+":
    print (num1 + num2)

elif op == "-":
    print (num1 - num2)

elif op == "/": 
    print (num1 / num2)

elif op == "*":
    print (num1 * num2)

else:
    print ("Invalid Operator") 

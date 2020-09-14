# Python Program For Simple Calculation
#geeksforgeeks.org
#SadraDan
# Function to add two numbers 
def add(num1, num2):
    return num1 + num2 

# Function to subtract two numbers 
def subtract(num1, num2): 
    return num1 - num2

# Funtion to multiply two numbers 
def multiply(num1, num2): 
    return num1 * num2 

# Functuin to divide two numbers 
def divide(num1, num2): 
    return num1 / num2 

# Just to make it a bit easier 
prompt = "What would it be?"

print """
------  CHOOSE YOUR OPERATION  ------
    '1'. Add
    '2'. Subtract
    '3'. Multiply
    '4'. Divide
"""
select = int(raw_input(prompt))

number_1 = int(raw_input("Enter First Number:"))
number_2 = int(raw_input("Enter Second Number:")) 

if select == 1 : 
    print number_1, '+', number_2, '=', add(number_1, number_2)
elif select == 2: 
    print number_1, '-', number_2, '=', subtract(number_1, number_2)
elif select == 3: 
    print number_1, '*', number_2, '=', multiply(number_1, number_2)
elif select == 4: 
    print number_1, '/', number_2, '=', divide(number_1, number_2)
else: 
    print "INVALID INPUT!"
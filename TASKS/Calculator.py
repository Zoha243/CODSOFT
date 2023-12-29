
import math

def Calculator_sum(a,b):
    sum = a+b
    return sum

def calculator_Subtract(x,y):
    subtract = x-y
    return subtract


def calculator_multiplication(num1,num2):
    return num1*num2

def calculator_factorial(n1):
    return math.factorial(n1)


def calculator_division(dividend,divisor): 
    return dividend/divisor

def calculator_square_root(number):
    return math.sqrt(number)

def calculator_square(number):
    return number*number


var= True
while var:
    print("Calculator")
    print("press 1 for Addition")
    print("press 2 for Subtraction")
    print("press 3 for Multiplication")
    print("press 4 for Division")
    print("press 5 for Factorial")
    print("press 6 for Square root")
    print("press 7 for Square")
    print("press 8 for Exit")
    Person= int(input("Choice:"))
    if Person ==1:
        user=int(input("Enter Value of num1:\n"))
        user_1=int(input("Enter Value of num2:\n"))
        print("Sum:",Calculator_sum(user,user_1))
    elif Person ==2:
        u=int(input("Enter Value of num1:\n"))
        u_1=int(input("Enter Value of num2:\n"))
        print("subtraction:",calculator_Subtract(u,u_1))
    elif Person ==3:
        u=int(input("Enter Value of num1:\n"))
        u_1=int(input("Enter Value of num2:\n"))
        print("Multiplication:",calculator_multiplication(u,u_1))
    elif Person ==4:
        user = float(input("Enter Value of num1:\n"))
        user1 = float(input("Enter Value of num2:\n"))
        print(calculator_division(user,user1)) 
    elif Person ==5:
        uu=int(input("Enter Value of num:\n"))
        print("factorial:",calculator_factorial(uu))
    elif Person==6:
        u_1 = int(input("Enter Value of num:\n"))
        print("Square Root: ",calculator_square_root(u_1))
    elif Person==7:
        u_1 = int(input("Enter Value of num:\n"))
        print("Square: ",calculator_square(u_1))
    elif Person==8:
        print("EXITING")
        break    
    Person_2=input("Do You want to perform calculations Again Press yes for continue and No for Exit \n")
    if Person_2 == "Yes" or Person_2 == "yes":
        var = True
    elif Person_2 == "No" or Person_2 == "no":
        var = False





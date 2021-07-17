# this is  a little program for simple calculator

#functionalities  are Addition. subtraction, division and Multiplication


from math import *
import time


def cal():
    try:
        a = int (input("Enter your first number: "))
        b = int (input("Enter your second number: "))
        c = input("What you want to do type \"+\" or \"*\" or \"/\" or \"-\": ")
    except:
        print("Ops...")
        pass

    def addition (a,b):
        result = a + b
        return result

    def div(a,b):
        result = a/b
        return  result

    def sub(a,b):
        result = a-b
        return result

    def mul(a,b):
        result = a*b
        return result

    if c == "+":
        ans = (addition(a,b))
    elif c== "/":
        ans = (div(a,b))
    elif c== "*":
        ans = (mul(a,b))
    elif c== "-":
        ans = (sub(a,b))
    return ans

# this function is designed to handle any kind of errors

def error_handeling():
    try:
        Answer = cal()
        print("Here is your answer: {}".format(Answer))
        time.sleep(2)
        print("Try another one !!")
        final()
        cal()
    except:
        print("Invaid input, please try again !!")
        time.sleep(1)
        pass

def final():
    error_handeling()
    Y = input("Do you want to continue, Y or N ?")
    if Y=="Y" or Y=="y":
        error_handeling()
    elif Y=="N" or Y=="n":
        print("Well see you next time !!")
        exit()
    else:
        print("Invalid input!!")
        final()

while True:
    final()



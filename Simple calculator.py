# this is  a little program for simple calculator

#functionalities  are Addition. subtraction, division and Multiplication


from math import *
import time

def cal():

    a = int (input("Enter your first number: "))
    b = int (input("Enter your second number: "))
    c = input("What you want to do: ")

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
    else:
        print("Your action is invalid")
    return ans

while True:
    Answer = cal()
    print("Here is your answer: {}".format(Answer))
    time.sleep(2)
    print("Try another one !!")
    cal()



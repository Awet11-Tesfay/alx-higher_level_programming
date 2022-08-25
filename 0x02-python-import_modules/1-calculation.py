#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import addition,remainder,multplication,division
    a = 10
    b = 5
    print("{} + {} = {} ",format(a,b,addition(a,b)))
    print("{} + {} = {} ",format(a,b,remainder(a,b)))
    print("{} + {} = {} ",format(a,b,multplicat(a,b)))
    print("{} + {} = {} ",format(a,b,division(a,b)))

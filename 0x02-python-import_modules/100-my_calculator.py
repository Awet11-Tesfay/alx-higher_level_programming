#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arg = sys.arg[1:]
    arg_count = len(arg)
    operators = ["+", "-", "*", "/"]
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.arg[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.arg[1])
        b = int(sys.arg[3])
        if sys.arg[2] is "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif sys.arg[2] is "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif sys.arg[2] is "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif sys.arg[2] is "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

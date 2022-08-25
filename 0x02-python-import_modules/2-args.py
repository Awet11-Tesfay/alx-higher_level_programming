#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    cont = len(sys.argv) - 1
    if cont == 1:
        print("1 argument", end="")
    elif cont != 1:
        print("{} arguments".format(cont), end="")
    if argcont == 0:
        print(".")
    else:
        print(":")
    if(len(sys.argv) > 1):
        for n in sys.argv:
            if i > 0:
                print("{:d}: {}".format(i, n))
            i += 1

#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    argcount = len(sys.argv) - 1
    if argcount == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argcount))
    for i in range(argcount):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sumc = 0
    i = 0
    for c in sys.argv:
        if i > 0:
            sumc += int(c)
        i += 1
    print(sumc)

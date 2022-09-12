#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        c = fct(*args)
        return c
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None

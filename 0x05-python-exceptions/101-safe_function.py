#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except (IndexError, ZeroDivisionError, ValueError, TypeError) as err:
        print(f"Exception: {}", file=sys.stderr)
        return None

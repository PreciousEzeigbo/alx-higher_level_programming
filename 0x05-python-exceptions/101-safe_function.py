#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        result = None
    return (result)

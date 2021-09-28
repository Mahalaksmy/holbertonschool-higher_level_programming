#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    var = None
    try:
        var = fct(*args)
    except BaseException as error:
        pass
    finally:
        return var

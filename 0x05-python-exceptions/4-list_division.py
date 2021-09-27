#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    x = []
    for i in range(list_length):
        resul_div = 0
        try:
            resul_div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            x.append(resul_div)
    return x

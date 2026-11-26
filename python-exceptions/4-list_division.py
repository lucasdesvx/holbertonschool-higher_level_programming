#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide corresponding elements from two lists."""
    result = []

    for index in range(list_length):
        division = 0
        try:
            value_1 = my_list_1[index]
            value_2 = my_list_2[index]
            if not isinstance(value_1, (int, float)) or not isinstance(
                    value_2, (int, float)):
                print("wrong type")
            else:
                division = value_1 / value_2
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result.append(division)

    return result

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides elements of two lists element-wise, handling various errors.

  Args:
      my_list_1: The first list.
      my_list_2: The second list.
      list_length: The desired length of the resulting list.

  Returns:
      A new list with the division results, or prints error messages.
  """
  result_list = []
  for i in range(list_length):
      if i >= len(my_list_1) or i >= len(my_list_2):
          try:
              my_list_1[i] / my_list_2[i]
          except TypeError:
              print("wrong type")
          except ZeroDivisionError:
              print("division by 0")
          except IndexError:
              print("out of range")
          finally:
              result_list.append(0)
    return result_list

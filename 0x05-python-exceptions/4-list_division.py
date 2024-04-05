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
      try:
          result_list.append(my_list_1[i] / my_list_2[i])
      except TypeError:
          result_list.append(0)
          print("wrong type")
          continue
      except ZeroDivisionError:
          result_list.append(0)
          print("division by 0")
          continue
      except IndexError:
          result_list.append(0)
          print("out of range")
          continue
      finally:
          pass
    return result_list

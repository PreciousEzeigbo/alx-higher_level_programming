#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=())
first_element = tuple_a + (0, 0)
second_element = tuple_b + (0, 0)

result1 = 0
result2 = 0

result1 += first_element[0] + second_element[0]
result2 += first_element[1] + second_element[1]

return (result1, result2)

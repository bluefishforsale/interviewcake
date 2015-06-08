#!/usr/bin/env python

array_of_ints = [1, 7, 3, 4]
array_of_ints2 =  [-10, -10, 1, 3, 2]


def min_of_two(a, b):
  if a < b:
    return a
  else:
    return b


def min_of_two(a, b):
  if a > b:
    return a
  else:
    return b

def min_of_list(data):
  for i in range(0, len(data)-1):
    if data[i] < data[i+1]:
      x = data[i]
    else:
      x = data[i+1]


def max_of_list(data):
  for i in range(0, len(data)-1):
    if data[i] > data[i+1]:
      x = data[i]
    else:
      x = data[i+1]


def return_max_product(data):
  result = None
  # two lowest ints
  if not result:
    #tmp1 = data.pop(data.index(min(data)))
    tmp1 = data.pop(data.index(min_of_list(data)))
    result = tmp1
  tmp2 = min(data)
  result =  tmp1 * tmp2
  data.append(tmp1)

  # if two lowest int's are both < 0
  # then -a * -b = +c
  if tmp1 and tmp2 < 0:
    #result = result * data.pop(data.index(max(data)))
    result = result * data.pop(data.index(max_of_list(data)))
    print(data, result)

  else:
    tmp3 = 1
    for i in range(0,3):
      x = data.pop(data.index(max(data)))
      # +c might still be smaller than the smallest large number
      if x >= result:
        tmp3 = tmp3 * x
      print(data, result, tmp3)
    result = tmp3

  print(result)


return_max_product(array_of_ints)
return_max_product(array_of_ints2)

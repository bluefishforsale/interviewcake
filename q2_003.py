#!/usr/bin/env python

import sys

input_array = [1, 2, 6, 5, 9]
input_array2 = [-10, -10, 1, 3, 2]

def array_of_products(data):
  tmp_products = [] 
  result_set = [1]*len(data)

  for i in range(1, len(data)+1):
    if i < len(data):
      #tmp_products.append([("%s*%s" % (data[i], data[i+1])), (data[i] * data[i+1])])
      tmp_products.append(("%d" % (data[i-1] * data[i])))
      print("%s*%s" % (data[i-1], data[i]))
    else:
      #tmp_products.append([("%s*%s" % (data[i], data[0])), (data[i] * data[0])])
      tmp_products.append(("%d" % (data[i] * data[0])))
      print("%s*%s" % (data[i], data[0]))
  for i in range(0, len(data)):
    a = tmp_products.pop(i+1)
    b = tmp_products.pop(-2)
    result_set[i] = a * b
    tmp_products.insert(i+1, a)
    tmp_products.insert(-2, b)
    print(result_set)
 

def reference_solution(data):
  result_set = [1]*len(data)
  for i in range(0, len(data)):
    tmp = data.pop(0)
    for bloop in data:
      result_set[i] = result_set[i] * bloop
    data.append(tmp)
  print(result_set)
  print('')


reference_solution(input_array)
array_of_products(input_array)

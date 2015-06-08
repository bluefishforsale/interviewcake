#!/usr/bin/env python

import sys

array_of_ints = [1, 2, 6, 5, 9]
length = len(array_of_ints)

result_array = [ ] * length

left_product = [''] * length
right_product = [''] * length
left_product[0] = 1
right_product[-1] = 1

for i in range(1, length):
  #print("L: %s * %s = %s" % (array_of_ints[i-1], left_product[i-1], (array_of_ints[i-1] * left_product[i-1])))
  left_product[i]  = array_of_ints[i-1] * left_product[i-1]
  #print("R: %s * %s = %s" % (array_of_ints[-i], right_product[-i], (array_of_ints[-i] * right_product[-i])))
  right_product[length-i] = array_of_ints[-i] * right_product[length-i+1]


right_product[0] = right_product[1] * array_of_ints[0]

print(left_product)
print(right_product)

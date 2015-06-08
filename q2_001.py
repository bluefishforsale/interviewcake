#!/usr/bin/env python

import sys

inputdata = [1, 7, 3, 4]
inputdata2 = [1, 0, 3, 4]


def On_no_div(data):
  tmpdata=[]
  sys.stdout.write('\n')
  a = data.pop(0)
  tmpdata.append(a)
  print(data)
    



def get_products_of_all_ints_except_at_index(data):
  tmplist = []
  resultlist = []

  for i in range(0, len(data)):
    tmplist=data[:]
    tmplist.pop(i)

    y = 1
    for x in range(0, len(tmplist)):
      y = y * tmplist[x]

    resultlist.append(y)
  print(resultlist)


print("O(n^2) Solution:"),
get_products_of_all_ints_except_at_index(inputdata)
#print("O(2n)  Solution: "),
#On_use_div(inputdata)
print("O(n^2) Solution:"),
#get_products_of_all_ints_except_at_index(inputdata2)
#print("O(2n)  Solution: "),
#On_use_div(inputdata2)

print("O(2n)  Solution: "),
On_no_div(inputdata)
#On_no_div(inputdata2)

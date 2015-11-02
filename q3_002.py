#!/usr/bin/python
# interviewcake.com
# question #3
#
# array_of_ints
#   given an array of integers, find the highest_product you can get from three of the integers
#   the array will always have at least three, and no maxmimum number of integers



def highest_product(array_of_ints):
    length = 3
    max_product = 1
    max_ints = [0] * length

    # sort array in place O(n log n)
    for i in array_of_ints:
        for j in range(len(max_ints)):
            if abs(i) > abs(max_ints[j]):
                max_ints[j] = i
                break

    print max_ints
    for i in max_ints:
        max_product = max_product * i

    return max_product


# using positive integers: 630
array_of_ints = [10, 2, 5, 1, 9, 7, 3, 4, 6, 0, 1]
print "using positive integers"
print highest_product(array_of_ints)

# using negative numbers: 300
array_of_ints = [-10, -10, 1, 3, 2]
print "using mixed positive / negative integers"
print highest_product(array_of_ints)

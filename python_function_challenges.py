# Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n. For example:
#     sum_to(6)  # returns 21
#     sum_to(10) # returns 55

def sum_to(n):
    return sum(range(n+1))

print(sum_to(6))
print(sum_to(10))

# Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers. For example:
#     largest([10, 4, 2, 231, 91, 54])  # returns 231
#     largest([1,2,3,4,0])  # returns 4

# using built-in functions
def largest(list):
    return max(list)

print(largest([10, 4, 2, 231, 91, 54]))
print(largest([1,2,3,4,0]))

# Without using built-in functions
def largest2(list):
    large_num = 0
    for num in list:
        if num > large_num:
            large_num = num
    return large_num

print(largest2([10, 4, 2, 231, 91, 54]))
print(largest2([1,2,3,4,0]))

# Write a function named occurances() that takes two string parameters and counts the number of occurrances of the second string inside the first string. For example:
#     occurances('fleep floop', 'e')   # returns 2
#     occurances('fleep floop', 'p')   # returns 2
#     occurances('fleep floop', 'ee')  # returns 1
#     occurances('fleep floop', 'fe')  # returns 0

# def occurances(str1, str2):
#     count = 0
#     length = len(str2)
#     if str2 in str1:
#         # return 'yes'
#         if length == 1:
#             for i in str1:
#                 if i == str2:
#                     count = count + 1
#             return count
#         else: 
#             return 'Nope, too hard'
#     else:
#         return count

def occurances(str1, str2):
  str1Split = str1.split(str2)
  return(len(str1Split)-1)
# print(occurances('stringsstrings', 'ing'))

print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

# Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on *args).

def product(*args):
    product = 1
    for i in args:
        product *= i
    return product

print(product(2,3,4))
print(product(2,3,4,10))
print(product(4,5))
'''
*********
PROGRAM 4
*********
Define a function above_average that takes a list of integers or floats as an argument. The function will identify the mean of the list, identify the numbers in the list that are greater than the mean, and then return those numbers in a list.

You may define a separate function that finds the average of a list, though you don't have to.
'''
def above_average(lis):
  for i in lis:
    average = sum(lis) / len(lis)
    greater = []
    if i > average:
      greater.append (i)
  return greater

  

'''
elif program == '4':
  lis = [int(i) for i in input("Enter a list of numbers separated by a space: ").split()]
  print(above_average(lis))
'''

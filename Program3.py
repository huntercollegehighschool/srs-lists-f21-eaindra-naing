'''
*********
PROGRAM 3
*********
Define a function second_smallest that takes a list of integers or floats as an argument. The function returns the 2nd smallest number in the list.
'''
def second_smallest(lis):
  lis.sort() 
  return (lis[1])



"""
elif program == '3':
  lis = [int(i) for i in input("Enter a list of numbers separated by a space: ").split()]
  print(second_smallest(lis))
"""

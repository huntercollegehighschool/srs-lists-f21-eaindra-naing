'''
*********
PROGRAM 1
*********
Define a function number_of_odds that takes a list of integers as an argument. The function returns how an integer, how many odd numbers are in the list.
'''



def number_of_odds(lis):
  odds = []
  for i in lis:
    if i % 2 == 1:
      odds.append (i)
  return (len(odds))




""""
if program == '1':
  lis = [int(i) for i in input("Enter a list of integers separated by a space: ").split()]
  print(number_of_odds(lis))
"""

#need to work on
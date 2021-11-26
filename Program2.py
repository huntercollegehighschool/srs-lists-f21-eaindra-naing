'''
*********
PROGRAM 2
*********
Define a function odd_reverse that takes a list as an argument. The function creates a new list containing only the elements in the odd indices (indices 1, 3, 5, ...) and then reverses it. The function returns that list.
'''
def odd_reverse(lis):
  odds = []
  for i in lis:
    if i % 2 == 1:
      odds.append (i)
  odds.sort(reverse = True) 
  return (odds)
  


"""
def number_of_odds(lis):
  odds = []
  for i in lis:
    if i % 2 == 1:
      odds.append (i)
  return (len(odds))
  
elif program == '2':
  lis = [int(i) for i in input("Enter a list, each element separated by a space: ").split()]
  print(odd_reverse(lis))
"""
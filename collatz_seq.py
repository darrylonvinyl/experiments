from collatz import collatz
import sys

try:
  number=int(input('Please enter a number: '))
  while number >= 1:
    number=collatz(number)
    if number > 1:
      continue
    elif number == 1:
      break 
except ValueError:
  print('Please enter an integer.')
except KeyboardInterrupt:
  print('Program ended.')

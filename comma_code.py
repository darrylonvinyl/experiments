# Comma code
def comma_code(lst):
  ret_string = ''
  for item in lst:
    if item == lst[0]:
      ret_string += str(item)
      continue
    if item == lst[-1]:
      ret_string += ', and ' + str(item)
      continue
    ret_string += ', ' + str(item)
  print(ret_string)

sample = [1,2,3,4,5]
sample_too = ['Test','for','these','negroes']

comma_code(sample_too)
comma_code(sample)

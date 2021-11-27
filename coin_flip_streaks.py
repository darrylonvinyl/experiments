import random
numberOfStreaks = 0
for experimentNumber in range(10000):
  flip_list = []
  for flip in range(100):
    if random.randint(0,1) == 0:
      flip_list.append('head')
    else:
      flip_list.append('tail')
  head_streak = 0
  tail_streak = 0
  flip_index = 0
  first_item = flip_list[0]
  if first_item == flip_list[1]:
    flip_index = 1
  for streak in flip_list[1:]:
    if streak == flip_list[flip_index - 1]:
      if streak == 'head':
        head_streak += 1
        tail_streak = 0
      else:
        tail_streak += 1
        head_streak = 0 
      if head_streak >= 6 or tail_streak >= 6:
        numberOfStreaks += 1
    flip_index += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))

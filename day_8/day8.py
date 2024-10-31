def read_data():
  data = []
  with open('data.txt', 'r') as f:
    for line in f.readlines():
      if line.strip() == '':
        data.append('')
      else:
        data.append(line.strip())
  
  return data

def check_tree(x, y, data):
  # Check borders
  if y == 0 or y == len(data[x]) - 1:
    return True
  elif x == 0 or x == len(data) - 1:
    return True

  tree = int(data[x][y])

  row = data[x]

  row_right = row[y+1:]
  row_left = (row[:y])[::-1]

  high_trees = 0  

  # Right 
  for t in row_right:
    if tree <= int(t):
      high_trees+=1
      break
      
  # Left
  for t in row_left:
    if tree <= int(t):
      high_trees+=1
      break

  # Build column for vertical check
  column = ""
  for i in range(len(data)):
    column += data[i][y]

  col_up = (column[:x])[::-1]
  col_down = column[x+1:]

  # Up
  for t in col_up:
    if tree <= int(t):
      high_trees +=1
      break
  
  # Down 
  for t in col_down:
    if tree <= int(t):
      high_trees += 1
      break


  if high_trees >= 4: 
    return False 
  else:
    return True

def count_trees(data):
  visible_trees = 0
  for x in range(len(data)):
    for y in range(len(data[x])):
      if check_tree(x, y, data) == True:
        visible_trees += 1
  
  return visible_trees

def calculate_scenic_score(x, y, data):
  up_score = 0 
  down_score = 0
  left_score = 0
  right_score = 0

  tree = int(data[x][y])

  row = data[x]

  row_right = row[y+1:]
  row_left = (row[:y])[::-1]


  # Right 
  for t in row_right:
    right_score += 1
    if tree <= int(t):
      break
      
  # Left
  for t in row_left:
    left_score += 1
    if tree <= int(t):
      break

  # Build column for vertical check
  column = ""
  for i in range(len(data)):
    column += data[i][y]

  col_up = (column[:x])[::-1]
  col_down = column[x+1:]

  # Up
  for t in col_up:
    up_score += 1
    if tree <= int(t):
      break
  
  # Down 
  for t in col_down:
    down_score += 1
    if tree <= int(t):
      break

  scenic_score = up_score * down_score * left_score * right_score
  return scenic_score

def find_highest_scenic_score(data):
  max_scenic_score = 0
  for i in range(len(data)):
    for j in range(len(data[i])):
      scenic_score = calculate_scenic_score(i, j, data)
      if scenic_score > max_scenic_score:
        max_scenic_score = scenic_score
  
  return max_scenic_score

def day_8():
  data = read_data()
  print(f"Answer Part I: {count_trees(data)}")
  print(f"Answer Part II: {find_highest_scenic_score(data)}")


day_8()

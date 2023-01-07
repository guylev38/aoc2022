def read_data():
  with open('data.txt', 'r') as f:
    stacks_raw, instructions_raw = (line.splitlines() 
    for line in f.read().strip("\n").split("\n\n"))
  
  # Parse Stacks
  number_of_stacks = len(stacks_raw[-1].strip().replace(" ", ""))
  indexes = [i for i, c in enumerate(stacks_raw[-1]) if c != " "]

  stacks = {}
  for i in range(number_of_stacks):
    stacks[str(i+1)] = []

  for i in range(len(stacks_raw)-1):
    for j in range(len(stacks_raw[i])):
      if j in indexes and stacks_raw[i][j] != ' ' and stacks_raw[i][j] != '[' and stacks_raw[i][j] != ']':
        stacks[str(indexes.index(j)+1)].append(stacks_raw[i][j])

  for i in range(len(stacks)):
    stacks[str(i+1)].reverse() 

  # Parse Instructions  
  instructions = []
  for line in instructions_raw:
    container = []
    for c in line.split():
      try:
        container.append(int(c))
      except ValueError:
        pass
    
    instructions.append(container)

  return stacks, instructions

def part_one():
  stacks, instructions = read_data()

  for line in instructions:
    for i in range(line[0]):
      crate = stacks[str(line[1])].pop()
      stacks[str(line[2])].append(crate)

  result = '' 
  for i in range(len(stacks)):
    result += stacks[str(i+1)][-1]
  
  print(result)

def part_two():
  stacks, instructions = read_data()

  for line in instructions:
    container = []
    for i in range(line[0]):
      crate = stacks[str(line[1])].pop()
      container.append(crate)
    container.reverse()
    for item in container:
      stacks[str(line[2])].append(item)
  
  result = '' 
  for i in range(len(stacks)):
    result += stacks[str(i+1)][-1]
  
  print(result)


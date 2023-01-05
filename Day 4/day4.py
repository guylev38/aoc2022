def read_data():
  data = []
  with open('data.txt', 'r') as f:
    for line in f.readlines():
      data.append(line.strip().split(','))

  for i in range(len(data)):
    data[i][0] = data[i][0].split('-')
    data[i][1] = data[i][1].split('-')
    data[i][0] = data[i][0] + data[i][1] 
    data[i] = [eval(j) for j in data[i][0]]
  return data


def part_one():
  data = read_data()
  count = 0
  for pair in data:
    if pair[1] <= pair[3] and pair[0] >= pair[2]:
      count += 1
    elif pair[1] >= pair[3] and pair[0] <= pair[2]:
      count += 1
  print(count) 

def part_two():
  data = read_data()
  count = 0
  for pair in data:
    if pair[1] <= pair[3] and pair[1] >= pair[2]:
      count+=1
    elif pair[3] <= pair[1] and pair[3] >= pair[0]:
      count += 1
  print(count)


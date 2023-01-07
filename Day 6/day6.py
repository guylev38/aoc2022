def read_data():
  with open('data.txt', 'r') as f:
    data = [line for line in f.readlines()]
  return data[0]

def part_one():
  data = read_data()
  count = 0
  for i in range(len(data)-3):
    marker = []
    flag = True
    j = i
    while j < i+4:
      marker.append(data[j])
      j+=1

    for c in marker:
      if marker.count(c) > 1:
        flag = False
        break
    
    if flag == False:
      count += 1
    else:
      count += 4
      break


  print(count) 
    

def part_two():
  data = read_data()
  count = 0
  for i in range(len(data)-13):
    marker = [] 
    flag = True
    j = i

    while j < i+14:
      marker.append(data[j])
      j+=1

    for c in marker:
      if marker.count(c) > 1:
        flag = False
        break
    
    if flag == False:
      count += 1
    else:
      count += 14
      break


  print(count) 

part_two()









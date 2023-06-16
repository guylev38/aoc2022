def read_data():
  with open('data.txt', 'r') as f:
    data = []
    for line in f.readlines():
      data.append(line.strip().split())
    
    for item in data:
      if item[0] in ['ls', '$']: 
        del item[0]
  return data

def part_one():
  data = read_data()
  dsum = 0
  dirs = {}
  current_dir = '/'
  prev_dir = '/'
  for item in data:
    if item[0] == 'cd':
      print(item)
      if item[1] == '..':
        current_dir = dirs[current_dir][0]
      else:
        prev_dir = current_dir
        current_dir = item[1]
      if current_dir not in dirs.keys():
        dirs[current_dir] = [prev_dir, 0]
      print(current_dir, prev_dir)
    if item[0].isdigit():
      print(item)
      dirs[current_dir][1] += int(item[0])
  root_size = dirs['/'][1]
  print(dirs['/'])
  for d in dirs:
    prev_dir = dirs[d][0]
    dirs[prev_dir][1] += dirs[d][1]
  # dirs['/'][1] -= root_size
  print(dirs['/'])


  for d in dirs:
    if dirs[d][1] <= 100000:
      dsum += dirs[d][1]

  # print(dirs)

  print(dsum)
part_one()
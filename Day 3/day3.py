import string


def first_part():
  data = []
  with open('data.txt', 'r') as f:
    for line in f.readlines():
      first_part, second_part = line[:len(line)//2], line[len(line)//2:]
      data.append([first_part.strip(), second_part.strip()])
  count = 0
  for item in data:
    for i in item[0]:
      if i in item[1]:
        if i.isupper():
          count += int(string.ascii_uppercase.index(i))+26+1
          break
        else:
          count += int(string.ascii_lowercase.index(i))+1
          break
  print(count)


def second_part():
  data = []
  with open('data.txt', 'r') as f:
    for line in f.readlines():
      data.append(line.strip())
  count = 0
  for i in range(0,len(data), 3):
    second = data[i+1]
    third = data[i+2]
    for j in data[i]:
      if j in second and j in third:
        if j.isupper():
          count += int(string.ascii_uppercase.index(j))+26+1
          break
        else:
          count += int(string.ascii_lowercase.index(j))+1
          break
  
  print(count)

second_part()
data = []
with open('data.txt', 'r') as f:
  for line in f.readlines():
    if line.strip() == '':
      data.append('')
    else:
      data.append(int(line.strip()))

max_elf = 0
elf_sum = 0

elves = [0, 0, 0]

for i in range(3):
  for j in range(len(data)):
    if data[j] == '':
      if elf_sum > max_elf and elf_sum not in elves:
        print(elves)
        max_elf = elf_sum
    
      elf_sum = 0
  
    else:
      elf_sum += data[j]

  elves[i-1] = max_elf
  max_elf = 0
  elf_sum = 0
  
print(sum(elves))


data = []
with open('data.txt', 'r') as f:
  for line in f.readlines():
    data.append(line.strip().split())

def part_one():
  score = 0
  points = {"X": 1, "Y": 2, "Z": 3, "draw": 3, "win": 6}
  for pair in data:
    if pair[0] == 'A' and pair[1] == 'Y':
      score += points[pair[0]] + points["win"] 
    elif pair[0] == 'B' and pair[1] == 'Z':
      score += points[pair[1]] + points["win"]
    elif pair[0] == 'C' and pair[1] == 'X':
      score += points[pair[1]] + points["win"]

    elif pair[0] == 'A' and pair[1] == 'Z':
      score += points[pair[1]]
    elif pair[0] == 'B' and pair[1] == 'X':
      score += points[pair[1]]
    elif pair[0] == 'C' and pair[1] == 'Y':
      score += points[pair[1]]

  
    elif pair[0] == 'A' and pair[1] == 'X':
      score += points[pair[1]] + points["draw"]
    elif pair[0] == 'B' and pair[1] == 'Y':
      score += points[pair[1]] + points["draw"]
    elif pair[0] == 'C' and pair[1] == 'Z':
      score += points[pair[1]] + points["draw"]

  print(score)

def part_two():
  score = 0
  points = {"A": 1, "B": 2, "C": 3, "draw": 3, "win": 6}
  options = {"AX": "C", "AZ": "B", "BX": "A", "BZ": "C", "CX": "B", "CZ": "A"}
  for pair in data:
    if pair[1] == "X":
      if pair[0] == "A":
        score += points[options["AX"]] 
      elif pair[0] == "B":
        score += points[options["BX"]]
      else:
        score += points[options["CX"]]
    
    elif pair[1] == "Y":
      score += points["draw"]
      if pair[0] == "A":
        score += points["A"] 
      elif pair[0] == "B":
        score += points["B"]
      elif pair[0] == "C":
        score += points["C"]
    
    else:
      score += 6
      if pair[0] == "A":
        score += points[options["AZ"]]
      elif pair[0] == "B":
        score += points[options["BZ"]]
      else:
        score += points[options["CZ"]]
  print(score)

part_two()
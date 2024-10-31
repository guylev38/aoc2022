class Dir: 
  # Directory (Node) in a N-ary tree
  def __init__(self, name, parent_dir):
    self.name = name
    self.parent_dir = parent_dir
    self.children = []
    self.size = 0
  
def read_data():
  # Read the data from the data.txt and 
  # parse it as needed.
  with open('data.txt', 'r') as f:
    data = []
    for line in f.readlines():
      data.append(line.strip().split())
    for item in data:
      if item[0] in ['ls', '$']: 
        del item[0]
  return data


def build_filesystem():
  # Build the filesystem N-ary tree
  data = read_data()
  root = Dir("/", None)
  
  current_node = root

  for d in data:
    if d[0] == "cd":
      if d[1] == "/":
         continue
      if d[1] == "..":
        current_node = current_node.parent_dir
      else: 
        new_node = Dir(d[1], current_node)
        current_node.children.append(new_node)
        current_node = new_node
    if d[0].isdigit():
      current_node.size += int(d[0])
       
  return root


def size_filesystem(node):
  # Add the sizes of children directories to parent directories
  total_size = node.size
  for child in node.children:
    total_size += size_filesystem(child)
  node.size = total_size
  return total_size


def sum_filesystem(node, dsum):
  # Sum all of the directories that their sizes are under 100,000
  if node.size <= 100000:
    dsum += node.size
  
  for child in node.children:
    dsum = sum_filesystem(child, dsum)

  return dsum

def choose_dir(node, picked_size, root_size):
  unused_space = 70000000 - root_size
  ux = unused_space + node.size # Unused space + node.size

  # If the removal of the current directory frees up enough space then save it 
  if ux > 30000000 and (ux - 30000000) < picked_size:
    picked_size = node.size

  for child in node.children: 
    new_picked_size = choose_dir(child, picked_size, root_size)

    # Update if there is a better directory to remove
    if new_picked_size < picked_size:
      picked_size = new_picked_size
  
  return picked_size

def day_7():
  root = build_filesystem()
  size_filesystem(root)

  print(f"Answer Part I: {sum_filesystem(root, 0)}")
  print(f"Answer Part II: {choose_dir(root, root.size, root.size)}")


day_7()




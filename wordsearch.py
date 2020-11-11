# Imports
import sys

# Global Variables
version = "2.0"
verbose_level = 0
limit_directions = False
reverse_remove = False

# Test Variables
class test:
    size = "11x13"
    string = "ysjzdesdikdzjlrcanuxddnyqaqwvadxrnakhlpdxyaenalassbanunytlrvaxeangdkeieomdqvpmmtbzzdagqkieeriatlhkjmtdlxtwioaitiahliiswmbpanamaahcsaleuzenevmco"
    wordlist = ["bahamas","chile","japan","maldives","guyane","haiti","mexico","moldova","pananma"]

# Parse flags
def parse_flags():
  flags = sys.argv

  # For every flag
  for x in flags:
    if (x[0] != "-"): # Check if it is a flag
      continue

    if (x == "-l"):
      global limit_directions
      limit_directions = True
      continue

    if (x == "-r"):
      global reverse_remove
      reverse_remove = True
      continue

    if (x[0:2] == "-v"):
      if (len(x) <= 3):
        global verbose_level
        try:
          verbose_level = int(x[-1])
        except:
          verbose_level = 1

        verbose(1, str("verbose level " + str(verbose_level)))
        continue
      else:
        error(x)

    if (x == "--"):
      return

    else:
      error(x)

# Parse Commands
def parse_commands():
  verbose(2, "Parsing Commands")

  options = sys.argv
  options.pop(0)

  # For every command
  for x in options:
    if (x[0] == "-"): # Do nothing for flags
      continue

    if (x == "search" or x == "s"):
      try:
        index = options.index("search")
      except:
        index = options.index("s")
      finally:
        try:
          array = create_array(options[index+2], options[index+3]) # search(size, string)
        except:
          array = create_array(test.size, test.string)
        finally:
          search(options[index+1], array) # search(word, array)
          return

    if (x == "help" or x == "h"):
      try:
        helpindex = options.index("help")
      except:
        helpindex = options.index("h")
      finally:
        try:
          helpindex += 1
          manual(options[helpindex])
        except:
          manual()

    else:
      error(x)

# Verbose
def verbose(level, message, end="\n"):
  global verbose_level
  if (verbose_level >= level):
    print(message, end=end)
  return

# Error
def error(var):
  print('"' + str(var) + '"' + " unknown")
  sys.exit()

# Create Array
def create_array(size, string):
  verbose(2, "Creating Array")
  verbose(2, str("\tsize: " + size + "\n\tstring: " + string))

  rows, cols = size.split("x")
  verbose(3, str(rows + " by " + cols))
  rows, cols = int(rows), int(cols)

  array = []

  for row in range(rows):
    array.append([])
    for col in range(cols):
      position = ((row * cols) + col)
      verbose(4, position)
      array[row].append(string[position])

  return array

# Print Array
def print_array(array, remove=[[-1,-1]], prefix="\t"):
  rowpos, colpos = 0, 0
  global reverse_remove

  for row in array:
    print(prefix, end="")

    for col in row:
      # check for removal
      for x in remove:
        if (x[0] == rowpos and x[1] == colpos):
          if (reverse_remove == True):
            rem = col + " "
          else:
            rem = ". "
          break

        else:
          if (reverse_remove == False):
            rem = col + " "
          else:
            rem = ". "

      print(rem, end="")

      colpos += 1

    print("\n", end="")
    rowpos += 1
    colpos = 0

  return

# Search
def search(word, array):
  verbose(2, "Starting Search")
  verbose(2, str("\tword: " + word + "\n\tarray: "))
  global verbose_level
  if (verbose_level >= 2):
    print_array(array)

  # Find starters
  starters = find_starters(array, word)

  # Init direction
  direction(starters, word, array)
  return

# Find starters
def find_starters(array, word):
  verbose(2, "Finding starters")
  word_start = word[0]

  verbose(2, "\t", end="")

  starters = []
  rowpos, colpos = 0, 0
  for row in array:
    for col in row:
      if (col == word_start):
        starters.append([rowpos, colpos])
        verbose(2, str(str(rowpos) + "," + str(colpos) + " "), end="")

      colpos += 1
    rowpos += 1
    colpos = 0

  verbose(2, "")

  if (starters == []):
    starters = [[-1,-1]]

  global verbose_level
  if (verbose_level >= 3):
    print_array(array, starters)

  return starters

# Direction
def direction(starters, word, array):
  verbose(2, str("Started looking in directions from starters"))

  # Get array size
  rows = len(array)
  cols = len(array[0])

  global limit_directions
  if (limit_directions == True):
    directions = ["d","r","dr","ur","u"]
  else:
    directions = ["d","r","dr","ur","u","ul","l","dl"]

  word = word[1:(len(word) + 1)]
  for coords in starters:
    found = direction_iter(array, cols, rows, directions, word, 0, [coords])

  print("Not Found")
  sys.exit()


def direction_iter(array, cols, rows, directions, word, offset=0, found=[]):
  for x in directions:
    next_direction = [x]
    if (x == "d"):
      row = found[-1][0] + 1
      col = found[-1][1]
    elif (x == "r"):
      row = found[-1][0]
      col = found[-1][1] + 1
    elif (x == "dr"):
      row = found[-1][0] + 1
      col = found[-1][1] + 1
    elif (x == "dl" and limit_directions == False):
      row = found[-1][0] + 1
      col = found[-1][1] - 1
    elif (x == "u" and limit_directions == False):
      row = found[-1][0] - 1
      col = found[-1][1]
    elif (x == "ur" and limit_directions == False):
      row = found[-1][0] - 1
      col = found[-1][1] + 1
    elif (x == "ul" and limit_directions == False):
      row = found[-1][0] - 1
      col = found[-1][1] - 1
    elif (x == "l" and limit_directions == False):
      row = found[-1][0]
      col = found[-1][1] - 1
    else:
      continue

    try:
      char = array[row][col]
    except:
      continue

    verbose(5, f'{char}: {offset}: {next_direction}: {found}')

    if (char == word[offset]):
      found.append([row, col])
      if (offset + 1 == len(word)): # Found word
        print_array(array,found,"")
        sys.exit()
      else:
        offset += 1
        direction_iter(array, cols, rows, next_direction, word, offset, found)

    else:
      offset = 0
      found = [found[0]]
      continue

# Manual/help pages
def manual(page="main"):
  if (page == "main"):
    print("wordsearchpy [flags] [--] <command> [options]")
  else:
    print('"' + str(page) + '"' + " not implemented")
  return

# Main
def main():
  # Parse flags and options
  parse_flags()
  parse_commands()
  return

# Run main if running as script/executable
if __name__ == "__main__":
    main()

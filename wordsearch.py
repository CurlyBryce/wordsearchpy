# Imports
import sys

# Global Variables
version = "a2.0"
verbose_level = 0

# Test Variables
class test:
    size = "11x13"
    string = "ysjzdesdikdzjlrcanuxddnyqaqwvadxrnakhlpdxyaenalassbanunytlrvaxeangdkeieomdqvpmmtbzzdagqkieeriatlhkjmtdlxtwioaitiahliiswmbpanamaahcsaleuzenevmco"
    lines = ["ysjzdesdikdzj","lrcanuxddnyqa","qwvadxrnakhlp","dxyaenalassba","nunytlrvaxean","gdkeieomdqvpm","mtbzzdagqkiee","riatlhkjmtdlx","twioaitiahlii","swmbpanamaahc","saleuzenevmco"]
    wordlist = ["bahamas","chile","japan","maldives","guyane","haiti","mexico","moldova","pananma"]

# Parse flags
def parse_flags():
  flags = sys.argv

  # For every flag
  for x in flags:
    if (x[0] != "-"): # Check if it is a flag
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
      search()
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
def verbose(level, message):
  global verbose_level
  if (verbose_level >= level):
    print(message)
  return

# Error
def error(var):
  print('"' + str(var) + '"' + " unknown")
  sys.exit()

# Search
def search():
  print("search not available")
  return

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

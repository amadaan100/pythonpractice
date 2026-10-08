#slice
#sys.argv

import sys

if len(sys.argv) < 2:
    sys.exit("Please provide a string as a command-line argument.")

for arg in sys.argv[1:]:
    print(arg)
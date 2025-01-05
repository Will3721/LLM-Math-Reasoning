# This file defines the scoring script.

import sys

with open(sys.argv[1], "r") as file:
    outputs = [line.strip() for line in file]

with open(sys.argv[2], "r") as file:
    answers = [line.strip() for line in file]


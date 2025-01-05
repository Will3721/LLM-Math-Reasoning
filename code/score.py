# This file defines the scoring script.

import sys

# Computes Accuracies

with open(sys.argv[1], "r") as file:
    outputs = [line.strip() for line in file]

with open(sys.argv[2], "r") as file:
    answers = [line.strip() for line in file]

print(len(outputs))
total = len(answers)
correct = 0
index = 0
for (output, answer) in zip(outputs, answers):
    index = index + 1
    our = output.replace(",", "")
    theirs = answer.replace(",", "")
    if '.' in our:
        our = float(our)
    else: 
        our = int(our)
    if '.' in theirs:
        theirs = float(theirs)
    else:
        theirs = int(theirs)
    if (abs(our - theirs) <= 0.05):
        correct += 1

print('Correct: ', correct)
print('Total: ', total)
print('Acc: ', (correct / total))

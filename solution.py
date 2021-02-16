import sys

digit_string = sys.argv[1]

sum = 0

for character in digit_string:
    sum += int(character)

print(sum)
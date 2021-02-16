import sys

level = int(sys.argv[1])

cur_level = 1
while cur_level <= level:
    sharp_str = "#" * cur_level
    print(sharp_str.rjust(level, ' '))
    cur_level = cur_level + 1
import os

file = open(os.path.join("Day 8", "file.txt"))
file_contents = file.read().split("\n")
print(file_contents)
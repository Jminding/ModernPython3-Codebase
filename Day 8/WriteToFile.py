import os

file = open(os.path.join("Day 8", "file.txt"), 'w')
file_contents = "9999"
file.write(file_contents)
file.close()
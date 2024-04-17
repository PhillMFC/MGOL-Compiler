import sys, os

file_mgol = sys.argv[1]

cat = open(file_mgol, 'r')
print(cat.read())
cat.close()
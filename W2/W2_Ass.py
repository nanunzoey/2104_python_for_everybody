import re

f = open("W2_realdata.txt")

lines = f.readlines()
num = 0

for line in lines:
    y = re.findall('[0-9]+', line)
    for i in y:
        num += int(i)
print(num)

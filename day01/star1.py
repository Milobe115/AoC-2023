import re

f = open("./input.txt", "r")
lines = f.readlines()

values = []

for line in lines:
    numbers = re.findall(r'(\d)', line)
    values.append(int(numbers[0] + numbers[-1]))

print(f"Calibration sum : {sum(values)}")
import re


def find_first_digit(line):
    one_pos = line.find("one") if "one" in line else 1000
    two_pos = line.find("two") if "two" in line else 1000
    three_pos = line.find("three") if "three" in line else 1000
    four_pos = line.find("four") if "four" in line else 1000
    five_pos = line.find("five") if "five" in line else 1000
    six_pos = line.find("six") if "six" in line else 1000
    seven_pos = line.find("seven") if "seven" in line else 1000
    eight_pos = line.find("eight") if "eight" in line else 1000
    nine_pos = line.find("nine") if "nine" in line else 1000
    first_digit = line.find(re.findall(r'(\d)', line)[0])
    min_val = min(one_pos, two_pos, three_pos, four_pos, five_pos, six_pos, seven_pos, eight_pos, nine_pos, first_digit)

    if min_val == one_pos:
        return 1
    elif min_val == two_pos:
        return 2
    elif min_val == three_pos:
        return 3
    elif min_val == four_pos:
        return 4
    elif min_val == five_pos:
        return 5
    elif min_val == six_pos:
        return 6
    elif min_val == seven_pos:
        return 7
    elif min_val == eight_pos:
        return 8
    elif min_val == nine_pos:
        return 9
    else:
        return int(line[first_digit])

def find_last_digit(line):
    one_pos = line.rfind("one") if "one" in line else -1
    two_pos = line.rfind("two") if "two" in line else -1
    three_pos = line.rfind("three") if "three" in line else -1
    four_pos = line.rfind("four") if "four" in line else -1
    five_pos = line.rfind("five") if "five" in line else -1
    six_pos = line.rfind("six") if "six" in line else -1
    seven_pos = line.rfind("seven") if "seven" in line else -1
    eight_pos = line.rfind("eight") if "eight" in line else -1
    nine_pos = line.rfind("nine") if "nine" in line else -1
    first_digit = line.rfind(re.findall(r'(\d)', line)[-1])
    max_val = max(one_pos, two_pos, three_pos, four_pos, five_pos, six_pos, seven_pos, eight_pos, nine_pos, first_digit)


    if max_val == one_pos:
        return 1
    elif max_val == two_pos:
        return 2
    elif max_val == three_pos:
        return 3
    elif max_val == four_pos:
        return 4
    elif max_val == five_pos:
        return 5
    elif max_val == six_pos:
        return 6
    elif max_val == seven_pos:
        return 7
    elif max_val == eight_pos:
        return 8
    elif max_val == nine_pos:
        return 9
    else:
        return int(line[first_digit])

def main():
    f = open("./input.txt", "r")
    lines = f.readlines()
    values = []
    for line in lines:
        fd = find_first_digit(line)
        ld = find_last_digit(line)
        values.append(int(fd*10 + ld))
    print(values)
    print(f"Calibration sum : {sum(values)}")

if __name__ == '__main__':
    main()

import re


def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    values = []
    for line in lines:
        numbers = re.findall(r'(\d)', line)
        values.append(int(numbers[0] + numbers[-1]))
    print(f"Calibration sum : {sum(values)}")

if __name__ == "__main__":
    main()
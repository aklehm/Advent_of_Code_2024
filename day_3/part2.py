import re


def extract_mul_parts(long_string: str) -> list:
    pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
    return re.findall(pattern, long_string)


def main():
    rawlines = list()

    with open('./day_3/input.txt', 'r') as f:
        rawlines = f.readlines()

    totalSum = 0
    calc = True
    for line in rawlines:
        instructions = extract_mul_parts(line)
        for instr in instructions:
            if 'do()' in instr:
                calc = True
                continue
            if "don't()" in instr:
                calc = False
                continue
            if calc:
                parts = str(instr).replace('mul(', '').replace(')', '')
                try:
                    numbers = parts.split(',')
                    totalSum += int(numbers[0].strip()) * int(numbers[1].strip())
                except Exception as e:
                    print(f'{e}: {instr}: {calc}')

    print(f'Total sum: {totalSum}')


if __name__ == '__main__':
    main()

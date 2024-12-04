def checkSafe(report: list) -> bool:
    safe = True
    direction = 'increasing' if (report[0] < report[1]) else 'decreasing'

    for i in range(len(report)):
        if i > 0:
            if direction == 'increasing' and report[i-1] > report[i]:
                safe = False
            if direction == 'decreasing' and report[i-1] < report[i]:
                safe = False
            if abs(report[i-1] - report[i]) < 1 or abs(report[i-1] - report[i]) > 3:
                safe = False
    return safe


def main():
    rawlines = list()
    safeReports = 0

    with open('./day_2/input.txt', 'r') as f:
        rawlines = f.readlines()

    for report in rawlines:
        lvlstr = report.split(' ')
        levels = list()
        for level in lvlstr:
            levels.append(int(level.replace('\n', '')))

        if checkSafe(levels):
            safeReports += 1

    print(f'Safe reports: {safeReports}')


if __name__ == '__main__':
    main()

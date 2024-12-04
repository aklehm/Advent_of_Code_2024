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


def remove_element(lst: list, index: int) -> list:
    try:
        lst.pop(index)
    except IndexError:
        print('Index out of range')
    return lst


def main():
    rawlines = list()
    safeReports = 0

    with open('./day_2/input.txt', 'r') as f:
        rawlines = f.readlines()

    for report in rawlines:
        lvlstr = report.split(' ')
        newLevels = list()
        for level in lvlstr:
            newLevels.append(int(level.replace('\n', '')))
        levels = tuple(newLevels)

        if checkSafe(newLevels):
            safeReports += 1
        else:
            for i in range(len(levels)):
                newLevels = list(levels)
                if checkSafe(remove_element(lst=newLevels, index=i)):
                    safeReports += 1
                    break

    print(f'Safe reports: {safeReports}')


if __name__ == '__main__':
    main()

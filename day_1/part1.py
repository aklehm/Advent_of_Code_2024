def main():
    rawlines = list()

    with open('./day_1/input.txt', 'r') as f:
        rawlines = f.readlines()

    leftList = list()
    rightList = list()

    for line in rawlines:
        data = line.split('  ')
        leftList.append(int(data[0].strip().replace('\n', '')))
        rightList.append(int(data[1].strip().replace('\n', '')))
    leftList.sort()
    rightList.sort()

    totalDistance = 0

    if (len(leftList) == len(rightList)):
        for i in range(len(leftList)):
            totalDistance += abs(leftList[i]-rightList[i])
        print(f'Total distance: {totalDistance}')
    else:
        print('Error: List size not equal!')


if __name__ == '__main__':
    main()

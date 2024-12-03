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

    score = 0

    if (len(leftList) == len(rightList)):
        for i in range(len(leftList)):
            score += leftList[i] * rightList.count(leftList[i])
        print(f'Similarity score: {score}')
    else:
        print('Error: List size not equal!')


if __name__ == '__main__':
    main()

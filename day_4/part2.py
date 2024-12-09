def search_crossMas(words: list) -> int:
    searchObjects = ['MAS', 'SAM']
    foundDiag = 0
    for row in range(len(words) - 2):
        for col in range(len(words[0]) - 2):
            diag_1 = ''.join([words[row][col], words[row+1][col+1], words[row+2][col+2]])
            diag_2 = ''.join([words[row+2][col], words[row+1][col+1], words[row][col+2]])
            foundDiag += diag_1 in searchObjects and diag_2 in searchObjects
    return foundDiag


def main():
    words = list()

    with open('./day_4/input.txt', 'r') as f:
        for line in f.readlines():
            words.append([x for x in line if x != '\n'])

    total = 0
    total += search_crossMas(words=words)

    print(f'Total X-MAS: {total}')


if __name__ == '__main__':
    main()

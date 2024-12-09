def search_horizontal(words: list) -> int:
    searchObjects = ['XMAS', 'SAMX']
    foundHor = 0
    for row in words:
        for i in range(len(words[0]) - 3):
            foundHor += ''.join(row[i:i+4]) in searchObjects
    return foundHor


def search_vertical(words: list) -> int:
    searchObjects = ['XMAS', 'SAMX']
    foundVer = 0
    for col in zip(*words):
        for i in range(len(words[0]) - 3):
            foundVer += ''.join(col[i:i+4]) in searchObjects
    return foundVer


def search_diagonal(words: list) -> int:
    searchObjects = ['XMAS', 'SAMX']
    foundDiag = 0
    for row in range(len(words) - 3):
        for col in range(len(words[0]) - 3):
            diag_1 = ''.join([words[row][col], words[row+1][col+1], words[row+2][col+2], words[row+3][col+3]])
            diag_2 = ''.join([words[row+3][col], words[row+2][col+1], words[row+1][col+2], words[row][col+3]])
            foundDiag += diag_1 in searchObjects
            foundDiag += diag_2 in searchObjects
    return foundDiag


def main():
    words = list()

    with open('./day_4/input.txt', 'r') as f:
        for line in f.readlines():
            words.append([x for x in line if x != '\n'])

    total = 0
    total += search_horizontal(words=words)
    total += search_vertical(words=words)
    total += search_diagonal(words=words)

    print(f'Total XMAS: {total}')


if __name__ == '__main__':
    main()

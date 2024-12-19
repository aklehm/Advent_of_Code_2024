import re


class AocDay6:
    def __init__(self):
        self.part1 = 0
        self.part2 = 0
        self.puzzleInput = list()
        self.puzzle = tuple()
        self.reGuard = r'[<>v^]'
        self.rePlace = r'[.X]'
        self.reObstacle = r'[#O]'
        self.curPos = [0, 0]
        self.guard = ''
        self.mapSize = [0, 0]

        with open('input_files/day6.txt', 'r') as f:
            puzzleList = list()
            for line in f.readlines():
                puzzleLine = [x for x in line if x != '\n']
                self.puzzleInput.append(puzzleLine)
                puzzleList.append(tuple(puzzleLine))
            self.puzzle = tuple(puzzleList)

        for i in range(len(self.puzzleInput)):
            for j in range(len(self.puzzleInput[i])):
                if re.match(self.reGuard, self.puzzleInput[i][j]):
                    self.guard = self.puzzleInput[i][j]
                    self.curPos = [i, j]
        self.mapSize = [len(self.puzzleInput), len(self.puzzleInput[0])]

    def _guardWalk(self, obsPos: list):
        maxSteps = (self.mapSize[0] * self.mapSize[1])
        curSteps = 0
        while curSteps < maxSteps:
            curSteps += 1
            if self.guard == '^':
                if self.curPos[0] == 0:
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = 'X'
                    # print('Break ^')
                    break
                if re.match(self.reObstacle, self.puzzleInput[self.curPos[0]-1][self.curPos[1]]):
                    self.guard = '>'
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = self.guard
                if re.match(self.rePlace, self.puzzleInput[self.curPos[0]-1][self.curPos[1]]):
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = 'X'
                    self.curPos = [self.curPos[0]-1, self.curPos[1]]
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = '^'

            if self.guard == '>':
                if self.curPos[1]+1 >= len(self.puzzleInput[self.curPos[0]]):
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = 'X'
                    break
                if re.match(self.reObstacle, self.puzzleInput[self.curPos[0]][self.curPos[1]+1]):
                    self.guard = 'v'
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = self.guard
                if re.match(self.rePlace, self.puzzleInput[self.curPos[0]][self.curPos[1]+1]):
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = 'X'
                    self.curPos = [self.curPos[0], self.curPos[1]+1]
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = '>'

            if self.guard == 'v':
                if self.curPos[0] + 1 >= len(self.puzzleInput):
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = 'X'
                    break
                if re.match(self.reObstacle, self.puzzleInput[self.curPos[0]+1][self.curPos[1]]):
                    self.guard = '<'
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = self.guard
                if re.match(self.rePlace, self.puzzleInput[self.curPos[0]+1][self.curPos[1]]):
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = 'X'
                    self.curPos = [self.curPos[0]+1, self.curPos[1]]
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = 'v'

            if self.guard == '<':
                if self.curPos[1] == 0:
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = 'X'
                    break
                if re.match(self.reObstacle, self.puzzleInput[self.curPos[0]][self.curPos[1]-1]):
                    self.guard = '^'
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = self.guard
                if re.match(self.rePlace, self.puzzleInput[self.curPos[0]][self.curPos[1]-1]):
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = 'X'
                    self.curPos = [self.curPos[0], self.curPos[1]-1]
                    self.puzzleInput[self.curPos[0]][self.curPos[1]] = '<'
        if curSteps >= maxSteps:
            self.part2 += 1

    def solveDay6(self):
        self._guardWalk(obsPos=[0, 0])
        self.part1 = 0
        for line in self.puzzleInput:
            self.part1 += line.count('X')
        self.part2 = 0
        for x in range(len(self.puzzle)):
            for y in range(len(self.puzzle[x])):
                self.puzzleInput = list()
                for line in self.puzzle:
                    self.puzzleInput.append(list(line))
                self.puzzleInput[x][y] = 'O'
                for i in range(len(self.puzzleInput)):
                    for j in range(len(self.puzzleInput[i])):
                        if re.match(self.reGuard, self.puzzleInput[i][j]):
                            self.guard = self.puzzleInput[i][j]
                            self.curPos = [i, j]
                self._guardWalk(obsPos=[i, j])


if __name__ == '__main__':
    aoc = AocDay6()
    aoc.solveDay6()
    print(f'Part 1: {aoc.part1}')
    print(f'Part 2: {aoc.part2}')

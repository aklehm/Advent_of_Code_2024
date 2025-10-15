from itertools import product


class AocDay7:
    def __init__(self):
        self.part1 = 0
        self.part2 = 0
        self.puzzleInput = list()
        self.operators = ['+', '*']
        self.operators2 = ['+', '*', '||']

        with open('input_files/day7.txt', 'r') as f:
            for line in f.readlines():
                puzzleLine = list()
                eq = line.split(':')
                puzzleLine.append(eq[0])
                eq = eq[1].strip().split(' ')
                for e in eq:
                    puzzleLine.append(e.replace('\n', ''))
                self.puzzleInput.append(puzzleLine)

    def _checkequation(self, equation: list):
        result = int(equation[0])
        resultOption = int(equation[1])
        obsNumber = len(equation) - 2
        operator_combinations = list(product(self.operators, repeat=obsNumber))
        for op in operator_combinations:
            # print(f'op: {op}')
            resultOption = int(equation[1])
            for i in range(obsNumber):
                # print(f'op[i]: {op[i]}')
                if op[i] == '+':
                    resultOption += int(equation[i+2])
                if op[i] == '*':
                    resultOption *= int(equation[i+2])
            # print(f'resultOption: {resultOption}')
            # print(f'result: {result}')
            if resultOption == result:
                self.part1 += result
                break
            
    def solveDay7(self):
        # print(self.puzzleInput)
        for equation in self.puzzleInput:
            self._checkequation(equation)


if __name__ == '__main__':
    aoc = AocDay7()
    aoc.solveDay7()
    print(f'Part 1: {aoc.part1}')
    print(f'Part 2: {aoc.part2}')

import re
from typing import Tuple


class AocDay5:
    def __init__(self):
        self.part1 = 0
        self.part2 = 0
        self.puzzleInput = list()
        self.rules = list()
        self.updates = list()
        self.reRules = r'^\d+\|\d+$'
        self.reUpdates = r'^(\d+,)+\d+$'

        with open('input_files/day5.txt', 'r') as f:
            self.puzzleInput = f.readlines()

        for element in self.puzzleInput:
            if re.match(self.reRules, element):
                pages = element.replace('\n', '').split('|')
                self.rules.append((int(pages[0]), int(pages[1])))
            if re.match(self.reUpdates, element):
                update = element.replace('\n', '').split(',')
                newUpdate = list()
                for u in update:
                    newUpdate.append(int(u))
                self.updates.append(tuple(newUpdate))

    def _checkUpdate(self, update: Tuple[int, ...]) -> bool:
        for i in range(len(update)):
            rules = [t for t in self.rules if update[i] in t]
            for rule in rules:
                idx = rule.index(update[i])
                if idx == 0:
                    for j in range(0, i, 1):
                        if update[j] == rule[1]:
                            return False
                if idx == 1:
                    for j in range(len(update)-1, i, -1):
                        if update[j] == rule[1]:
                            return False
                if idx < 0 or idx > 1:
                    print(f'Wrong rule Size: {idx}')
                    raise Exception
        return True

    def _sortUpdates(self, update: Tuple[int, ...]) -> None:
        precedence = {val: set() for val in update}

        for first, second in self.rules:
            if first in update and second in update:
                precedence[second].add(first)

        def resolve_order(value, visited, stack):
            if value in visited:
                return
            visited.add(value)
            for predecessor in precedence[value]:
                resolve_order(predecessor, visited, stack)
            stack.append(value)

        visited = set()
        stack = []
        for value in update:
            resolve_order(value, visited, stack)

        sortedUpdate = tuple(stack[::-1])
        self.part2 += sortedUpdate[len(sortedUpdate)//2]

    def solveDay5(self):
        for u in self.updates:
            if self._checkUpdate(u):
                self.part1 += u[len(u)//2]
            else:
                self._sortUpdates(u)


if __name__ == '__main__':
    aoc = AocDay5()
    aoc.solveDay5()
    print(f'Part 1: {aoc.part1}')
    print(f'Part 2: {aoc.part2}')

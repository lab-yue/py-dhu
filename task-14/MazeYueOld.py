# from https://github.com/rainy-me/python-homework/blob/master/maze/Maze.py
# import sys
# import time
# import curses
from random import randint, choice

# c = curses.initscr()


class Direction:
    UP = [-1, 0]
    DOWN = [1, 0]
    LEFT = [0, -1]
    RIGHT = [0, 1]

    ALL = [
        UP,
        DOWN,
        LEFT,
        RIGHT,
    ]
    # MAP = {
    #     "KEY_UP": UP,
    #     "KEY_DOWN": DOWN,
    #     "KEY_LEFT": LEFT,
    #     "KEY_RIGHT": RIGHT,
    # }


class Cell:
    PLAYER = "👻"
    OPEN = "🌕"
    CLOSE = "🌑"

    def __init__(self):
        self.status = Cell.CLOSE
        self.options = [*Direction.ALL]

    def open(self):
        self.status = Cell.OPEN

    @property
    def isClose(self):
        return self.status == Cell.CLOSE


class Maze:

    def __init__(self, width=0, height=0):
        self._visited = []
        self._width = width
        self._height = height
        self._map = [[Cell() for _ in range(width)] for _ in range(height)]
        self._created = False
        self.run()
        # self._movingPostion = None

    @property
    def playerPostion(self):
        return self._movingPostion if self._created else self._visited[-1]

    def getCell(self, x, y) -> Cell:
        if (
            0 <= x <= self._width - 1 and
            0 <= y <= self._height - 1
        ):
            return self._map[x][y]
        else:
            return None

    # def run(self, win):
    def run(self):
        [x, y] = self.randomPoint()
        startPoint = self._map[x][y]
        startPoint.open()
        self._visited.append([x, y])

        # while True:
        while not self._created:
            # c.clear()
            # m.draw()
            # if not self._created:
            #    self.waitForMove(win)
            # else:
            #    time.sleep(.3)
            self.dig()
            # c.refresh()

    def dig(self) -> int:
        [x, y] = self.playerPostion
        cell = self._map[x][y]

        while len(cell.options):
            option = choice(cell.options)
            cell.options.remove(option)
            [dx, dy] = option
            one_forward = self.getCell(x + dx, y + dy)
            two_forward = self.getCell(x + 2 * dx, y + 2 * dy)
            if (
                one_forward and
                two_forward and
                one_forward.isClose and
                two_forward.isClose
            ):
                one_forward.open()
                two_forward.open()
                self._visited.append([x + 2 * dx, y + 2 * dy])
                return
        self._visited.pop()
        if len(self._visited) == 0:
            self._created = True
            self._movingPostion = [x, y]

    # def waitForMove(self, win):
    #     while 1:
    #         try:
    #             key = str(win.getkey())
    #             if (key not in Direction.MAP):
    #                 break
    #             [x, y] = self.playerPostion
    #             [dx, dy] = Direction.MAP[key]
    #             cell = self.getCell(x+dx, y+dy)
    #             if cell and not cell.isClose:
    #                 self._movingPostion = [x+dx, y+dy]
    #             break
    #         except Exception:
    #             pass

    def randomPoint(self) -> [int, int]:
        return [randint(0, self._width - 1), randint(0, self._height - 1)]

    # def draw(self):
    #     for x, row in enumerate(self._map):
    #         for y, cell in enumerate(row):
    #             if (self.playerPostion == [x, y]):
    #                 c.addstr(Cell.PLAYER)
    #             else:
    #                 c.addstr(cell.status)
    #         c.addstr("\n")
    #     if self._created:
    #         c.addstr(
    #             "press arrow key to move:\n" +
    #             "UP:↑ \nDOWN: ↓ \nRIGHT:→ \nLEFT:←\nQUIT: Ctrl+C\n"
    #         )


if __name__ == '__main__':
    Maze(5, 5)

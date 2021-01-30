from random import randint, choice
import sys
import random
import time


class Direction:
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    TOP = (0, -1)
    DOWN = (0, 1)
    ALL = [LEFT, TOP, DOWN, RIGHT]

    @staticmethod
    def op(direction):
        return {
            Direction.LEFT: Direction.RIGHT,
            Direction.TOP: Direction.DOWN,
            Direction.DOWN: Direction.TOP,
            Direction.RIGHT: Direction.LEFT,
        }.get(direction)


class Maze:

    """
    前回作成した迷路生成のアルゴリズムを元に、機能を拡張していく。

    実装内容は下記の通り

    ・迷路のスタート地点及びゴール地点の設定

    ・スタートからゴールまで移動を行い、ゴールにたどり着いたら処理を終了する

    ・スタートからゴールまでに要したステップ数を表示する

    ・スタートからゴールまでの経路を描画する

    上記を元に各設問に回答せよ

    問1.
    上記の要件を満たすプログラムを実装せよ

    問2.
    スタートからゴールまでの経路を自動で検索し、その経路を可視化するプログラムを実装せよ
    """

    _width = 0
    _height = 0

    _data = []

    _startPath = []

    _isCreated = False

    _playerPoint = None

    _startPoint = None
    _goalPoint = None

    def __init__(self, width, height):
        print("init")
        if width < 5 or height < 5:
            raise "maze size should be bigger than 5x5"
        self._width = width
        self._height = height
        self._data = [0b11111111] * width * height
        self._open = []
        self._goalPath = []
        self.kbd = {
            "a": lambda: self.moveIfOk(Direction.LEFT),
            "d": lambda: self.moveIfOk(Direction.RIGHT),
            "w": lambda: self.moveIfOk(Direction.TOP),
            "s": lambda: self.moveIfOk(Direction.DOWN),
            "q": lambda: exit(),
        }
        self.create()

    def create(self):
        print("create")
        [x, y] = self.__randomPoint()
        self._data[self.__by(x, y)] &= 127
        self._open.append([x, y])
        self._startPath.append([x, y])

        while not self._isCreated:
            self.dig()
        self.startGame()

    def startGame(self):
        self._startPoint = choice(self._open)
        self._goalPoint = choice([p for p in self._open if p != self._startPoint])
        self._playerPoint = self._startPoint
        self._goalPath = self.search(self._startPoint)
        self.draw()
        while self._playerPoint != self._goalPoint:
            if self.handle():
                self.draw()

    def search(self, start, directions=Direction.ALL, path=[]):
        if start == self._goalPoint:
            return []
        [x, y] = start
        for direction in directions:
            [dx, dy] = direction
            [nx, ny] = [x + dx, y + dy]
            if not self.__cell(nx, ny) or (self.__cell(nx, ny) & 128):
                pass
            elif [nx, ny] == self._goalPoint:
                return path
            else:
                ok = self.search(
                    [nx, ny],
                    [d for d in Direction.ALL if d != Direction.op(direction)],
                    [*path, [nx, ny]],
                )
                if ok:
                    return ok

    def dig(self):
        print("dig")
        [x, y] = self._startPath[-1]
        head = self.__cell(x, y) & 240
        tail = self.__cell(x, y) & 15
        while tail:
            (k, dx, dy) = choice(
                list(
                    filter(
                        bool,
                        [
                            tail & (1 << 0) and (0, *Direction.LEFT),
                            tail & (1 << 1) and (1, *Direction.TOP),
                            tail & (1 << 2) and (2, *Direction.DOWN),
                            tail & (1 << 3) and (3, *Direction.RIGHT),
                        ],
                    )
                )
            )
            tail &= ~(1 << k)
            self._data[self.__by(x, y)] = head | tail
            [nx_1, ny_1, nx_2, ny_2] = [x + dx, y + dy, x + 2 * dx, y + 2 * dy]
            if self.__cell(nx_1, ny_1) & self.__cell(nx_2, ny_2) & 128:
                self._data[self.__by(nx_1, ny_1)] &= 127
                self._open.append([nx_1, ny_1])
                self._data[self.__by(nx_2, ny_2)] &= 127
                self._open.append([nx_2, ny_2])
                self._startPath.append([nx_2, ny_2])
                return
        self._startPath.pop()
        if len(self._startPath) == 0:
            self._isCreated = True

    def draw(self):
        print("draw")
        for y in range(self._height):
            for x in range(self._width):
                for cell, f in {
                    "⬛️": lambda: self.__cell(x, y) >> 7,
                    "🔱": lambda: [x, y] == self._playerPoint,
                    "🈁": lambda: [x, y] == self._startPoint,
                    "🍎": lambda: [x, y] == self._goalPoint,
                    "🟨": lambda: [x, y] in self._goalPath,
                    "⬜️": lambda: True,
                }.items():
                    if f():
                        print(cell, end="")
                        break
            print("")
        print("press key to move:\nw: ↑ \ns: ↓ \nd: → \na: ←\nq: QUIT\n")

    def moveIfOk(self, direction):
        [x, y] = self._playerPoint
        [dx, dy] = direction
        cell = self.__cell(x + dx, y + dy)
        if cell >> 6 and not cell >> 7:
            self._playerPoint = [x + dx, y + dy]

    def handle(self):
        fn = self.kbd.get(input())
        if fn:
            fn()
            return 1
        return 0

    def __randomPoint(self) -> [int, int]:
        return [randint(0, self._width - 1), randint(0, self._height - 1)]

    def __by(self, x, y):
        return x + y * self._height

    def __cell(self, x, y):
        if 0 <= x <= self._width - 1 and 0 <= y <= self._height - 1:
            return self._data[self.__by(x, y)]
        else:
            return 0


if __name__ == "__main__":
    Maze(10, 10)

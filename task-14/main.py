import sys
import time
import curses
from random import randint, choice

"""
Pythonを用いての実装を行い、以下の問に対して回答せよ。

提出内容は課題に対して作成したプログラムデータ及び、そのプログラムの出力とする。jupiter等でプログラムと出力が同ファイルになっている場合は、まとめてしまって問題ない。

これまで学習したオブジェクト指向プログラミングやアルゴリズムの応用として、下記に関するプログラムを実装する。

穴掘り法を用いた迷路生成プログラム

今回扱うテーマは下記となる。

    クラスやメソッド処理
    多次元配列（リスト）の取り扱い
    forやwhileなどの各種繰り返し処理
    複雑な条件分岐
    再帰処理


【下記に記載のプログラムをPythonを用いて実装する】

穴掘り法は、全面壁と定義した作業領域中に穴を伸ばして道としていくことによって迷路を作成するプログラムである。ゲームのダンジョンの自動生成などで利用される手法のうちの古典的、基本的な手法のひとつである。

下記が穴掘り法のアルゴリズムとなる。

    縦横それぞれ5マス以上のマップを作成する
    作成したマップをすべて壁とする
    マップ上のx,y座標から任意の位置を選択して、そこから掘り進める。掘り進める方法は下記となる


    上下左右の方向で、どの方向が掘り進められるのか判定する。掘り進められるかどうかの定義は、現在の座標から1マス先及び2マス先の座標まで壁となっていることである
    掘り進めることが可能な方向をランダムに選択して、2マス先まで道として、現在位置を更新する
    現在位置をチェックポイントとしてリストに追加し、保存する
    掘り進めることができなくなるまで1.~3.を繰り返す
    掘り進めることができなくなったら、これまで3.に記録していた座標からどこかしらかに掘り進めることが可能な座標を取得してまた1.からの作業を行う
    どこにも掘ることが出来る座標がなくなった場合は、その時点で処理を終了する



上記を元に各設問に回答せよ

問1.
記載のアルゴリズムを元にして、迷路生成を行うプログラムを実装せよ

問2.
 生成したプログラムにプレイヤーの定義を行い、input関数からの入力を元に迷路空間を上下左右に移動するための処理を実装せよ
"""
c = curses.initscr()


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
    MAP = {
        "KEY_UP": UP,
        "KEY_DOWN": DOWN,
        "KEY_LEFT": LEFT,
        "KEY_RIGHT": RIGHT,
    }


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
        self._movingPostion = None

    @property
    def playerPostion(self):
        return self._movingPostion if self._created else self._visited[-1]

    def getCell(self, x, y) -> Cell:
        if 0 <= x <= self._width - 1 and 0 <= y <= self._height - 1:
            return self._map[x][y]
        else:
            return None

    def run(self, win):
        [x, y] = self.randomPoint()
        startPoint = self._map[x][y]
        startPoint.open()
        self._visited.append([x, y])

        while True:
            c.clear()
            m.draw()
            if self._created:
                self.waitForMove(win)
            else:
                time.sleep(0.3)
                self.dig()
            c.refresh()

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
                one_forward
                and two_forward
                and one_forward.isClose
                and two_forward.isClose
            ):
                one_forward.open()
                two_forward.open()
                self._visited.append([x + 2 * dx, y + 2 * dy])
                return
        self._visited.pop()
        if len(self._visited) == 0:
            self._created = True
            self._movingPostion = [x, y]

    def waitForMove(self, win):
        while 1:
            try:
                key = str(win.getkey())
                if key not in Direction.MAP:
                    break
                [x, y] = self.playerPostion
                [dx, dy] = Direction.MAP[key]
                cell = self.getCell(x + dx, y + dy)
                if cell and not cell.isClose:
                    self._movingPostion = [x + dx, y + dy]
                break
            except Exception:
                pass

    def randomPoint(self) -> [int, int]:
        return [randint(0, self._width - 1), randint(0, self._height - 1)]

    def draw(self):
        for x, row in enumerate(self._map):
            for y, cell in enumerate(row):
                if self.playerPostion == [x, y]:
                    c.addstr(Cell.PLAYER)
                else:
                    c.addstr(cell.status)
            c.addstr("\n")
        if self._created:
            c.addstr(
                "press arrow key to move:\n"
                + "UP:↑ \nDOWN: ↓ \nRIGHT:→ \nLEFT:←\nQUIT: Ctrl+C\n"
            )


if __name__ == "__main__":
    m = Maze(5, 5)
    try:
        curses.wrapper(m.run)
    except KeyboardInterrupt:
        sys.exit(0)

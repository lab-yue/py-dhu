# https://gist.github.com/koorimizuw/6a8702f2289c032e05de063d7d385f3b
from random import randint, choice

"""
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


class Grid:
    def __init__(self):
        self.road = False
        self.visited = False

    def dig(self):
        self.road = True
        self.visited = True

    def visit(self):
        self.visited = True


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.checkPoint = []
        if self.isIllegal():
            raise ("Illegal width or height value!")

        self.map = [[Grid() for _ in range(height)] for _ in range(width)]
        self.create()
        # (self.positionX, self.positionY) = self.checkPoint[0]
        # while True:
        #     print(f'position: {self.positionX}, {self.positionY}')
        #     self.draw()
        #     print("press key to move:\nw: ↑ \ns: ↓ \nd: → \na: ←\nq: QUIT\n")
        #     control = input()
        #     if control == 'q':
        #         break
        #     elif control == 'w' and self.positionX - 1 in range(0, self.height) and self.map[self.positionX-1][self.positionY].road:
        #         self.positionX -= 1
        #     elif control == 's' and self.positionX + 1 in range(0, self.height) and self.map[self.positionX+1][self.positionY].road:
        #         self.positionX += 1
        #     elif control == 'd' and self.positionY + 1 in range(0, self.width) and self.map[self.positionX][self.positionY+1].road:
        #         self.positionY += 1
        #     elif control == 'a' and self.positionY - 1 in range(0, self.width) and self.map[self.positionX][self.positionY-1].road:
        #         self.positionY -= 1

    def create(self):
        (startX, startY) = self.randomPosition()
        self.dig(startX, startY)
        while self.haveNoDig():
            (startX, startY) = self.haveNoDig()
            self.dig(startX, startY)

    def dig(self, x, y):
        while True:
            self.map[x][y].dig()
            self.checkPoint.append((x, y))
            option = self.randomDirection(x, y)
            if not option:
                break
            (x, y) = option[0]
            self.map[x][y].dig()
            (x, y) = option[1]

    # def draw(self):
    #     self.roadIcon = "⬜️"
    #     self.wallIcon = "⬛️"
    #     self.charaIcon = "🟨"
    #     for i in range(len(self.map)):
    #         line = ""
    #         for j in range(len(self.map[i])):
    #             if self.positionX == i and self.positionY == j:
    #                 line += self.charaIcon
    #             elif self.map[i][j].road:
    #                 line += self.roadIcon
    #             else:
    #                 line += self.wallIcon
    #         print(line)

    def isIllegal(self):
        if self.width < 5 or self.height < 5:
            return True
        return False

    def randomPosition(self):
        return (randint(0, self.width - 1), randint(0, self.height - 1))

    def randomDirection(self, x, y):
        options = []

        if x - 2 in range(0, self.width):
            if not self.map[x - 1][y].road and not self.map[x - 2][y].road:
                options.append([(x - 1, y), (x - 2, y)])
        if x + 2 in range(0, self.width):
            if not self.map[x + 1][y].road and not self.map[x + 2][y].road:
                options.append([(x + 1, y), (x + 2, y)])
        if y - 2 in range(0, self.height):
            if not self.map[x][y - 1].road and not self.map[x][y - 2].road:
                options.append([(x, y - 1), (x, y - 2)])
        if y + 2 in range(0, self.height):
            if not self.map[x][y + 1].road and not self.map[x][y + 2].road:
                options.append([(x, y + 1), (x, y + 2)])

        if not options:
            return None

        return choice(options)

    def haveNoDig(self):
        for (i, j) in self.checkPoint:
            if self.randomDirection(i, j):
                return (i, j)
        return None


if __name__ == "__main__":
    Maze(5, 5)

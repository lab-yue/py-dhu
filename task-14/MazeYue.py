from random import randint, choice


class Maze:

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

    _width = 0
    _height = 0

    _data = 0

    _startPath = []

    _isCreated = False

    _playerPoint = None

    def __init__(self, width, height):
        # print("init")
        if width < 5 or height < 5:
            raise "maze size should be bigger than 5x5"
        self._width = width
        self._height = height
        self._data = [0b11111111] * width * height
        # self.kbd = {
        #     "a": lambda: self.moveIfOk(1 << 0),
        #     "d": lambda: self.moveIfOk(1 << 1),
        #     "w": lambda: self.moveIfOk(1 << 2),
        #     "s": lambda: self.moveIfOk(1 << 3),
        #     "q": lambda: exit(),
        # }
        self.create()

    def create(self):
        # print("create")
        [x, y] = self.__randomPoint()
        self._data[self.__by(x, y)] &= 0b01111111
        self._startPath.append([x, y])

        while not self._isCreated:
            self.dig()
        # while 1:
        #     if self.handle():
        #         self.draw()

    def dig(self):
        # print("dig")
        # self._playerPoint = self._startPath[-1]
        [x, y] = self._startPath[-1]
        head = self.__cell(x, y) & 0b11110000
        tail = self.__cell(x, y) & 0b00001111
        while tail:
            (k, dx, dy) = choice(
                list(
                    filter(
                        bool,
                        [
                            tail & (1 << 0) and (0, -1, 0),
                            tail & (1 << 1) and (1, 1, 0),
                            tail & (1 << 2) and (2, 0, -1),
                            tail & (1 << 3) and (3, 0, 1),
                        ],
                    )
                )
            )
            tail &= ~(1 << k)
            self._data[self.__by(x, y)] = head | tail
            [nx_1, ny_1, nx_2, ny_2] = [x + dx, y + dy, x + 2 * dx, y + 2 * dy]
            if self.__cell(nx_1, ny_1) & self.__cell(nx_2, ny_2) & 0b10000000:
                self._data[self.__by(nx_1, ny_1)] &= 0b01111111
                self._data[self.__by(nx_2, ny_2)] &= 0b01111111
                self._startPath.append([nx_2, ny_2])
                return
        self._startPath.pop()
        if not len(self._startPath):
            self._isCreated = True
        #     self.draw()

    # def draw(self):
    #     print("draw")
    #     for y in range(self._height):
    #         for x in range(self._width):
    #             if self.__cell(x, y) >> 7:
    #                 print("❌", end="")
    #             elif [x, y] == self._playerPoint:
    #                 print("🔱", end="")
    #             else:
    #                 print("✅", end="")
    #         print("")
    #     print("press key to move:\nw: ↑ \ns: ↓ \nd: → \na: ←\nq: QUIT\n")

    # def moveIfOk(self, direction):
    #     [x, y] = self._playerPoint
    #     [dx, dy] = {
    #         (1 << 0): (-1, 0),
    #         (1 << 1): (1, 0),
    #         (1 << 2): (0, -1),
    #         (1 << 3): (0, 1),
    #     }[direction]
    #     cell = self.__cell(x + dx, y + dy)
    #     if cell >> 6 and not cell >> 7:
    #         self._playerPoint = [x + dx, y + dy]

    # def handle(self):
    #     fn = self.kbd.get(input())
    #     if fn:
    #         fn()
    #         return 1
    #     return 0

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

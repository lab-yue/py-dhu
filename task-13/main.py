#!/usr/bin/env python3
from pathlib import Path

__path__ = Path(__file__).parent
CYAN = "\033[96m"
UNDERLINE = "\033[4m"
END = "\033[0m"


def print_question(question):
    return print(f"{UNDERLINE}{CYAN}{question}{END}{END}")


def assert_print(a, b):
    print(f"{a} == {b}")
    assert a == b


print_question(
    """
問1.

四則演算と繰り返し処理

任意の正の数値aおよびbに対して、公倍数をすべてリストして出力するプログラムを作成し、動作検証を行い、その結果を出力せよ
"""
)

# すべて公倍数??? なので無限ループである。
# def run(a,b):
#     import itertools
#     [print(a*b*i) for i in itertools.count(start=1)]

# 公約数
def common_divisor(a, b):
    for i in range(1, min(a, b) + 1):
        if not a % i | b % i:
            print(i)


common_divisor(12, 24)

print_question(
    """
問2.

関数定義とその呼び出し：

平方根の近似値を求める

以下の繰り返し処理を実行して入力値の平方根を求める計算を行うために、関数squareRootを作成する。当関数の定義は下記となる

1. 平方根を求めたい数値をx（xは0より大きな数）とする

2. 平方根の近似値としてraを定義し、xと同じ値を設定する

3. r1に対して、raを代入する

4. もうひとつの近似値としてr2 = x/r1を定義する

・r1がxの平方根であれば、r2もまたxの平方根である。異なっていればxの平方根はr1とr2の間にある

5. 新しい近似値として、r1とr2の平均ra = (r1+r2)/2を作成する

6. 3.~5.を何度か適当な数繰り返すとxの平方根の近似値が求められる

上記に対する処理を実装し、作成した関数に対して引数13を代入した際の平方根の近似値を出力せよ
"""
)


def squareRoot(x):
    r1, r2 = x, 1
    for _ in range(1000):
        r1 = (r1 + r2) / 2
        r2 = x / r1
        if r1 == r2:
            return r1
    return r1


print(f"squareRoot of {13} = {squareRoot(13)}")

print_question(
    """
問.3

三角関数の利用：

2次元座標の原点(0, 0)から、座標(3, 4)の方向を向いている物体aを考える

同空間内の任意の座標bがaの前方にあるかどうかを判定するためのプログラムを実装し、動作検証を行い、その結果を出力せよ

なお、前方にあるかどうかの判定はベクトルの内積の正負で行うものとする
"""
)


class p(tuple):
    def __sub__(self, other):
        return p((i - j for (i, j) in zip(self, other)))

    def __matmul__(self, other):
        return sum([i * j for (i, j) in zip(self, other)])

    def __and__(self, face):
        self.__face = p(face)
        return self

    def __or__(self, other):
        product = (self.__face or self - self) @ (p(other) - self)
        position = "side"
        if product > 0:
            position = "ahead"
        elif product < 0:
            position = "behind"
        print(f"{other} is {position} of {self}")
        return self


p((0, 0)) & (3, 4) | (1, 1) | (0, 0) | (-1, -1)

print_question(
    """
問4.

文字列操作:

以下の要件に相当する関数を実装し、Inputから入力する文字列を取得してテストするプログラムを実装せよ

・ この関数は、文字列をひとつ引数に取り、処理をした結果の文字列を戻り値として返す
・ 引数の文字列から0~9の数値を表す文字はそのままに、それ以外の文字は"*"（アスタリスク）に変換する
・ 数値であった文字をカウントし、変換した文字列の最後に"(num)"というようなフォーマットで文字数を追加する。なお、numはカウントした文字の数
・ 変換後の文字列を返り値として返す

上記のプログラムを実装し、動作検証を行い、その結果を出力せよ
"""
)


def transform_input(input_str: str) -> str:
    n, out = 0, ""
    for char in input_str:
        if char.isdigit():
            out += char
            n += 1
        else:
            out += "*"
    return f"{out}({n})"


base = "233aa3"
out = transform_input(base)
assert out == "233**3(4)"
print(f"transform {base} to {out}")

print_question(
    """
問5.

リストないしはディクショナリーを用いた処理:

添付として共有したファイル(univ.txt)には東京都内の大学一覧が記載されている。
その中から「亜細亜大学」のような大学名に同じ文字が複数用いられているものを判定して、
すべて表示するプログラムを実装せよ
"""
)


def print_dupe():
    path = __path__ / "univ.txt"
    with open(path, "r") as f:
        [print(l) for l in f.readlines() if len(set(l)) ^ len(l)]


print_dupe()

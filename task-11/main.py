#!/usr/bin/env python3

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
UNDERLINE = "\033[4m"
END = "\033[0m"


def print_question(question):
    return print(f"{UNDERLINE}{CYAN}{question}{END}{END}")


def assert_print(a, b):
    print(f"testing: {a} == {b} ?", end=" ")
    assert a == b
    print("...ok")


print_question(
    """
問1.

アトリビュートを確認する

クラスTestAttributeを作成し、その中にいくつかの変数、
関数を定義してdir関数を用いてそのクラスに存在しているアトリビュートのリストを表記するプログラムを実装せよ
""")


class TestAttribute:
    a = 1

    def __init__(self):
        self.b = 2

    def test(self):
        pass


print(dir(TestAttribute))


print_question(
    """
問2.

 typeを用いて型の違いを調べる

クラスAClassを作成して、int型のアトリビュートa_int、float型のアトリビュートa_float、string型のアトリビュートa_strを定義する

以下の要件を満たすメソッドをそれぞれ、作成し、動作を検証せよ

__init__(self, a) :
引数をint型、float型、string型に変換したものをそれぞれのアトリビュートに代入する

printData(self) :
以下ようなフォーマットで値を出力する

"
a_int = 101(int)
a_float = 101.0(float)
a_str = '101'(str)
"

※初期化メソッドで"101"を渡した場合を想定
""")


class AClass:

    def __init__(self, a):
        self.a_int = int(a)
        self.a_float = float(a)
        self.a_str = str(a)

    def printData(self):
        for a in ['a_int', 'a_float', 'a_str']:
            val = getattr(self, a)
            t = type(val).__name__
            if t == 'str':
                val = f"'{val}'"
            print(f"{a} = {val}({t})")


AClass("101").printData()


print_question(
    f"""
問.3

プロパティの復習

指定した値の累乗の数値を取り扱うクラスPowerを実装する

コンストラクタ__init__(self, x)では引数としてxを受け取り、自身持つアトリビュート_xに代入を行う

プロパティとして下記関数の定義を行う{END}

{RED}この２つの意味が逆になってる ==================> ・setX(self) : _xの値を返す{END}
{RED}この２つの意味が逆になってる ==================> ・getX(self, x) : _xの値を更新する{END}

{UNDERLINE}{CYAN}・getPowerOfX(self, n) : _xのn乗の値を返す

また動作検証として、上記のクラスに対して、クラスのインスタンスを作成し、それぞれの関数が返した値を出力するプログラムを実装せよ
""")


class Power:
    def __init__(self, x):
        self._x = x

    def getX(self):
        return self._x

    def setX(self, x):
        self._x = x

    def getPowerOfX(self, n):
        return self._x ** n


p = Power(2)
assert_print(p.getX(), 2)
p.setX(3)
assert_print(p.getX(), 3)
assert_print(p.getPowerOfX(2), 9)


print_question(
    """
問4.

型の取り扱い

上記Powerの__init__およびsetX関数に関して、引数として代入されてきた値が数値でなかった場合、
_xに対してNone(何も存在しないことを示す値)を代入するプログラムを実装せよ
""")


class Power2:
    def __init__(self, x):
        self.__setXOrNone(x)

    def getX(self):
        return self._x

    def setX(self, x):
        self.__setXOrNone(x)

    def getPowerOfX(self, n):
        return self._x ** n

    def __setXOrNone(self, x):
        self._x = x if isinstance(x, (int, float)) else None


p2 = Power2("test")
assert_print(p2.getX(), None)

print_question(
    """

問5.

例外処理を行う

線形補間を行う関数lerpを定義して正しく動いた場合と、例外の発生した場合の動作を検証せよ

この関数では引数として開始値a、終了値b、aとbの補間値tを定義する

パラメータtの動作範囲は0から1の値で制限されており、この関数は計算結果とメッセージを返すものとする（Python関数は複数の返り値を指定した場合、タプルで計算結果を返す）

処理の定義は下記、

・t = 0 の場合はaを返し、メッセージにはNoneを返す
・t = 1 の場合はbを返し、メッセージにはNoneを返す
・t > 0 かつ t < 1 の場合はaからbにtだけ移動した分の値を返し、メッセージにはNoneを返す
・なんらかの例外が発生して正しく計算できなかった場合は-1を返し、エラーメッセージを添えて返す

想定する例外処理として、下記の判定を行う

・a、bないしはtに対して、数値以外の値が入ってきた場合は例外を発生させる
・tが0から1の範囲にない場合はraiseを用いて例外を発生させる
"""
)


class OutOfRange(Exception):
    pass


def lerp(a, b, t):
    try:
        if 0 <= t <= 1:
            return a + (b-a)*t, None
        raise OutOfRange("tが0から1の範囲にない")
    except Exception as e:
        return -1, e


assert_print(lerp(1, 2, 1), (2, None))
assert_print(lerp(0, 2, 0), (0, None))
assert_print(lerp(2, 4, .5), (3, None))

ret, message = lerp("2", None, -1)
assert_print(ret, -1)
assert_print(isinstance(message, OutOfRange), True)

ret, message = lerp("2", None, -1)
assert_print(ret, -1)
assert_print(isinstance(message, Exception), True)

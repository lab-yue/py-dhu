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
半径rの円の面積を求めるプログラムをラムダ式を用いて実装し、確認としてrの値が3だった際の結果を出力するプログラムを実装せよ
"""
)


def area(r: float):
    from math import pi

    return pi * r ** 2


print(f"{area(3)}")

print_question(
    """
問2.
ある試験を実施したところ、受験者15人に対して、各人の平均点は下記のようになった。

64, 89, 43, 75, 91, 67, 47, 82, 30, 66, 87, 76, 54, 53, 86

試験結果の平均点mをリスト内包表記を用いて算出せよ
"""
)

# 内包表記にする意味がない
scores = [64, 89, 43, 75, 91, 67, 47, 82, 30, 66, 87, 76, 54, 53, 86]
m = sum(scores) / len(scores)
print(m)

print_question(
    """
問3.
問2.で算出した平均値を用いて、標準偏差sdを求め、各人の偏差値dvを求めるプログラムをリスト内包表記を用いて計算し、出力せよ。

なお、標準偏差の定義は下記を参照。

https://ja.wikipedia.org/wiki/%E6%A8%99%E6%BA%96%E5%81%8F%E5%B7%AE

偏差値の定義は、下記とする。

dv = 10 * (x - m) / sd + 50

※xは各人の点数
"""
)


def calc_dv(arr):
    from math import sqrt

    # from statistics import pstdev
    # sd = pstdev(scores)
    sd = sqrt(sum([(x - m) ** 2 for x in arr]) / len(arr))
    return [10 * (x - m) / sd + 50 for x in arr]


print(calc_dv(scores))

print_question(
    """
問4.
3と5の倍数のときは"Fizz Buzz"、3の倍数のときは"Fizz"、5の倍数のときは"Buzz"、それ以外の場合はその数値を返すプログラムをジェネレータfizz_buzz_generatorを使って作成し、1から30までの結果を出力するプログラムを実装せよ
"""
)


def fizz_buzz_generator(m: int):
    n = 1
    while n <= m:
        yield {0b10: "Fizz", 0b01: "Buzz", 0b00: "Fizz Buzz"}.get(
            int(bool(n % 3)) | int(bool(n % 5)) << 1, n
        )
        n += 1


[print(n) for n in fizz_buzz_generator(30)]

print_question(
    """
問5.
下記の関数に対して、文字列の始まりに[start]を終わりに[end]を挿入するデコレータdecoを作成し、動作を確認せよ。

def print_message(message):
    print(message)
"""
)


def deco(fn):
    def wrapper(message):
        return fn(f"[start]{message}[end]")

    return wrapper


@deco
def print_message(message):
    print(message)


print_message("test")

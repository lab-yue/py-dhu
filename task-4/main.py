#!/usr/bin/env python3

from math import pi

CYAN = '\033[96m'
UNDERLINE = '\033[4m'
END = '\033[0m'


def print_question(question): return print(
    f"{UNDERLINE}{CYAN}{question}{END}{END}")


def assert_print(a, b):
    print(f"{a} == {b}")
    assert a == b


print_question("""
問1.
Input関数を用いて入力を整数として受け取り、
値を2倍にして下記のようなフォーマットで出力するプログラムを実装せよ。
"Xの2倍の値はYです"
※Xは入力された数値、Yは算出した数値
""")


def Q1():
    try:
        x = int(input("X="))
        print(f"{x}の2倍の値は{x*2}です")
    except:
        pass


Q1()


print_question("""
問2.
数値を受け取り、3の倍数である際は"Fizz"、5の倍数である際は"Buzz"、
3の倍数であり5の倍数でもある場合は"Fizz Buzz"、
それ以外の場合は与えられた数値を出力する関数fizz_buzz(n)を実装せよ。
また、動作検証を行うコードを組み込み、1から30までの数値に対する出力を例示せよ。
""")


fizz_buzz_map = {0b10: "Fizz", 0b01: "Buzz", 0b00: "Fizz Buzz"}


def fizz_buzz(num: int):
    _hash = int(bool(n % 3)) | int(bool(n % 5)) << 1
    _val = fizz_buzz_map.get(_hash, num)
    return _val


for n in range(1, 31):
    print(n, fizz_buzz(n))

print_question("""
問3.
オイラー角をラジアンに変換して戻り値として返す関数radian(degree)を実装せよ。
また、動作検証を行うコードを組み込み動作を例示せよ。
""")


def radian(degree: int) -> float:
    return degree * (pi / 180)


assert_print(radian(0), 0)
assert_print(radian(90), pi / 2)
assert_print(radian(180), pi)
assert_print(radian(360), 2 * pi)


print_question("""
問4.
与えられた整数nに対して、1からnまでの和を求める関数sum(n)をsum(n) = n + sum(n - 1)でかつ、
nが0より小さい場合はsum(n) = 0として定義する。
この関数の戻り値が360を超える最も小さなnの値を算出するプログラムを実装し、結果を出力せよ。
""")


def _sum(n: int):
    if n < 0:
        return 0
    return n + _sum(n - 1)


n = 1
while True:
    if _sum(n) > 360:
        break
    n += 1
print(n)

print_question("""
問5.
モールス信号をアルファベットへ変換する関数convert_mools(str)を実装し、下記の文言を英語へ変換した結果を出力せよ。なお、モールス信号はこちら（https://ja.wikipedia.org/wiki/%E3%83%A2%E3%83%BC%E3%83%AB%E3%82%B9%E7%AC%A6%E5%8F%B7）の欧文モールス信号に準拠し、区切り文字は" "(全角スペース)である。

"・－　－・　－・－－　　－・－・　－－－　－・・　・　　－・・　－－－　・　・・・　－・　　－　　・－・　・・－　－・　　・－　・・・　　－・－－　－－－　・・－　　－　・・・・　－－－　・・－　－－・　・・・・　－　　　・－・　・・－　－・　　・－　・・・　　・・　－　　・－－　・－・　－－－　－　・　"
""")

mools = {
    "・－": "a",
    "－・・・": "b",
    "－・－・": "c",
    "－・・": "d",
    "・": "e",
    "・・－・": "f",
    "－－・": "g",
    "・・・・": "h",
    "・・": "i",
    "・－－－": "j",
    "－・－": "k",
    "・－・・": "l",
    "－－": "m",
    "－・": "n",
    "－－－": "o",
    "・－－・": "p",
    "－－・－": "q",
    "・－・": "r",
    "・・・": "s",
    "－": "t",
    "・・－": "u",
    "・・・－": "v",
    "・－－": "w",
    "－・・－": "x",
    "－・－－": "y",
    "－－・・": "z",
    "－－－－－": "0",
    "・－－－－": "1",
    "・・－－－": "2",
    "・・・－－": "3",
    "・・・・－": "4",
    "・・・・・": "5",
    "－・・・・": "6",
    "－－・・・": "7",
    "－－－・・": "8",
    "－－－－・": "9",
}


def convert_mools(code) -> str:
    return "".join([mools.get(c, " ") for c in code.split("　")])


message = convert_mools(
    "・－　－・　－・－－　　－・－・　－－－　－・・　・　　－・・　－－－　・　・・・　－・　　－　　・－・　・・－　－・　　・－　・・・　　－・－－　－－－　・・－　　－　・・・・　－－－　・・－　－－・　・・・・　－　　　・－・　・・－　－・　　・－　・・・　　・・　－　　・－－　・－・　－－－　－　・　"
)
print(message)

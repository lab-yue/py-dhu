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
共有ファイル（int_list.txt）からデータを一行ごとに数として読み込み、
数値が3の倍数なら"Fizz"、5の倍数なら"Buzz"、3および5の倍数なら"Fizz Buzz"、
それ以外であれば読み込んだ数値をそのまま出力するプログラムを実装せよ
"""
)

fizz_buzz_map = {0b10: "Fizz", 0b01: "Buzz", 0b00: "Fizz Buzz"}


def read_fizz_buzz():
    path = __path__ / "int_list.txt"
    with path.open("r") as f:
        for l in f.readlines():
            n = int(l)
            _hash = int(bool(int(l) % 3)) | int(bool(int(l) % 5)) << 1
            print(fizz_buzz_map.get(_hash, n))


read_fizz_buzz()

print_question(
    """
問2.
共有ファイル（poem.txt）には映画『探偵はBARにいる』で取り上げられた萩原朔太郎の詩のひとつが記録されている。
これを読み込み、句点「。」および読点「、」ごとに分割し、
その中に存在する日本語の母音のひらがな「あ」「い」「う」「え」「お」が何文字含まれるのかをカウントし、
下記のようなフォーマットで出力するプログラムを実装せよ。
泥酔の翌朝に於けるしらじらしい悔恨は、(母音数:1)
病んで舌をたれた犬のやうで、(母音数:1)
魂の最も痛々しいところに噛みついてくる。(母音数:2)
"""
)


def count_vowel():
    import re
    from collections import Counter

    line_regex = re.compile(r"[\s\S]+?[。、]")
    path = __path__ / "poem.txt"
    with path.open("r") as f:
        poem = f.read()
    for part in line_regex.findall(poem):
        c = Counter(part)
        vowels = sum([c[v] for v in ["あ", "い", "う", "え", "お"]])
        print(f"{part}(母音数:{vowels})")


count_vowel()

print_question(
    """
問3.
inputを用いて数値を2回受け取り、aとbという変数に代入して、下記のようなフォーマット（a = 2, b = 3だった場合）で外部ファイルへ出力するプログラムを実装せよ。

2 + 3 = 5

なお、ファイル名はsum.txtとする
"""
)


def write_sum_to_txt():
    [a, b] = [int(input(f"{_} = "))for _ in ['a', 'b']]
    path = __path__ / "sum.txt"
    with path.open("w") as s:
        s.write(f"{a} + {b} = {a+b}")


write_sum_to_txt()


print_question(
    """
問4.
inputを用いて入力値を繰り返し受け取り、
それが数値だった場合にはその数値を整数に変換したものを、
数値以外の文字列だった場合には”NULL”という文字列を一行ずつ出力し、
"quit"または"q"という文字列が入力された場合には何も出力せずに実行を終了するプログラムを実装せよ。
なお、ファイル名はinput.txtとする
"""
)


def input_loop():
    path = __path__ / "input.txt"
    with path.open("a") as f:
        while 1:
            i = input("input = ")
            if i in ["q", "quit"]:
                return
            try:
                num = int(float(i))
                f.write(f"{num}\n")
            except:
                f.write("NULL\n")


input_loop()

print_question(
    """
問5.
曜日計算を求める公式として普及しているツェラーの公式が下記の定義である。

y年m月d日の曜日を求める際に、グレゴリオ暦(Gregorian)での曜日hは

h = (d + [13 * (m + 1) / 5] + Y + [Y / 4] + 5 * C + [C / 4]) mod 7

※ a mod bはaをbで割った余り(a % bと同様の定義)
※ [X]はガウス記号とし、ｘを超えない最大の整数とする(math.floorと同様の定義)

C = [y / 100]
Y = y mod 100

と定義し、数値hの曜日との対応表は下記とする。

上記の式を適応して、inputから受けたy、m、dの数値に対して曜日hを計算し、
"月曜日"のような文字列に変換して出力するプログラムを実装せよ
"""
)


def calc_day(y: int, m: int, d: int) -> str:
    from math import floor as f

    C, Y = f(y / 100), y % 100
    return {
        1: "日",
        2: "月",
        3: "火",
        4: "水",
        5: "木",
        6: "金",
        0: "土",
    }.get((d + f(13 * (m + 1) / 5) + Y + f(Y / 4) + 5 * C + f(C / 4)) % 7) + "曜日"


print(calc_day(*[int(input(f"{_} = ")) for _ in ["y", "m", "d"]]))

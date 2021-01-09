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

標準ライブラリを扱う。datetimeを用いた日時操作

Inputから受け取った文字列からdatetimeオブジェクトを生成し、出力するプログラムを実装せよ。

なお、入出力に用いるフォーマットは下記のようなものとする。

入力例 :
2021/1/11

出力例 :
2021年1月11日（土）
"""
)


def get_date(time: str):
    try:
        from datetime import datetime

        # -> not working
        # import locale
        # locale.setlocale(locale.LC_TIME, 'Japanese_Japan.UTF-8')

        d = datetime.strptime(time, "%Y/%M/%d")
        weekday = [
            "土",
            "日",
            "月",
            "火",
            "水",
            "木",
            "金",
        ][d.weekday()]
        return f"{d.year}年{d.month}月{d.day}日（{weekday}）"
    except:
        print(f"time {time} is invalid")


assert_print(get_date("2021/1/11"), "2021年1月11日（土）")
get_date(input("please input time: "))


print_question(
    """
問2.

標準ライブラリを扱う。calendar機能を用いた出力

datetime.now()では現在時点の日時を取得することができる。この関数及びcalendarモジュールを用いて、現在時点から1500日後の月のカレンダーを描画するためのプログラムを実装せよ。
"""
)


def get_date_1500_days_later():
    import calendar
    from datetime import datetime, timedelta

    future = datetime.now() + timedelta(days=1500)
    print(calendar.month(future.year, future.month))


get_date_1500_days_later()


print_question(
    """
問.3

標準ライブラリを扱う。osを用いたシステム制御

ルートディレクトリ"/"直下に配置されているディレクトリおよびファイルを下記のフォーマットで出力するためのプログラムを実装せよ。

ディレクトリの場合：
"D : directory_name"

ファイルの場合：
"F : file_name (file_size)"
"""
)


def list_root_dir():
    import os

    for path in os.listdir("/"):
        path = os.path.join("/", path)
        if os.path.isdir(path):
            print(path)
        elif os.path.isfile(path):
            size = os.path.getsize(path)
            print(f"{path} ({size})")


list_root_dir()


print_question(
    """
問4.

標準ライブラリを扱う。mathを用いた数値計算

3次元空間の座標p1(2.9, 3.0, 7.1)から、秒速v(1.2, 2.5, 0.1)で移動した際の9秒後の座標p2(3.7,  5.4, 5.3)との距離を求めるプログラムを実装せよ。
"""
)


def calc_distance(p1, v, t, p2):
    import math

    (p1x, p1y, p1z) = p1
    (sx, sy, sz) = v
    (p2x, p2y, p2z) = p2
    delta = math.dist([p1x + t * sx, p1y + t * sy,
                       p1z + t * sz], [p2x, p2y, p2z])
    return delta


print(calc_distance(p1=(2.9, 3.0, 7.1), p2=(
    3.7, 5.4, 5.3), v=(1.2, 2.5, 0.1), t=9))

print_question(
    """
問5.

標準ライブラリを扱う。Jsonへのデータ変換

ユーザデータのやり取りをJsonで取り扱うシステムで、IDが1となっているユーザの情報を確認したところ、下記のデータが返されたものとする。

{
   "Id" : 1
   "AreaFrom" : "Tokyo",
   "BirthYear" : "2001",
   "Gender" : "Male"
 }

同様のフォーマットでID、出身地、誕生年、性別をJson文字列で出力するプログラムを作成し、動作検証として任意の値を入れた結果を出力せよ。
"""
)


def get_info(base: str):
    try:
        import json
        data = json.loads(base)
        for (k, v) in [
            ("Id", "ID"),
            ("AreaFrom", "出身地"),
            ("BirthYear", "誕生年"),
            ("Gender", "性別"),
        ]:
            data[v] = data.pop(k)
        return json.dumps(data, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"base data is not valid json: {e}")


print(get_info(
    """
{
    "Id" : 1,
    "AreaFrom" : "Tokyo",
    "BirthYear" : "2001",
    "Gender" : "Male"
}
"""
))

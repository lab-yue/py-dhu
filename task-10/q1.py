#!/usr/bin/env python3

import DHUPythonDev
from utils import print_question

print_question(
    """
問1.
下記の要件を満たすクラスを実装せよ

1-2.
【定義したモジュールを利用する】
上記constに定義した数値tauをprintを用いて出力するプログラムを実装せよ。
"""
)

print(DHUPythonDev.const.τ)


print_question(
    """
1-5.
【定義したモジュールを利用する】
ここまでのテストとして、inputを用いて受けた数値を半径として、円の面積を出力するプログラムを実装せよ
"""
)

print(DHUPythonDev.math.Math.circleArea(10))

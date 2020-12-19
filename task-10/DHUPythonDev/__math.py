#!/usr/bin/env python3

"""
1-3.
【モジュール内にクラスとクラスメソッドを定義する】
数値処理を行うモジュールmathを作成し、その内部にMathクラスを作成し、引数rを受けて円の面積を求めるメソッドcircleAreaを実装せよ。
"""


class Math:
    @staticmethod
    def circleArea(r):
        from math import pi
        return pi * r ** 2

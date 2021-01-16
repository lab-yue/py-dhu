#!/usr/bin/env python3
def log(fn):
    def wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        print(ret)
        return ret

    return wrapper


def with_question(q):
    question_text = "\n".join(map(lambda line: line.lstrip(), q.question.split("\n")))
    print(f"\n{q.__name__}: {question_text}")
    return q


class Q1:
    question = """
    1から100までの数字を加算して出力するプログラムを実装せよ
    """

    @staticmethod
    @log
    def run(start: int, end: int, n=int) -> int:
        return (start + end) * n / 2


assert with_question(Q1).run(start=1, end=100, n=100) == 5050


class Q2:
    question = """
    1から100までの数字の中から7の倍数のみを出力するプログラムを実装せよ
    """

    @staticmethod
    def run(start: int, end: int, should_print):
        [print(n) for n in range(start, end + 1) if should_print(n)]


with_question(Q2).run(start=1, end=100, should_print=lambda n: n % 7 == 0)


class Q3:
    question = """
    1から100までの数値をループして、通常時はその数値を、3で割り切れる場合は"Fizz"、5で割り切れる場合は"Buzz"、3と5の両者で割り切れる場合は"Fizz Buzz"を出力するプログラムを実装せよ
    """

    @staticmethod
    def run(start: int, end: int):
        fizz_buzz = {0b01: "Fizz", 0b10: "Buzz", 0b11: "Fizz Buzz"}
        for n in range(start, end + 1):
            # python 3.9
            if val := fizz_buzz.get(int(not n % 3) | int(not n % 5) << 1):
                print(val)
                # for debug
                # print(f"{n} --> {val}")

            # python under 3.9
            # val = fizz_buzz.get(
            # int(not n % 3) | int(not n % 5) << 1
            # )
            # if val:
            # print(f"{n} --> {val}")
            # print(val)


with_question(Q3).run(
    start=1,
    end=100,
)


class Q4:
    question = """
    1から100までの数字の中から素数（1と自分自身以外で割り切れない1以外の数値）のみを出力するプログラムを実装せよ
    """

    @staticmethod
    def run(*args, **kwargs):
        return Q2.run(*args, **kwargs)

    @staticmethod
    def is_prime(num: int) -> bool:
        return num != 1 and all(num % i != 0 for i in range(2, num))


with_question(Q4).run(start=1, end=100, should_print=Q4.is_prime)


class Q5:
    question = """
    1から数え上げた際に現れる100以下のメルセンヌ素数をすべて出力するプログラムを実装せよ。なお、単語の定義は以下となる

    メルセンヌ数 : 2のべき乗よりも 1 小さい自然数、すなわち 2n − 1（n は自然数）の形の自然数
    メルセンヌ素数 : メルセンヌ数でかつ素数であるもの
    """

    @staticmethod
    def run(end: int):
        start = 1
        while True:
            start += 1
            num = 2 ** start - 1
            if num > end:
                break
            if Q4.is_prime(num):
                print(num)


with_question(Q5).run(end=100)

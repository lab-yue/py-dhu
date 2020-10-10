#!/usr/bin/env python3
def log(fn):
    def wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        print(ret)
        return ret

    return wrapper


def with_question(q):
    print("\n".join(map(lambda line: line.lstrip(), q.question.split("\n"))))
    return q


class Q1:
    question = """
    問1.
    自転車を漕いで、時速17Kmで移動した際の25分後の移動距離を出力するプログラムを記載せよ
    """

    @staticmethod
    @log
    def run(pairs):
        return sum(map(lambda pair: pair[0] * pair[1] / 60, pairs))


assert with_question(Q1).run([(17, 25)]) == 17 * 25 / 60


class Q2:
    question = """
    問2.
    設問1の最後の5分間を時速17Kmの30%の速度で移動した際の移動距離を求めるプログラムを記載せよ
    """

    @staticmethod
    def run(*args):
        return Q1.run(*args)


assert with_question(Q2).run([(17, 20), (17 * 0.3, 5)]) == (17 * 20 + 17 * 0.3 * 5) / 60


class Q3:
    question = """
    問3.
    縦3mm、横7mm、高さ11mmの物体があった際に、その物体を横に3の11乗個、縦に7の3乗個、上下に10個重ねた際の体積を求めるプログラムを記載せよ
    """

    @staticmethod
    @log
    def run(cube: (int, int, int), size: (int, int, int)):
        from functools import reduce
        from operator import mul

        return reduce(mul, [*cube, *size])


assert (
    with_question(Q3).run((3, 7, 11), (3 ** 11, 7 ** 3, 10))
    == 3 * 7 * 11 * 3 ** 11 * 7 ** 3 * 10
)


class Q4:
    question = """
    問4.
    身長170cm、体重65kgの人間のBMI（Body Mass Index、身長の2乗に対する体重の比）を算出するプログラムを記載せよ
    """

    @staticmethod
    @log
    def run(height: int, weight: int):
        return weight / (height / 100) ** 2


assert with_question(Q4).run(height=170, weight=65) == 65 / 1.7 ** 2


class Q5:
    question = """
    問5.
    月に額面210,000円の給与を取得して、毎月23,900円の税金（源泉徴収税）、20,130円の保険料（健康保険・厚生年金）を差し引かれた際の、年間の手取り額を算出するプログラムを記載せよ
    """

    @staticmethod
    @log
    def run(salary: int, tax: int, insurance: int):
        return (salary - tax - insurance) * 12


assert (
    with_question(Q5).run(salary=210_000, tax=23_900, insurance=20_130)
    == (210_000 - 23_900 - 20_130) * 12
)

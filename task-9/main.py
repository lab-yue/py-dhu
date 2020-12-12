#!/usr/bin/env python3

GREEN = '\033[92m'
CYAN = "\033[96m"
YELLOW = '\033[93m'
RED = '\033[91m'
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
下記の要件を満たすクラスを実装せよ

Ⅰ.
あるRPGタイトルのゲーム内のキャラクターを管理するためのクラスとしてCharacterBaseクラスを定義するものとする。

変数として下記のものを宣言して実装せよ。

・個体識別を行うための変数、CharacterId

・名前を管理するための変数、Name

・最大の体力を管理するための変数、HP

・現在の体力を管理するための変数、CurrentHP


Ⅱ.
宣言したCharacterBaseクラスに対して、メソッド__init__（コンストラクタ）を作成し、引数をそれぞれ定義し、1.で宣言した変数に代入して初期化するためのプログラムを作成せよ。


Ⅲ.
宣言したCharacterBaseクラスに対して、メソッドAddDamageを作成し、ダメージ付与を行うためのプログラムを実装せよ。なお、要件は下記とする。

・第一引数damageで付与ダメージを定義する

・CurrentHPに対して、damage分減算を行い、もしマイナスの数値になったら0を代入する


Ⅳ.
操作キャラクターを監視するためのクラスCharacterを、CharacterBaseクラスの子クラスとして、下記の要件を満たすプログラムを実装せよ。

・攻撃力を管理するための変数、AttackPower

・経験値を管理するための変数、Exp

・次のレベルに到達するための値を管理するための変数、NextLevelExp

・__init__から上記変数Expに対しても初期化を行い、もし変数に値が入っていなければ0とする


Ⅴ.
Characterクラスに次のレベルに到達するのに必要な値を表すためのプロパティ、ExpRemainを定義する。なお、要件は下記とする。

・ゲッターの名前はGetExpRemainとする

・値がマイナスになった場合は0を返す


※Ⅰ~Ⅴまでの変数名、メソッド名、プロパティ名は適宜変更しても良いが、一読して意味の通じる命名規則になっていること

"""
)


class CharacterBase:

    def __init__(self, CharacterId: str, Name: str, HP: int, CurrentHP: int):
        self.__CharacterId = CharacterId
        self.Name = Name
        self.__HP = HP
        self.__CurrentHP = CurrentHP

    def AddDamage(self, damage: int) -> int:
        tmp = max(self.__CurrentHP - damage, 0)
        diff = damage if tmp else self.__CurrentHP
        self.__CurrentHP = tmp
        return diff

    @property
    def id(self):
        return self.__CharacterId

    @property
    def isAlive(self):
        return self.__CurrentHP > 0


class Character(CharacterBase):

    def __init__(self, Group: str, AttackPower: int = 0, Exp: int = 0, NextLevelExp: int = 0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Group = Group
        self.__AttackPower = AttackPower
        self.__Exp = Exp
        self.__NextLevelExp = NextLevelExp
        self.__ExpRemain = 0
        self.__ExpMap = {}

    @property
    def Exp(self):
        return self.__Exp

    @property
    def ExpRemain(self):
        return self.__NextLevelExp - self.__Exp

    @ExpRemain.getter
    def GetExpRemain(self) -> int:
        return max(self.ExpRemain, 0)

    def Attack(self, target):
        damage = target.AddDamage(self.__AttackPower)
        print(
            f"{self.Group}[{self.Name}のターン]{END}{target.Name}に対して攻撃を行った。{damage}のダメージ")
        if target.isAlive:
            self.__ExpMap[target.id] = self.__ExpMap.get(target.id, 0) + damage
        else:
            print(f"{RED}{target.Name}は倒れた{END}")
            self.__Exp += self.__ExpMap.pop(target.id, 0) + damage


print_question(
    """
問2.
実装したクラスの検証を行うための、下記の要件を満たすテストコードを実装し、動作を確認せよ

Ⅰ.
Characterクラスのインスタンスとして、下記の3人のキャラクターを生成する

主人公：
CharacterId : 1
Name : 主人公
HP : 100
CurrentHP : 100
AttackPower : 1
Exp : 0
NextLevelExp : 10

エネミー1：
CharacterId : 2
Name : エネミー1
HP : 3
CurrentHP : 3
AttackPower : 1
Exp : 0
NextLevelExp : 0

エネミー2：
CharacterId : 3
Name : エネミー2
HP : 5
CurrentHP : 5
AttackPower : 1
Exp : 0
NextLevelExp : 0


Ⅱ.
上記の3人のキャラクターはそれぞれ、順番に下記の行動を行う。

①主人公が生存している場合、エネミー1が生存していればエネミー1に、そうでなければエネミー2に対して攻撃を行う

②エネミー1が存在している場合、主人公に対して攻撃を行う

③エネミー2が存在している場合、主人公に対して攻撃を行う

なお、生存の定義はCurrentHPが0より大きい場合。攻撃の定義はAttackPower分の値をCurrentHPから減算するものとする。

また、主人公の攻撃によりエネミーが倒れた場合、付与したダメージ分の経験値としてExpに加算する


Ⅲ.
上記の行動に対して、下記要件のログを出力する

①検証開始時、"バトル開始"

②攻撃を行った場合、"[Aのターン]Bに対して攻撃を行った。Cのダメージ"

③上記攻撃で相手を倒した場合、"Aは倒れた"

④主人公が倒れたないしはすべてのエネミーが倒れた場合、"バトル終了"

⑤最後まで生存していたのが主人公だった場合、”Aの経験値を取得した。次のレベルまでB”
"""
)


def parse(character_info: str):
    info = {}
    separator = " : "
    for l in character_info.splitlines():
        if separator not in l:
            continue
        k, v = l.split(separator)
        info[k] = int(v) if v.isnumeric() else v
    return info


class Group:
    PLAYER = CYAN
    ENEMY = YELLOW


class TestGame:

    def __init__(self, players):
        self.__TurnIndex = 0
        self.__Players = players

    @property
    def CurrentPlayer(self):
        return self.__Players[self.__TurnIndex % len(self.__Players)]

    @property
    def AlivePlayers(self):
        return [p for p in self.__Players if p.isAlive]

    @property
    def GroupWin(self):
        aliveGroups = set([p.Group for p in self.AlivePlayers])
        if len(aliveGroups) == 1:
            return aliveGroups.pop()
        return None

    @property
    def Target(self):
        for target in self.AlivePlayers:
            if self.CurrentPlayer.Group != target.Group:
                return target
        return None

    def run(self):
        print(f"{GREEN}バトル開始{END}")
        while self.Target:
            if self.CurrentPlayer.isAlive:
                self.CurrentPlayer.Attack(self.Target)
            self.__TurnIndex += 1
        self.end()

    def end(self):
        print(f"{GREEN}バトル終了{END}")
        if self.GroupWin == Group.PLAYER:
            for a in self.AlivePlayers:
                print(f"{GREEN}{a.Exp}の経験値を取得した。次のレベルまで{a.GetExpRemain}{END}")


player = Character(**parse(f"""
CharacterId : 1
Name : 主人公
HP : 100
CurrentHP : 100
AttackPower : 1
Exp : 0
NextLevelExp : 10
Group : {Group.PLAYER}
"""))

enemy_1 = Character(
    **parse(
        f"""
CharacterId : 2
Name : エネミー1
HP : 3
CurrentHP : 3
AttackPower : 1
Exp : 0
NextLevelExp : 0
Group : {Group.ENEMY}
"""
    )
)

enemy_2 = Character(
    **parse(
        f"""
CharacterId : 3
Name : エネミー2
HP : 5
CurrentHP : 5
AttackPower : 1
Exp : 0
NextLevelExp : 0
Group : {Group.ENEMY}
       """
    ))


TestGame([player, enemy_1, enemy_2]).run()

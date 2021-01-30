#!/usr/bin/env python3
"""
以下にあるpokemonのデータファイルを読んで、
https://github.com/fanzeyi/pokemon.json
(pokedex.json)
"""


import json
import statistics
from pathlib import Path

__parent__ = Path(__file__).parent

with open(__parent__ / "pokedex.json", "r") as f:
    pokedex = json.load(f)


def get_pokemon_by_index(index: int):
    """
    ＊図鑑番号を指定すると対応するポケモンを表示する
    """
    for p in pokedex:
        if p["id"] == index:
            print(p)
            return


get_pokemon_by_index(151)


def get_pokemon_en_name_by_jp_name(name: str):
    """
    ＊日本語のポケモン名を指定すると英語のポケモン名を表示する
    """

    for p in pokedex:
        if p["name"]["japanese"] == name:
            print(p["name"]["english"])
            return


get_pokemon_en_name_by_jp_name("ミロカロス")


def list_top_3_pokemon_by_atk():
    """
    ＊こうげきりょくの強い１から３位のポケモンを表示
    """
    return [
        print(p)
        for p in sorted(pokedex, key=lambda pokemon: -pokemon["base"]["Attack"])[:3]
    ]


list_top_3_pokemon_by_atk()


def list_bottom_3_pokemon_by_speed():
    """
    ＊すばやさの遅い１から３位のポケモンを表示
    """
    return [
        print(p)
        for p in sorted(pokedex, key=lambda pokemon: pokemon["base"]["Speed"])[:3]
    ]


list_bottom_3_pokemon_by_speed()

speed_avg = statistics.mean([p["base"]["Speed"] for p in pokedex])


def find_fire_fighter(index: int):
    """
    ＊消防士向きのポケモンを探す
     図鑑番号を指定して
     水のタイプをもっていて、すばやさが平均以上の
     ポケモンであれば、採用と表示する
    """
    for p in pokedex:
        if (
            p["id"] == index
            and "Water" in p["type"]
            and p["base"]["Speed"] >= speed_avg
        ):
            print("採用")
            return


find_fire_fighter(230)


defence_median = statistics.median([p["base"]["Defense"] for p in pokedex])


def find_electricity_producer(index: int):
    """
    ＊発電向きのポケモンを探す
     図鑑番号を指定して
     でんきのタイプをもっていて、ぼうぎょりょくが中央値以上の
     ポケモンであれば、採用と表示する
    """
    for p in pokedex:
        if (
            p["id"] == index
            and "Electric" in p["type"]
            and p["base"]["Defense"] >= defence_median
        ):
            print("採用")
            return


find_electricity_producer(243)

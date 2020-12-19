#!/usr/bin/env python3

"""
問2.
外部モジュールを利用する

外部モジュールとして、画像処理を行うための機能セットであるOpenCVを利用する。

<<--- Memo --->>
OpenCVで用いる画像認識は、認識を行うための正しい画像、正しくない画像を用いて分類を行った教師データを用いて判定をかける分類方法を用いている。

この分類を行う中で各画像が保有している「特徴」を分析し、その抽出を行う。

学習された「特徴量」をまとめたデータのことを「カスケード分類器」や「カスケードファイル」と呼ぶ。

このカスケード分類機を用いて、顔認証を行うためのプログラムをサンプルとして共有する。
<<--- Memo --->>


サンプルデータとして添付された"DataSamples.zip"を利用する。


まず、下記の命令をコマンドライン（ターミナル）から実行してAnacondaを更新する。

conda update conda -c conda-canary

もし、下記の確認がされた場合はyを入力してEnterを押下する。

Proceed ([y]/n)?

それが済んだら、下記の命令を参考にanacondaに対してOpenCVをインストールする。

ライブラリ検索命令:
conda search {name}

ライブラリインストール命令:
conda install {name}={version}={build}

※name、 version、 buildにはそれぞれ"opencv"、インストールするバージョン、ターゲットとなるビルドを記載する


インストール後に、OpenCVを用いた画像処理を行う。

まず、検証として、共有された下記のファイルを実行する。

OpenCVTest.ipynb

・グレースケール化
・顔認証


当プログラムを参考にして、共有されたカスケードファイルcat_cascade.xml(参考 : https://github.com/wellflat)及び試験データcat_sample1~3.jpgを用いて、下記のプログラムを実装せよ。

・猫の顔認証を行い、顔を四角で囲むプログラムを実装せよ

・下記の手法で画像の特徴点検出を行い描画するためのプログラムを実装せよ

> Scale Invariant Feature Transform(SIFT)アルゴリズムを用いて特徴点の検出をする
> 参考 : https://docs.opencv.org/3.4/d5/d3c/classcv_1_1xfeatures2d_1_1SIFT.html

> 取得した特徴点(KeyPoints)に対して可視化を行う
# gab958f8900dd10f14316521c149a60433
> 参考 : https://docs.opencv.org/3.4/d4/d5d/group__features2d__draw.html
"""

import cv2
from pathlib import Path

__parent__ = Path(__file__).parent


def to_absolute(p):
    return str(p.absolute())


faceCascade = cv2.CascadeClassifier(
    to_absolute(__parent__ / "DataSamples/CatSamples/Cascades/cat_cascade.xml")
)


def detect(file_path: str):
    file_in = to_absolute(file_path)
    file_out = to_absolute(__parent__ / "out" / f"detected_{file_path.name}")

    print(f"start processing {file_in}")

    imgBGR = cv2.imread(file_in)
    imgGray = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, minNeighbors=1, minSize=(80, 80))

    for (x, y, w, h) in faces:
        imgBGR = cv2.rectangle(imgBGR, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.imwrite(file_out, imgBGR)

    print(f"end processing {file_out}")


if __name__ == "__main__":
    from multiprocessing import Pool

    imgs = Path(__parent__ / "DataSamples/CatSamples/Images").glob("*.jpg")

    pool = Pool()
    pool.map(detect, imgs)
    pool.close()
    pool.join()

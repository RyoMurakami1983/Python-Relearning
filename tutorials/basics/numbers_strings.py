#!/usr/bin/env python3
"""
Python基礎: 数値と文字列
Python公式チュートリアル 3章の内容を実践
"""

print("=== 数値の基本操作 ===")

# 基本的な算術演算
print("算術演算:")
print(f"2 + 2 = {2 + 2}")
print(f"50 - 5*6 = {50 - 5*6}")
print(f"(50 - 5*6) / 4 = {(50 - 5*6) / 4}")
print(f"8 / 5 = {8 / 5}")  # 除算は常にfloatを返す

# 整数除算と剰余
print(f"\n整数除算と剰余:")
print(f"17 // 3 = {17 // 3}")  # 整数除算
print(f"17 % 3 = {17 % 3}")   # 剰余
print(f"5 * 3 + 2 = {5 * 3 + 2}")  # 除算の検証

# べき乗
print(f"\nべき乗:")
print(f"5 ** 2 = {5 ** 2}")
print(f"2 ** 7 = {2 ** 7}")

# 変数の使用
print(f"\n=== 変数の使用 ===")
width = 20
height = 5 * 9
area = width * height
print(f"幅: {width}, 高さ: {height}")
print(f"面積: {area}")

print(f"\n=== 文字列の基本操作 ===")

# 文字列の作成
single_quote = 'シングルクォート'
double_quote = "ダブルクォート"
print(f"シングルクォート: {single_quote}")
print(f"ダブルクォート: {double_quote}")

# エスケープ文字
print('doesn\'t')  # エスケープ
print("doesn't")   # 混合引用符
print('"Yes," they said.')

# 改行とタブ
print("改行を含む文字列:\n  - 1行目\n  - 2行目")
print("タブを含む文字列:\tタブ後の文字")

# 生文字列
print(r"生文字列では\nそのまま表示される")

# 複数行文字列
multiline = """
複数行の
文字列を
作成できます
"""
print(multiline)

# 文字列の連結
prefix = "Py"
suffix = "thon"
combined = prefix + suffix
print(f"連結: {prefix} + {suffix} = {combined}")

# 文字列の繰り返し
repeated = "Python! " * 3
print(f"繰り返し: {repeated}")

# 文字列のインデックス
word = "Python"
print(f"\n=== 文字列のインデックス ===")
print(f"word = '{word}'")
print(f"word[0] = '{word[0]}'")  # 最初の文字
print(f"word[5] = '{word[5]}'")  # 6番目の文字
print(f"word[-1] = '{word[-1]}'")  # 最後の文字
print(f"word[-2] = '{word[-2]}'")  # 最後から2番目

# 文字列のスライス
print(f"\n=== 文字列のスライス ===")
print(f"word[0:2] = '{word[0:2]}'")  # 0から1まで
print(f"word[2:5] = '{word[2:5]}'")  # 2から4まで
print(f"word[:2] = '{word[:2]}'")    # 最初から1まで
print(f"word[4:] = '{word[4:]}'")    # 4から最後まで
print(f"word[-2:] = '{word[-2:]}'")  # 最後から2番目から最後まで

# 文字列の長さ
print(f"\n文字列の長さ: len('{word}') = {len(word)}")

# 文字列は変更不可能
print(f"\n文字列は変更不可能（immutable）です")
try:
    # word[0] = 'J'  # これはエラーになる
    pass
except TypeError as e:
    print(f"エラー: {e}")

# 新しい文字列を作成
new_word = 'J' + word[1:]
print(f"新しい文字列: '{new_word}'")
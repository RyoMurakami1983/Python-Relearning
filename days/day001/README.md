# Day 001: Python基礎とインタープリターの使い方

## 📚 学習内容

### 公式ドキュメントの対象セクション
- [Python チュートリアル 1. やる気を引き出してくれるもの](https://docs.python.org/ja/3/tutorial/appetite.html)
- [Python チュートリアル 2. Python インタープリターの使い方](https://docs.python.org/ja/3/tutorial/interpreter.html)

### 学習のポイント
- Pythonの特徴と利点の理解
- インタープリターの起動方法
- インタラクティブモードの使い方
- スクリプトの実行方法

## 💻 実装したコード

### hello_world.py
```python
# 最初のPythonプログラム
print("Hello, World!")
print("Python 再学習開始！")

# 基本的な計算
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")

# 変数の使用
name = "Python Learner"
print(f"私は {name} です")
```

### 実行結果
```
Hello, World!
Python 再学習開始！
2 + 3 * 4 = 14
私は Python Learner です
```

## 🔍 学んだこと・気付き

### 新しい発見
- Pythonの哲学「Simple is better than complex」を再確認
- インタープリターのインタラクティブモードでの`>>>`プロンプト

### 重要なポイント
- Pythonは読みやすさを重視した言語設計
- インデントによるブロック構造
- 豊富な標準ライブラリ

### つまずいた点・解決方法
- 特になし（基礎的な内容のため）

## 🎯 練習問題

### 問題
1. 自分の名前と年齢を変数に格納し、自己紹介文を表示するプログラムを作成
2. 簡単な四則演算を行い、結果を表示するプログラムを作成

### 解答
```python
# 問題1の解答
name = "山田太郎"
age = 25
print(f"はじめまして、{name}です。{age}歳です。")

# 問題2の解答
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
```

## 📋 次回の学習予定
- Python チュートリアル 3章: Python を電卓として使う
- 数値と文字列の基本的な操作

## 🔗 参考リンク
- [Python公式ドキュメント](https://docs.python.org/ja/3/)
- [Python チュートリアル全体](https://docs.python.org/ja/3/tutorial/)

---
**学習時間**: 30分  
**理解度**: ★★★★★ (5段階評価)
# Python学習環境セットアップガイド

## 🐍 Pythonのインストール

### 1. 公式Pythonのダウンロード
- [Python.org](https://www.python.org/)から最新版をダウンロード
- 推奨バージョン: Python 3.11以上

### 2. バージョン確認
```bash
python --version
python3 --version
```

### 3. pipの確認
```bash
pip --version
pip3 --version
```

## 🛠️ 開発環境の準備

### 推奨エディター/IDE
1. **Visual Studio Code**
   - Python拡張機能をインストール
   - Pylint、Black、autopep8などの拡張機能も推奨

2. **PyCharm Community Edition**
   - 無料で高機能なPython IDE

3. **Jupyter Notebook/Lab**
   - 学習と実験に最適
   ```bash
   pip install jupyter
   jupyter notebook
   ```

### 仮想環境の設定
```bash
# 仮想環境の作成
python -m venv python_learning_env

# 仮想環境のアクティベート
# Windows:
python_learning_env\Scripts\activate
# macOS/Linux:
source python_learning_env/bin/activate

# 仮想環境の確認
which python
```

## 📚 必要なパッケージ

### 基本パッケージ
```bash
pip install --upgrade pip
pip install ipython        # 高機能なPythonシェル
pip install jupyter        # Jupyter Notebook
pip install requests       # HTTP通信
pip install beautifulsoup4 # HTML解析
pip install pandas         # データ分析
pip install matplotlib     # グラフ作成
pip install numpy          # 数値計算
```

### 開発ツール
```bash
pip install black          # コードフォーマッター
pip install pylint         # コード品質チェック
pip install mypy           # 型チェック
pip install pytest         # テストフレームワーク
```

## 🔧 便利な設定

### .pythonrc ファイル（Pythonシェル設定）
```python
# ~/.pythonrc
import os
import sys
import atexit
import readline
import rlcompleter

# タブ補完を有効化
readline.parse_and_bind('tab: complete')

# 履歴ファイルの設定
histfile = os.path.join(os.path.expanduser("~"), ".python_history")
try:
    readline.read_history_file(histfile)
    h_len = readline.get_current_history_length()
except FileNotFoundError:
    open(histfile, 'wb').close()
    h_len = 0

def save(prev_h_len, histfile):
    new_h_len = readline.get_current_history_length()
    readline.set_history_length(1000)
    readline.append_history_file(new_h_len - prev_h_len, histfile)

atexit.register(save, h_len, histfile)

# よく使う関数をインポート
from pprint import pprint as pp
import datetime as dt
import json
import math
import random
import re

print("Python学習環境が準備できました！")
print("便利な関数: pp (pprint), dt (datetime), json, math, random, re")
```

### 環境変数の設定
```bash
# ~/.bashrc または ~/.zshrc に追加
export PYTHONSTARTUP="$HOME/.pythonrc"
export PYTHONPATH="$HOME/Python-Relearning:$PYTHONPATH"
```

## 📂 学習プロジェクトのクローン

```bash
git clone https://github.com/RyoMurakami1983/Python-Relearning.git
cd Python-Relearning
```

## 🚀 学習の開始

1. **Day 1から開始**
   ```bash
   cd days/day001
   python hello_world.py
   ```

2. **進捗の記録**
   - 毎日の学習記録をコミット
   - 学習時間と理解度を記録

3. **定期的な復習**
   - 週末に1週間分の復習
   - 月末に1ヶ月分の総復習

## 🔗 参考リンク

- [Python公式ドキュメント](https://docs.python.org/ja/3/)
- [Python チュートリアル](https://docs.python.org/ja/3/tutorial/)
- [Python標準ライブラリ](https://docs.python.org/ja/3/library/)
- [PEP 8 -- Style Guide for Python Code](https://pep8-ja.readthedocs.io/)

## 🆘 トラブルシューティング

### よくある問題と解決方法

1. **"python is not recognized"エラー**
   - PATHにPythonのインストールディレクトリが追加されているか確認
   - `python3`コマンドを試す

2. **モジュールがインポートできない**
   - 仮想環境がアクティベートされているか確認
   - `pip list`でインストール済みパッケージを確認

3. **日本語の文字化け**
   - ファイルのエンコーディングをUTF-8に設定
   - `# -*- coding: utf-8 -*-`をファイルの先頭に追加

4. **権限エラー**
   - 仮想環境を使用する
   - `pip install --user`オプションを使用

## 📞 サポート

質問や問題があれば以下を参照：
1. Python公式ドキュメント
2. Stack Overflow
3. Python Japan Discord
4. PyQ（有料学習サービス）
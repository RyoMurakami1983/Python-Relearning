#!/usr/bin/env python3
"""
新しい学習日のディレクトリとファイルを作成するユーティリティスクリプト
使用方法: python create_day.py 002 "数値と文字列の操作"
"""

import os
import sys
import shutil
from pathlib import Path

def create_day_structure(day_num, topic):
    """指定された日数のディレクトリ構造を作成する"""
    
    # プロジェクトのルートディレクトリを取得
    script_dir = Path(__file__).parent
    project_root = script_dir.parent.parent
    
    # 日数のフォーマット（例: "002"）
    day_str = f"day{day_num:03d}"
    day_dir = project_root / "days" / day_str
    
    # ディレクトリが既に存在する場合は確認
    if day_dir.exists():
        response = input(f"{day_str}は既に存在します。上書きしますか？ (y/N): ")
        if response.lower() != 'y':
            print("キャンセルしました。")
            return
        shutil.rmtree(day_dir)
    
    # ディレクトリを作成
    day_dir.mkdir(parents=True, exist_ok=True)
    
    # テンプレートファイルの読み込み
    template_path = project_root / "resources" / "templates" / "daily_template.md"
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # テンプレートの置換
    readme_content = template_content.replace("Day XXX", f"Day {day_num:03d}")
    readme_content = readme_content.replace("[学習テーマ]", topic)
    
    # README.mdファイルの作成
    readme_path = day_dir / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    # サンプルPythonファイルの作成
    python_file = day_dir / f"day{day_num:03d}.py"
    python_content = f'''#!/usr/bin/env python3
"""
Day {day_num:03d}: {topic}
"""

print("Day {day_num:03d}: {topic}")
print("=" * 50)

# ここに学習内容のコードを書いてください

if __name__ == "__main__":
    print("学習を開始します！")
'''
    
    with open(python_file, 'w', encoding='utf-8') as f:
        f.write(python_content)
    
    print(f"✅ {day_str}のディレクトリとファイルを作成しました:")
    print(f"   📁 {day_dir}")
    print(f"   📄 {readme_path}")
    print(f"   🐍 {python_file}")
    print(f"\n次のステップ:")
    print(f"   1. cd {day_dir}")
    print(f"   2. README.mdを編集して学習内容を記録")
    print(f"   3. {python_file.name}にコードを実装")

def main():
    if len(sys.argv) != 3:
        print("使用方法: python create_day.py <日数> \"<学習テーマ>\"")
        print("例: python create_day.py 002 \"数値と文字列の操作\"")
        sys.exit(1)
    
    try:
        day_num = int(sys.argv[1])
        if day_num < 1 or day_num > 100:
            raise ValueError("日数は1-100の範囲で指定してください")
    except ValueError as e:
        print(f"エラー: {e}")
        sys.exit(1)
    
    topic = sys.argv[2]
    create_day_structure(day_num, topic)

if __name__ == "__main__":
    main()
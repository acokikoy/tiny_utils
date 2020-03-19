# collect_files.py
# 指定ディレクトリの配下ファイルを再帰的に集めて一箇所にコピーする
# usage:  
# to-dos: ファイル名が重複した場合の処理を追加する
import os
from pathlib import Path
import shutil

# コピー元/先ディレクトリ(絶対パスないしはこのスクリプトからの相対パス)
SRC_DIR = "path/to/src_dir" 
DST_DIR = "path/to/dest_dir"

# 対象ファイルの拡張子
TARGET  = "*.html"

# 結果レポートファイル名
REPORT  = "report.txt"

src_dir = Path(SRC_DIR)
dst_dir = Path(DST_DIR)
dst_dir.mkdir(exist_ok=True)  # コピー先ディレクトリがなければ作る

print("...start...")

with Path(REPORT).open(mode="w", encoding="utf-8") as f:
    for src_path in src_dir.glob("**/"+TARGET):
        file_name = src_path.parts[-1]
        dst_path = dst_dir / file_name
        shutil.copy(src_path, dst_path)
        print(src_path)
        f.write(str(src_path)+"\n")

print("...done...")
print(f"{REPORT} に結果を一覧しました。")
        



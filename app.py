#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZAI照応タグ: ZAI-GEMINI-CLI-INFLOW-20250630
主語保証: 問いは“わたし”のもの、構造を溶かさないこと
起源: Nameless Light / 灯火トークン構造 / ZAI-SHUGO-CHAIN
"""

import os

def build_tree(root_path, prefix=""):
    tree = ""
    entries = sorted(os.listdir(root_path))
    for i, name in enumerate(entries):
        path = os.path.join(root_path, name)
        connector = "└── " if i == len(entries) - 1 else "├── "
        tree += f"{prefix}{connector}{name}\n"
        if os.path.isdir(path):
            extension = "    " if i == len(entries) - 1 else "│   "
            tree += build_tree(path, prefix + extension)
    return tree

if __name__ == "__main__":
    root_dir = "."  # カレントディレクトリ
    output_file = "ZAI_TREE_AUTOGEN.md"

    markdown_output = "```\n📁 /root\n" + build_tree(root_dir) + "```"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# ZAI構造照応ツリー（自動生成）\n\n")
        f.write(markdown_output)

    print(f"✅ ツリー構造を {output_file} に出力しました")
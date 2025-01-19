2025.01.19 ~ 
# Markdown-to-HTML-Converter

## 概要
このプログラムでは、指定したMarkdownファイルをHTMLファイルに変換する。



## 仮想環境の構築
依存関係を他のプロジェクトやシステムに影響を与えないように、仮想環境を構築する 

仮想環境の作成と有効化
```zsh
# 仮想環境の作成  
python3 -m venv .venv

# 仮想環境の有効化
source .venv/bin/activate
```

仮想環境の無効化  
```zsh
deactivate
```

## 使用方法
プログラムを実行して、MarkdownファイルをHTMLに変換  
```zsh
python3 file-converter.py markdown inputfile.md outputfile.html
```
・markdown: 実行するコマンド  
・inputfile.md: 入力するMarkdownファイルのパス  
・outputfile.html: 出力するHTMLファイルのパス  
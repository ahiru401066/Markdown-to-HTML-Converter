import sys
import markdown

def main(args):
    #バリテーション
    if(len(args) != 4):
        print("適切なコマンドが実行されていません。")
        sys.exit(1)
    elif(args[1] != "markdown"):
        print("Unknown that command：" ,args[1])

    #パスの認識
    inputpath = args[2]
    outputpath = args[3]

    #mdファイルの内容の読み込み
    with open(inputpath, encoding='utf-8') as f:
        contents = f.read()

    #md to html と　index.htmlファイルとして出力
    md = markdown.Markdown(extensions=['tables'])
    changedContents = md.convert(contents)
    with open(outputpath, "w") as f:
        f.write(changedContents)

#シェルで　python3 file-converter.py markdown inputfile outputfile
args = sys.argv
main(args)
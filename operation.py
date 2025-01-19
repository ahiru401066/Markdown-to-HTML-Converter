import sys
import markdown

def main(args):
    #バリテーション
    if(len(args) != 4):
        print("適切なコマンドが実行されていません。")
        sys.exit(1)
    elif(args[1] != "markdown"):
        print("Unknown that command：" ,args[1])

    inputpath = args[2]
    outputpath = args[3]

#シェルで　python3 file-converter.py markdown inputfile outputfile
args = sys.argv
main(args)
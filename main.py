from utils.constructeur import obfuscator, construct
import sys
def main():
    try :
        f = open(sys.argv[1] , "r")
        output_file = open(sys.argv[2], "w")
        content = f.read()
        result = f"_=([]!=[[],[]]);__=_+([]==[]);___=__**__-(_==([]==[]));exec(('%c'*({construct(len(content))}))%({obfuscator(content)}))"
        output_file.write(result)
    except:
        print("invalid format!\nenter something like : python3 ./main.py src dest")

main()
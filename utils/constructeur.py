
def construct(n):
    bin = to_bin(n)
    result = []
    for (j,i) in enumerate(bin):
        if i == "1":
            result.append(f"__**({transform_pow(len(bin) - j - 1)})")
    return "+".join(result)
def to_bin(n):
    result = ""
    while n > 0 :
        result = f"{n%2}{result}"
        n//=2
    return result
def transform_pow(n):
    return ["(___**___)*(([]!=[]))",
            "(__*__%___)",
            "(([]==[])+(__*__)-___)",
            "(___**___%(([]==[])+(()==()))+__)",
            "(([]==[])+(__*__)-___)*(___**___%(([]==[])+(()==()))+__)-(([]==[])+(__*__)-___)",
            "((__+([]==[]))*__-_)",
            "(([]==[])+(__*__)-___)**(([]==[])+(__*__)-___)+((__+([]==[]))*__-_)%(___**___%(([]==[])+(()==()))+__)",
            "(([]==[])+(__*__)-___)**(([]==[])+(__*__)-___)+((__+([]==[]))*__-_)%(___**___%(([]==[])+(()==()))+__)+_"
            ][n]
def obfuscator(input):
    result=[]
    for i in input:
        result.append(construct(ord(i)))
    return ",".join(result) 

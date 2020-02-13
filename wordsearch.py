#Imports
import sys, time

#Classes
class dict:
    colordict = {"c":"0","r":"31","g":"32","y":"33","b":"34","m":"35","c":"36","w":"37"}
    matrix = []
    matches = []
    helpdict = {
        "main":"CLI List:\n  [h]elp <page>: display help page\n  [v]erbose: enable verbose logging",
    }

#Global Variables
v = 0
word = ""

#Test Vars
class test:
    lines = ["ysjzdesdikdzj","lrcanuxddnyqa","qwvadxrnakhlp","dxyaenalassba","nunytlrvaxean","gdkeieomdqvpm","mtbzzdagqkiee","riatlhkjmtdlx","twioaitiahlii","swmbpanamaahc","saleuzenevmco"]
    findlist = ["bahamas","chile","japan","maldives","guyane","haiti","mexico","moldova","pananma"]

#Functions
def count(x,c=0):
    for y in x:
        c += 1
    return c

def listhelp(x="main"):
    if (x in dict.helpdict):
        print(dict.helpdict[x])
    else:
        print('Unknown help page')
    quit()
    return

def color(x,y):
    if (x in dict.colordict):
        return f'\033[{dict.colordict[x]}m{y}\033[0m'
    else:
        return f'color not found: {x}'

def verbose(x=0,y="\n"):
    if (v > 0):
        print(x,end=y,flush=True)
    return

def clitest():
    if ((arglen := len(sys.argv)) > 1):
        for x in range(1,arglen):
            y = sys.argv[x]
            if (y in ["h","help"]):
                try:
                    listhelp(sys.argv[x + 1])
                except:
                    listhelp()
            elif (y in ["v","verbose"]):
                global v
                v = 1
            elif (y in ["w","word"]):
                global word
                verbose(sys.argv[x + 1])
                word = str(sys.argv[x + 1])
                return
            else:
                print(f'Unrecognised argument: {y}')
                listhelp()
    return

def linestomatrixdict(x):
    c,r = len(test.lines),count(test.lines[0])
    verbose(color("g",f'Grid is a {c}x{r}'))

    verbose(color("g",f'Lines to be converted are:'))
    for x in test.lines:
        verbose(f'\t|{x}|')
    
    verbose(color("c","\nStarting conversion"))

    for x in test.lines:
        verbose("\t|","")
        tmplist = []
        for y in x:
            tmplist.append(y)
            verbose(y,"")
        dict.matrix.append(tmplist)
        verbose("|")
    
    verbose(color("c","\nConversion Completed"))
    return

def printmatrix(x,f):
    rcoord = 0
    col = 0
    for r in dict.matrix:
        ccoord = 0
        verbose("\t|","")
        for c in r:
            for y in x:
                if ([rcoord,ccoord] == y):
                    col = 1
                    break
                else:
                    col = 0
            if col == 1:
                verbose(color(f,f'{c}'.upper()),"")
            else:
                verbose(f'{c}'.upper(),"")
            ccoord += 1
        verbose("|")
        rcoord += 1

def lookaround(tmp,x):
    rx = range(-1,2)
    i = tmp[-1]

    for y in rx:
        for z in rx:
            try:
                coord = [abs((z + i[0])),abs((y + i[1]))]
            finally:
                try:
                    if ((dict.matrix[coord[0]][coord[1]]) == (x)):
                        tmp.append(coord)
                except:
                    continue
    dict.matches.append(tmp)
    return tmp

def findword(x):
    verbose(color("m","\nStarting Search"))

    tmplist = []
    iterr = 0
    tmp = []

    for y in x:
        tmplist.append(y)
    verbose(f'\tword is: {x}\n\t{tmplist}\n')

    for c in dict.matrix:
        iterc = 0
        for b in c:
            if (tmplist[0] == b):
                tmp = [[iterr,iterc]]
                verbose(f'\tFound "{b}" on {tmp[0]}')
                for x in tmplist:
                    if (not lookaround(tmp,x)):
                        break
                        
                printmatrix(tmp,"c")
            iterc += 1
        iterr += 1

    c = 0
    copy = []
    for x in dict.matches:
        var = len(x)
        if var > c:
            c = var
            copy = x
            continue
    verbose(color("g",'\n\nLikely Result'))
    printmatrix(copy,"g")
    


def main():
    #Pre Main
    clitest()
    #Start Main
    verbose(color("r","Start Main\n"))

    linestomatrixdict(test.lines)

    findword(word)

    #End Main
    verbose(color("r","\nEnd Main"))
    return

if __name__ == "__main__":
    main()
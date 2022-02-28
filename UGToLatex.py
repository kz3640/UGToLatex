import constants

def main():
    print("Hello World!")
    with open('Perfect-Ed-Sheeran.raw', 'r') as f:
        lines = f.readlines()
    f.close()

    defn = []
    for line in lines:
        defn.append(whatIsThis(line))

    for x in range(len(defn)):
        print(defn[x])
        if defn[x] == 2:
            print(chordify(lines[x]))

def whatIsThis(line):
    #-1: unknown
    # 0: empty line
    # 1: verse header
    # 2: chords
    # 3: lyrics
    if line[0:1] == "[": #like in [verse 1], [chorus], etc
        return 1
    if line.count(' ') >= len(line)-1:
        return 0
    if line.count(' ') > len(line)/3:
        return 2
    return 3

def chordify(raw):
    returnMe = constants.SC
    for x in raw:
        if x == '#':
            returnMe = returnMe + constants.SHARP
        elif x == 'b':
            returnMe = returnMe + constants.FLAT
        elif x != '\n':
            returnMe = returnMe + x
    returnMe = returnMe + constants.EC
    return returnMe

def combine(rawL, rawC):
    returnMe = ""
    
    

if __name__ == "__main__":
    main()

import constants
import sys

def main(name, inp, out):
    lines = []
    w = open(out, "a")
    w.write(constants.HEADER)
    with open(inp) as f:
        for l in f:
            lines.append(l)
    lines = rmJunk(lines)
    i = 0
    while i != len(lines):
        if whatIsThis(lines[i]) == 2:
            if (i != len(lines)-1):
                if whatIsThis(lines[i+1] == 3)
                    print(combine(lines[i] , lines[i+1]))
                    w.write(combine(lines[i], lines[i+1]))
                    w.write("\n")
        i+=1
    w.write(constants.FOOTER)
    return

def rmJunk(lines):
    returnMe = []
    check = ["|", "---"]
    i = 0
    while i != len(lines):
        if any(ext in lines[i] for ext in check):
            print("removed line " + str(i) + ".")
        else:
            returnMe.append(lines[i])
        i+=1
    return returnMe

def combine(chords, lyrics):
    combined = lyrics
    chords = chords + ' '
    i = len(chords)
    while i != 0:
        if chords[i-1:i] == 'b':
            chords = chords[0:i-1] + constants.FLAT + chords[i:]
        if chords[i-1:i] == '\#':
            chords = chords[0:i-1] + constants.SHARP + chords[i:]
        if (chords[i-1:i] == 'A' or
            chords[i-1:i] == 'B' or
            chords[i-1:i] == 'C' or
            chords[i-1:i] == 'D' or
            chords[i-1:i] == 'E' or
            chords[i-1:i] == 'F' or
            chords[i-1:i] == 'G'):
            j = chords.index(' ', i)
            combined = lyrics[0:i-1] + "\\[" + chords[i-1:j] + "]" + lyrics[i-1:]
        i-=1
    return combined

def whatIsThis(line):
    #-1: unknown
    # 0: empty line
    # 1: verse header
    # 2: chords
    # 3: lyrics
    if line[0:1] == "[": #like in [verse 1], [chorus], etc
        return 1
    if line.count(' ') == len(line): #empty line
        return 0
    if line.count(' ') > len(line)/3: #space ocurrs more than 1 in 3 chars
        return 2
    if len(line) < 4:  #only 1/2/3 char on a line (lone chord)
        return 2
    return 3

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])

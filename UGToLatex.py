import constants
import sys

def main(name, inp, out):
    """
    The main method

    name    The name of the song
    inp     The name of the text file containing the song
    out     The name of the text file to output the song
    """

    writer = open(out, "a")         #the writer to the output
    reader = open(inp)              #the reader to the input
    lines = []                      #the array of lines in the input

    writer.write(constants.HEADER)  #write the tex file header

    for line in reader:
        lines.append(line)          #place all lines in a list

    lines = rmJunk(lines)           #remove junk lines

    i = 0                           #loop counter
    while i != len(lines):          #loop through all lines
        if (whatIsThis(lines[i]) == 2 and
        i != len(lines) -1 and  
        whatIsThis(lines[i+1] == 3)):
        #this code runs if the current line is chords, and the next line
        #is lyrics
            writer.write(combine(lines[i], lines[i+1]))
            writer.write("\n")
            i+=1                    #advance loop an extra time
        i+=1                        #advance loop
    writer.write(constants.FOOTER)  #write the tex file footer
    return

def rmJunk(lines):
    """
    Removes unneeded lines
    lines   The lines to search through
    """

    returnMe = []                   #the cleaned lines
    check = ["|", "---"]            #what to look for in an unneeded line
    i = 0                           #loop counter

    while i != len(lines):          #loop through all lines
        if any(ext in lines[i] for ext in check):
            print("removed line " + str(i) + ".")
        else:
            returnMe.append(lines[i])
        i+=1                        #advance loop
    return returnMe

def combine(chords, lyrics):
    """
    Combines chords and lyrics
    chords  The chords to be combined
    lyrics  The lyrics to be combined
    """

    combined = lyrics               #set the eventual return to lyrics
    chords = chords + ' '           #add a space to the end of chords
                                    #to search for eventually

    s = "\\["                       #enclose chord in tex
    e = "]"

    i = len(chords)                 #loop counter
    while i != 0:                   #loop thorugh all indexes, backwards
        if chords[i-1:i] == 'b':    #change flats
            chords = chords[0:i-1] + constants.FLAT + chords[i:]
        elif chords[i-1:i] == '\#': #change sharps
            chords = chords[0:i-1] + constants.SHARP + chords[i:]
        elif (chords[i-1:i] == 'A' or
              chords[i-1:i] == 'B' or
              chords[i-1:i] == 'C' or
              chords[i-1:i] == 'D' or
              chords[i-1:i] == 'E' or
              chords[i-1:i] == 'F' or
              chords[i-1:i] == 'G'):

            j = chords.index(' ', i)#look for the first occurrence of
                                    #a space after the chord
            combined = lyrics[0:i-1] + s + chords[i-1:j] + e + lyrics[i-1:]
        i-=1
    return combined

def whatIsThis(line):
    """
    Tells whether a line is a chord, lyrics, verse header, or blank.
    line    The line to look at
    """
    #-1: unknown
    # 0: empty line
    # 1: verse header
    # 2: chords
    # 3: lyrics
    if line[0:1] == "[":            #like in [verse 1], [chorus], etc
        return 1
    if line.count(' ') == len(line):#empty line
        return 0
    if line.count(' ') > len(line)/3:
        return 2
    if len(line) < 4:               #only 1/2/3 char on a line
        return 2
    if line.count('a') +
       line.count('e') +
       line.count('i') +
       line.count('o') +
       line.count('u') == 0:        #no vowels
        return 2                    
    return 3

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])

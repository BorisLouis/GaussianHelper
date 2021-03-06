import os

def getFileList(path,ext):
    dirList = os.listdir(path)
    fileList = []
    for file in dirList:
        if ext in file:
            fileList.append(file)

    return fileList


def readFile(path):
    file2Read = open(path,'r')

    calcLine = []
    coordLine = []

    for line in file2Read:

        if '#' in line:
            calcLine.append(line)
        if line[0] == 'C':
            coordLine.append(line)
            for l in file2Read:
                coordLine.append(l)


    file2Read.close()
    return coordLine

def readLogFile(path):
    file2Read = open(path, 'r')
    allLine = file2Read.readlines()
    file2Read.close()
    idx =[]
    counter = 0
    for line in allLine:
        counter = counter +1
        if 'Standard orientation' in line:
            idx.append(counter)

    idx2Read = idx[-1]
    coordLine = []
    while True:
        #read line from the last standard orientation
        line = allLine[idx2Read]
        test = line.lstrip()
        if len(test)!=0:
            if test[0].isnumeric():
                ln = line
                while test[0].isnumeric():
                    l2Write = getCoordLine(ln)
                    coordLine.append(l2Write)
                    idx2Read = idx2Read + 1
                    ln = allLine[idx2Read]
                    test = ln.lstrip()

                break
        # index lines to next line
        idx2Read = idx2Read + 1
    return coordLine



def getCoordLine(line):

    # get line to write from log line
    splitLine = line.split()
    atomNumber = splitLine[1]
    atom = getAtomFromNumber(atomNumber)
    X = splitLine[3]
    X = formatNumber(X)
    Y = splitLine[4]
    Y = formatNumber(Y)
    Z = splitLine[5]
    Z = formatNumber(Z)

    l2Write = atom + '        ' + X + '      ' + Y + '      ' + Z + '\n'
    return l2Write

def makeInputFile(path,cLine,calcLine,comment,charge, coordLine,optRedundant,freeze,name='READY'):

    folder,file = os.path.split(path)
    file,ext = os.path.splitext(file)
    path2Use = folder + '/' + file + name +'.com'

    f = open(path2Use,'w')
    #add computer related command
    for line in cLine:
        f.write(line)
    f.write('\n')

    #add calculation related Line
    for line in calcLine:
        f.write(line)

    f.write('\n')
    f.write(comment)
    f.write('\n')

    f.write(charge)

    if len(freeze)!=0:
        freeze = getFreeze(freeze)
    #add atom coordinates Line
    atomNumber = dict()
    for line in coordLine:
        if len(freeze)==0:
            f.write(line)
        else:
            #count atoms
            key = line[0]
            if key in atomNumber.keys():
                atomNumber[key] = atomNumber[key]+1
            else:
                atomNumber[key] = 1
            l2Write = applyFreeze(line,freeze,atomNumber)
            f.write(l2Write)

    #add opt redundant
    if len(optRedundant)!=0:
        optRedundantLines = getOptRedundant(optRedundant, coordLine)
        for line in optRedundantLines:
            f.write(line)
            f.write('\n')

    f.write('\n')

    f.close()

def getOptRedundant(optRedundant,coordLine):
    wrapLine = optRedundant.pop(0)
    wrapLine = wrapLine.split()
    optRedLine = []
    for line in optRedundant:
        newStr = wrapLine[0]
        currLine = line.split()

        if isNumber(currLine[-1]):
            fixedCoord = currLine.pop()
        else:
            fixedCoord = ''

        for elem in currLine:
            atomNumber = getAtomNumber(elem,coordLine)
            newStr = newStr + ' ' + str(atomNumber)
        if wrapLine[1] == 'B':
            angStr = newStr+ ' ='+fixedCoord + ' ' + wrapLine[1]
            newStr = newStr + ' '+ wrapLine[2]
        else:
            newStr = newStr + ' ' + wrapLine[1]

        optRedLine.append(angStr)
        optRedLine.append(newStr)

    return optRedLine

def getAtomNumber(atomCoord,coordLine):
    counter = 0
    atomCounter = 0

    atom = atomCoord[0]
    atomN = atomCoord[1:]

    for line in coordLine:
        counter = counter +1
        if atom in line:
            atomCounter = atomCounter+1

        if atomCounter == int(atomN):
            return counter

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getFreeze(freeze):
    frz = dict()
    #Depending on the presence of "!" or absence in first position, we define the default action to be freezing or not
    #freezing. Hence the exclamation mark allow to freeze everything except the atoms on the list.
    if freeze[0] == '!':
        frz['default'] = '-1'
        frz['action']  = ' 0'
        freeze = freeze[1:]
    else:
        frz['action'] = '-1'
        frz['default'] = ' 0'

    splitFreeze = freeze.split()
    #we initialize with a random label, trying to find label that correspond to atoms
    currentLabel = 'buggy'
    for elem in splitFreeze:
        #check if it is a numeric
        if elem.isnumeric():
            if currentLabel in frz.keys():
                tmpList = []
                #make a new list with the old element
                for el in frz[currentLabel]:
                    tmpList.append(el)
                #add the new element
                tmpList.append(elem)
                #add to the dictionary
                frz[currentLabel] = tmpList
            else:
                #create dict entry
                frz[currentLabel] = [elem]
        else:
            currentLabel = elem

    return frz

def applyFreeze(line,freeze,atomNumber):
    #check if the element on the line is present in the dict
    if line[0] in freeze.keys():

        if str(atomNumber[line[0]]) in freeze[line[0]]:
            newLine = line[0:2] + freeze['action'] + line[2:]
        else:
            newLine = line[0:2] + freeze['default'] + line[2:]

    else:
        newLine = line[0:2] + freeze['default'] + line[2:]

    return newLine

def formatNumber(number):

    idx = number.find('.')
    nAfter = len(number)-idx-1

    if idx==1:
        number = '  ' + number

    if idx ==2:
        number = ' '  + number

    if nAfter == 6:
        number = number[:-1]

    if nAfter == 7 :
        number = number[:-2]

    return number


def getAtomFromNumber(number):

    if number == '6':
        return 'C'
    elif number == '1':
        return 'H'
    elif number == '8':
        return 'O'
    elif number == '7':
        return 'N'
    elif number == '16':
        return 'S'
    else:
        return NotImplementedError
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

        if '#n' in line:
            calcLine.append(line)

        else:
            if line[0]!='%':
                coordLine.append(line)

    file2Read.close()
    return coordLine

def makeInputFile(path,cLine,calcLine,coordLine,optRedundant):

    f = open(path,'w')
    #add computer related command
    for line in cLine:
        f.write(line)
    f.write('\n')

    #add calculation related Line
    for line in calcLine:
        f.write(line)

    #add atom coordinates Line
    for line in coordLine:
        f.write(line)
    f.write('\n')

    #add opt redundant
    for line in optRedundant:
        f.write(line)
    f.close()



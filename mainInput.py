import os
import input

path = 'D:/Documents/Unif/PhD/2021-Data/Quantum Calculations/2021/04 - April/21/03 - Pentamer/Spectra/'
fileExt = '.log'
optRedundant = []
#optRedundant.append('D F')
#optRedundant.append('C5 C6 C7 S1 -0.9')
#optRedundant.append('S1 C10 C11 C46 30.6')
#optRedundant.append('C45 C44 C47 S2 14.9')
#optRedundant.append('S2 C50 C51 C82 15.9')
#optRedundant.append('C84 C85 C87 S3 25.7')
#optRedundant.append('N1 C12 C14 C18 -37.4')
#optRedundant.append('N2 C13 C15 C20 -45.2')
#optRedundant.append('N3 C52 C54 C56 35.2')
#optRedundant.append('N4 C53 C60 C61 38.4')
#optRedundant.append('N5 C91 C94 C98 37.3')
#ptRedundant.append('N6 C91 C93 C95 38.7')


calcLine = '#n TD=(NStates=10) B3LYP/6-31G(d)\n'
charge   = '0 1\n'
comment = 'Tetramer Spectra\n'
freeze = ''

#STANDARD GEOMETRY OPTIMIZATION
#'#n B3LYP/6-31G(d) Opt\n'
#'#n PM3 Opt\n'
#SPECTRA
#TD=(NStates=10) B3LYP/6-31G(d)

# get file in the directory
fileList = input.getFileList(path,fileExt)

#loop through file and do the desired modification
for file in fileList:
    fileName = os.path.splitext(file)
    currentPath = path+file

    cLine = []
    cLine.append('%mem=40000MB\n')
    cLine.append('%nprocshared=20\n')
    cLine.append('%chk=' + fileName[0] + '.chk\n')

    if fileExt == '.com':
        #read file and extract coordinate
        coordLine = input.readFile(currentPath)
    elif fileExt == '.log':
        coordLine = input.readLogFile(currentPath)
    else:
        raise Exception('Something went wrong')

    #Make Input file according to input
    input.makeInputFile(currentPath,cLine,calcLine,comment,charge,coordLine,optRedundant,freeze)



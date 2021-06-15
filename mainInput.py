import os
import input

path = 'D:/Documents/Unif/PhD/2021-Data/Quantum Calculations/2021/06 - June/14 - PM3 & basis set test/test Code'
fileExt = '.com'
optRedundant = []
optRedundant.append('D B F')
optRedundant.append('C5 C6 C7 S1 -0.9')
optRedundant.append('S1 C10 C11 C46 30.6')
#optRedundant.append('C45 C44 C47 S2 14.9')
#optRedundant.append('S2 C50 C51 C82 15.9')
#optRedundant.append('C84 C85 C87 S3 25.7')
#optRedundant.append('S3 C90 C91 C122 16.2')
#optRedundant.append('C125 C126 C127 S4 22.3')
#optRedundant.append('S4 C160 C161 C164 14.5')
#optRedundant.append('C165 C166 C167 S5 24.2')

#optRedundant.append('N1 C12 C14 C18 -37.4')
#optRedundant.append('N2 C13 C15 C20 -45.2')
#optRedundant.append('N3 C52 C54 C56 35.2')
#optRedundant.append('N4 C53 C60 C61 38.4')
#optRedundant.append('N5 C91 C94 C98 37.3')
#optRedundant.append('N6 C92 C93 C95 38.7')


calcLine = '#n PM3 Opt=ModRedundant\n'
charge   = '0 1\n'
comment = 'Tetramer PM3 optimization with dihedral freezing\n'
freeze = ''

#STANDARD GEOMETRY OPTIMIZATION
#'#n B3LYP/6-31G(d) Opt\n'
#'#n B3LYP/6-31G(d) Opt=ModRedundant\n'
#'#n PM3 Opt=ModRedundant\n'
#SPECTRA
#TD=(NStates=10) B3LYP/6-31G(d)

# test if path is complete or not, add '/' if needed
if path[-1:] != '/':
    path = path + '/'

# get file in the directory
fileList = input.getFileList(path,fileExt)

#loop through file and do the desired modification
for file in fileList:
    fileName = os.path.splitext(file)
    currentPath = path+file

    cLine = []
    cLine.append('%mem=80000MB\n')
    cLine.append('%nprocshared=10\n')
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



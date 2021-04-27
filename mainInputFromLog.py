import os
import input

path = 'D:/Documents/Unif/PhD/2021-Data/Quantum Calculations/2021/04 - April/21/01 - Trimer/Test1/'
fileExt = '.log'
optRedundant = []
optRedundant.append('C5 C6 C7 S1 -0.9')
optRedundant.append('S1 C10 C11 C46 30.6')
optRedundant.append('C45 C44 C47 S2 14.9')
optRedundant.append('S2 C50 C51 C82 15.9')
optRedundant.append('C84 C85 C87 S3 25.7')

calcLine = '#n TD=(NStates=10) B3LYP/6-31G(d)\n'
charge   = '0 1\n'
comment = 'Trimer After reoptimization for short chain\n'

#STANDARD GEOMETRY OPTIMIZATION
#'#n B3LYP/6-31G(d) Opt\n'
#'#n PM3 Opt\n'

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

    #read file and extract coordinate
    coordLine = input.readLogFile(currentPath)

    input.makeInputFromLog(currentPath,cLine,calcLine,comment, charge,coordLine,optRedundant)

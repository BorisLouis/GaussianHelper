import os
import input

path = 'D:\Documents/Unif/PhD/2021-Data/Quantum Calculations/2021/03 - March/23 - TQ1TrimerSpectra/TrimerLongShortNoReopt/'
fileExt = '.log'
optRedundant = []
calcLine = '#n TD=(NStates=10) B3LYP/6-31G(d)\n'
charge   = '0 1\n'
comment = 'test input from log\n'

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

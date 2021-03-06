import os
import input

path = 'D:/Documents/Unif/PhD/2021-Data/Quantum Calculations/2021/08 - August/Scaling even more up/02 - Decamer/Spectra'
fileExt = '.log'
optRedundant = []
#optRedundant.append('D B F')
#optRedundant.append('C5 C6 C7 S1 0.9')
#optRedundant.append('S1 C10 C11 C46 30.4')
#optRedundant.append('C45 C44 C47 S2 15.3')
#optRedundant.append('S2 C50 C51 C82 13.9')
#optRedundant.append('C84 C85 C87 S3 25.8')
#optRedundant.append('S3 C90 C91 C122 16.2')
#optRedundant.append('C125 C126 C127 S4 22.3')
#optRedundant.append('S4 C160 C161 C164 14.5')
#optRedundant.append('C165 C166 C167 S5 24.2')
#optRedundant.append('S5 C200 C201 C205 15.8')
#optRedundant.append('C206 C204 C207 S6 23.5')
#optRedundant.append('S6 C234 C235 C237 15.5')
#optRedundant.append('C238 C240 C241 S7 23.5')
#optRedundant.append('S7 C274 C275 C284 14.7')
#optRedundant.append('C286 C285 C287 S8 22.8')
#optRedundant.append('S8 C320 C321 C322 15.1')
#optRedundant.append('C323 C325 C327 S9 21.5')
#optRedundant.append('S9 C360 C361 C362 15.7')
#optRedundant.append('C365 C366 C367 S10 23.2')

calcLine = '#n TD=(NStates=10) B3LYP/LanL2DZ\n'
charge   = '0 1\n'
comment = 'Decamer Spectra\n'
freeze = []#'! H 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68'
#PM3 Opt=ModRedundant SCRF=(Solvent=o-DiChloroBenzene)
#STANDARD GEOMETRY OPTIMIZATION
#'#n B3LYP/6-31G(d) Opt\n'
#'#n B3LYP/6-31G(d) Opt=ModRedundant\n'
#'#n PM3 Opt=ModRedundant\n'
#SPECTRA
#TD=(NStates=10) B3LYP/6-31G(d)
##n TD=(NStates=10) B3LYP/LanL2DZ\n

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



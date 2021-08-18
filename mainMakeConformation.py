import os
import random

import input

path = 'D:/Documents/Unif/PhD/2021-Data/Quantum Calculations/2021/08 - August/03 - Different Conformation/01 - Conformation Generation test'
fileExt = '.log'
method  = 'random'
nConformation = 5

#give the list of dihedrals to be done
dhToMod = []
dhToMod.append('D B F')
dhToMod.append('C5 C6 C7 S1')
dhToMod.append('S1 C10 C11 C46')
dhToMod.append('C45 C44 C47 S2')
dhToMod.append('S2 C50 C51 C82')
dhToMod.append('C84 C85 C87 S3')
dhToMod.append('S3 C90 C91 C122')
dhToMod.append('C125 C126 C127 S4')
dhToMod.append('S4 C160 C161 C164')
dhToMod.append('C165 C166 C167 S5')
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

calcLine = '#n PM3 Opt=ModRedundant\n\n'
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


def makeConformation(dh2Mod, method):

    optModRedundant = []
    optModRedundant.append(dh2Mod[0])
    #we skip first element
    for i in range(1,len(dh2Mod)):
        if method == 'random':
            #generate random angle
            genAngle = random.randrange(start=-180,stop=180)

        optModRedundant.append(dh2Mod[i] + ' ' + str(genAngle))

    return optModRedundant


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

    for i in range(0,nConformation):
        #Generate conformation
        optModRedundant = makeConformation(dhToMod, method)

        name = 'conformation0' + str(i)

        #Make Input file according to input
        input.makeInputFile(currentPath, cLine, calcLine, comment, charge, coordLine, optModRedundant, freeze, name)













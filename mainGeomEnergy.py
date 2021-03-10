import os
import output
import input

path = 'D:/Documents/Unif/PhD/2021-Data/Quantum Calculations/2021/03 - March/09 - TQ1/3 - Trimer/Opt/'
fileExt = '.log'

# get file in the directory
fileList = input.getFileList(path,fileExt)

#loop through file and do the desired modification
for file in fileList:
    fileName = os.path.splitext(file)
    currentPath = path+file

    totE,totEkj = output.getSingleOptEnergy(currentPath)

    print(fileName[0] + ' gave an energy of ' +  str(totE) + ' hartrees or ' + str(totEkj) + ' kj/mol' )

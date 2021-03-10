import os
import output
import input


path = 'D:/Documents/Unif/PhD/2021-Data/Quantum Calculations/2021/03 - March/09 - TQ1/1 - Full TD/Spectra/'
fileExt = '.log'
sigma   = 20 #nm

# get file in the directory
fileList = input.getFileList(path,fileExt)

#loop through file and do the desired modification
for file in fileList:
    fileName = os.path.splitext(file)
    currentPath = path+file

    currentSpectra = output.getSpectra(currentPath)
    currentSpectra['path'] = currentPath
    output.makeSpectra(currentSpectra,sigma)

import os
import output
import input
import matplotlib.pyplot as plt

path = 'D:/Documents/Unif/PhD/2021-Data/Quantum Calculations/2021/06 - June/21 - Scaling up And solvent/Results'
fileExt = '.log'
sigma   = 20 #nm
legend = ['Trimer','TrimerThio','Pentamer','PentamerThio','Octramer','OctamerThio',]
# test if path is complete or not, add '/' if needed
if path[-1:] != '/':
    path = path + '/'

# get file in the directory
fileList = input.getFileList(path,fileExt)

#loop through file and do the desired modification
WLAxes = []
WLIntensities = []

for file in fileList:
    fileName = os.path.splitext(file)
    currentPath = path+file

    currentSpectra = output.getSpectra(currentPath)
    currentSpectra['path'] = currentPath
    WLAxis,WLIntensity = output.makeSpectra(currentSpectra,sigma)

    WLAxes.append(WLAxis)
    WLIntensities.append(WLIntensity)


for i in range(0,len(WLAxes)):

    currentWLAxis = WLAxes[i]
    currentIAxis  = WLIntensities[i]

    fig = plt.figure(1)
    plt.plot(currentWLAxis, currentIAxis)
    plt.xlabel('Wavelength')
    plt.ylabel('Intensity')

plt.legend(legend)

fileName = path + '/'  + 'compWL' + '.svg'

plt.savefig(fileName)
plt.close(fig)






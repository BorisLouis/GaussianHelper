import os
import fitting
import numpy as np
import matplotlib.pyplot as plt

def getSingleOptEnergy(path):
    file2Read = open(path, 'r')

    data = []
    # get all line containing energy
    for line in file2Read:
        if 'E(' in line:
            data.append(line)
    file2Read.close()
    # parse the last line containing energy to extract the number
    lastLine = data[-1]

    idx1 = lastLine.find(') =')
    idx2 = lastLine.find('A.U.')

    energyStr = lastLine[idx1+3:idx2]
    energyVal = float(energyStr)

    # convert hartree to kj/mol
    finalEnergy = energyVal*2625.5

    return energyVal, finalEnergy


def getSpectra(path):
    file2Read = open(path, 'r')
    Spectra = dict()

    wL = []
    E  = []
    Amp = []
    for line in file2Read:
        if ' nm ' in line:

            idx1 = line.find('-A')
            idx2 = line.find('eV')
            idx3 = line.find('nm')
            idx4 = line.find('f=')
            idx5 = line.find('<')

            energy = float(line[idx1+2:idx2])
            wavelength = float(line[idx2+2:idx3])
            relAmp = float(line[idx4+2:idx5])

            wL.append(wavelength)
            E.append(energy)
            Amp.append(relAmp)

    Spectra['Wavelength'] = wL
    Spectra['eV'] = E
    Spectra['Amp'] = Amp

    return Spectra


def makeSpectra(Spectra,sigma):

    Wavelength = Spectra['Wavelength']
    eV = Spectra['eV']
    Amp = Spectra['Amp']
    #get the range of value in the spectra
    WLRange = (min(Wavelength),max(Wavelength))
    eVRange = (min(eV),max(eV))
    #normalize amplitude
    newAmp = []
    for val in Amp:
        newAmp.append(val/max(Amp))

    #create wavelength and energy axis based on the range
    WLAxis = np.arange(round(WLRange[0])-3*sigma,round(WLRange[1])+3*sigma,1)
    sigmaEV1 = convertSigma2EV(sigma,eVRange[0])
    sigmaEV2 = convertSigma2EV(sigma,eVRange[1])
    eVAxis = np.arange(eVRange[0],eVRange[1],0.01)

    #Pre-allocate intensity array
    WLIntensity = np.zeros(WLAxis.shape)
    evIntensity = np.zeros(eVAxis.shape)

    #Loop through the state to generate a gaussian based on the input
    for i in range(0,len(Wavelength)):
        currentWL = Wavelength[i]
        currenteV = eV[i]
        currentAmp = Amp[i]

        sigmaeV = convertSigma2EV(sigma,currentWL)
        tmpWLGauss = fitting.Gauss1D(WLAxis,currentWL,currentAmp,sigma)
        tmpWLeVGauss = fitting.Gauss1D(eVAxis,currenteV,currentAmp,sigmaeV)

        WLIntensity = WLIntensity + tmpWLGauss
        evIntensity = evIntensity + tmpWLeVGauss

    print(Wavelength[Amp == max(Amp)])

    path = Spectra["path"]
    folder,file = os.path.split(path)
    file,ext = os.path.splitext(file)

    fig = plt.figure(1)
    plt.plot(WLAxis,WLIntensity)
    plt.bar(Spectra['Wavelength'],Spectra['Amp'])
    plt.xlabel('Wavelength')
    plt.ylabel('Intensity')
    fileName = folder+ '/' + file + 'WL'+ '.svg'
    plt.savefig(fileName)
    plt.close(fig)

    fig = plt.figure(2)
    plt.plot(eVAxis,evIntensity)
    plt.bar(Spectra['eV'], Spectra['Amp'])
    plt.xlabel('eV')
    plt.ylabel('Intensity')
    fileName = folder+ '/' + file + 'eV'+'.svg'
    plt.savefig(fileName)
    plt.close(fig)

    return WLAxis,WLIntensity




def convertSigma2EV(sigma,currentWL):
    c = 299792458

    fStart = c/(currentWL+sigma/2)/10**(-9)
    fStop  = c/(currentWL-sigma/2)/10**(-9)

    Df = abs(fStart-fStop)

    sigmaEV = Df/241799050402417

    return sigmaEV




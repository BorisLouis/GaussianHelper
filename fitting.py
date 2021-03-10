import numpy as np

def Gauss1D(x, mu, Amp, sigma):

    gauss = Amp * np.exp(-((x-mu)**2 / (2*sigma**2)))

    return gauss
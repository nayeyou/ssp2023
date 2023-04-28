import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import librosa

def getFIRFFT(H, order, winname=None):
    NFFT = (len(H)-1)*2
    H2 = np.concatenate((H, H[::-1])) + np.zeros(2*len(H))*(1j)
    # print(H2.shape)
    time_H2 = np.fft.ifft(H2, NFFT)
    order = min(NFFT, order)
    time_H2 = np.concatenate((time_H2[(len(time_H2)-order//2):], time_H2[0:order//2+1]))
    if winname != None:
        win = librosa.filters.get_window(winname, order+1, fftbins=False)
        time_H2 = time_H2*win
    return time_H2.real

y = getFIRFFT(H=np.arange(20), order=10, winname='hamming')
plt.figure()
plt.plot(y)
#
# getFIRFFT(H=np.arange(10))

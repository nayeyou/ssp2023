import sys
import numpy as np
import matplotlib
import librosa
from matplotlib import pyplot as plt
import librosa.display

#from scipy.io import wavfile
import scipy
from scipy import signal

from scipy.fft import fftshift
Ts = 0.01   # 10 ms shift size
Tf = 0.02   # 20 ms frame size
cmap_plot = plt.cm.bone_r # default colormap for spectrogram, gray, reversed

# 오디오 파일 부르고 자르기
wavefile = 'D:/YYN/audio_/digitrec_ye/segmented/YouYeNa/3/kdigits0-3.wav'
x , sr = librosa.load(wavefile , sr=16000)
for i in range(0,100):
    globals()['x_'+str(i)] = x[int(16*i) : int((16*i)+16)] # 10ms
# print(x_10,x_10.shape)

# hamming LPF 생성
for i in range(0,100):
    a = signal.firwin(51, ((i+1)*0.005), window='hamming')
    globals()['y_filter_'+str(i)] = signal.lfilter(a, [1.0], eval('x_'+str(i)))


for i in range(0,99):
    for
    y = np.hstack((('y_filter_'+str(i)),('y_filter_'+str(i+1))))


# # window 적용
#  for i in range(0,100):
#      globals()['y_'+str(i)] = eval('y_filter_'+str(i))
# plt.plot(x1)



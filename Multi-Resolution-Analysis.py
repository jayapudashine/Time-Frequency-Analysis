import numpy as np
from scipy.fftpack import rfft, irfft, fftfreq
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# Session Seven / Spectrograms and Gabor Transforms

T = 10      # Time domain
n = 2048    # Sampling

t = np.linspace(0, T, n+1)
time = t[:n]
#t = t2[:n]
# Actual frequency component   Cos0T , Cos1T, Cos2T ...
#freq = [(2 * np.pi / T) * ii for jj in (np.arange(0,n/2), np.arange(-n/2, 0)) for ii in jj]
signal = (3*np.sin(2*time) + 0.5*np.tanh(0.5*(time-3)) + 0.2*np.exp(-(time-4)**2) + 1.5*np.sin(5*time) \
          + 4*np.cos(3*(time-6)**2)) / 10 + (time/20)**3
freq = np.fft.fftfreq(signal.size, d=time[1]-time[0])
fourier = np.fft.fft(signal)      # Heisenberg Uncertainty Principle is associated with fft
freq_shift = np.fft.fftshift(freq)
plt.figure(1)
plt.subplot(211)
plt.plot(time, signal, color='lightblue', linewidth=1)

plt.subplot(212)
plt.plot(freq_shift, np.fft.fftshift(np.abs(fourier)), color='blue', linewidth=1)
plt.show()

# Gabor Transform
width = 0.3
slide = np.arange(0, 10, 0.1)
spec = np.zeros(shape=(len(slide),len(time)))
plt.figure(2)
for i in range(len(slide)):
    filter = np.exp(-width*(time-slide[i])**2)
    signal_filter = filter * signal
    fourier_filterr = np.fft.fft(signal_filter)

    plt.subplot(311)
    plt.plot(time, signal, color='lightblue', linewidth=1)
    plt.plot(time, filter, color='lightgreen', linewidth=1)

    plt.subplot(312)
    plt.plot(time, signal_filter, color='blue', linewidth=1)

    plt.subplot(313)
    plt.plot(freq_shift, np.fft.fftshift(np.abs(fourier_filterr)), color='green', linewidth=1)

    spec[i, :] = np.fft.fftshift(np.abs(fourier_filterr)).reshape(-1)
    plt.xlim(-T , T )
    plt.pause(0.005)
    plt.clf()

# plotting the spectrogram

slide_mesh, freq_mesh = np.meshgrid(slide, freq_shift)

fig, ax = plt.subplots()
ax.set_yscale('symlog')
ax.pcolormesh(slide_mesh, freq_mesh, spec.transpose())
plt.xlim([0,10])
plt.ylim([-60,60])
#ٍplt.zlim([-10,10])
plt.show()
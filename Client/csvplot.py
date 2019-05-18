import numpy as np
import scipy as sy
import scipy.fftpack as syfp
import pylab as pyl

# Read in data from file here
array = np.loadtxt("test_data.csv")
length = len(array)
# Create time data for x axis based on array length
x = sy.linspace(0.00001, length*0.00001, num=length)

# Do FFT analysis of array
FFT = sy.fft(array)
# Getting the related frequencies
freqs = syfp.fftfreq(array.size, d=(x[1]-x[0]))

# Create subplot windows and show plot
pyl.subplot(211)
pyl.plot(x, array)
pyl.subplot(212)
pyl.plot(freqs, sy.log10(FFT), 'x')
pyl.show()
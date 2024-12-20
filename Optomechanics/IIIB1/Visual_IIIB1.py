# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# import data and visualize
a = 0.8
lst_max_amplitude = []
lst_freq = [1,30,15,45]

data = pd.read_csv("IIIB1\B2d.csv")
f = data['Freq']
dBm = data['Amp']
lst_max_amplitude.append(np.max(dBm))
plt.plot(f/1000, dBm, label = 'Vpp = 3.6 V, f = 45 kHz', color='lightskyblue', alpha = a)

data = pd.read_csv("IIIB1\B2c.csv")
f = data['Freq']
dBm = data['Amp']
lst_max_amplitude.append(np.max(dBm[200:600]))
plt.plot(f/1000, dBm, label = 'Vpp = 5.2 V, f = 30 kHz', color='royalblue', alpha = a)

data = pd.read_csv("IIIB1\B2a.csv")
f = data['Freq']
dBm = data['Amp']
lst_max_amplitude.append(np.max(dBm[100:600]))
plt.plot(f/1000, dBm, label = 'Vpp = 10 V, f = 15 kHz', color='blue', alpha = a)

data = pd.read_csv("IIIB1\B2b.csv")
f = data['Freq']
dBm = data['Amp']
lst_max_amplitude.append(np.max(dBm[100:600]))
plt.plot(f/1000, dBm, label = 'Vpp = 10 V, f = 1 kHz', color='navy', alpha = a)

amplitude_error = [abs(float(i)*0.05) for i in lst_max_amplitude]
print(amplitude_error)
# adjust plot
plt.xlim(1,50)
plt.ylim(-87,-15)
plt.ylabel(r'Amplitude (dBm)')
plt.xlabel(r'Frequency (kHz)')
plt.legend(loc=1)
plt.grid()
plt.savefig('Images\IIIB1.eps', format='eps')
plt.show()

plt.errorbar(lst_freq, lst_max_amplitude, yerr=amplitude_error, color='b', fmt='.')
plt.xlim(0,50)
plt.ylim(-60,-15)
plt.ylabel(r'Max amplitude (dBm)')
plt.xlabel(r'Frequency (kHz)')
plt.grid()
plt.savefig('Images\IIIB1_amplitudes.eps', format='eps')
plt.show()


# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# import data and visualize
a = 0.8

data = pd.read_csv("IIIB1\B2d.csv")
f = data['Freq']
dBm = data['Amp']
plt.plot(f, dBm, label = 'Vpp = 3.6 V, f = 45 kHz', color='lightskyblue', alpha = a)

data = pd.read_csv("IIIB1\B2c.csv")
f = data['Freq']
dBm = data['Amp']
plt.plot(f, dBm, label = 'Vpp = 5.2 V, f = 30 kHz', color='royalblue', alpha = a)

data = pd.read_csv("IIIB1\B2a.csv")
f = data['Freq']
dBm = data['Amp']
plt.plot(f, dBm, label = 'Vpp = 10 V, f = 15 kHz', color='blue', alpha = a)

data = pd.read_csv("IIIB1\B2b.csv")
f = data['Freq']
dBm = data['Amp']
plt.plot(f, dBm, label = 'Vpp = 10 V, f = 1 kHz', color='navy', alpha = a)

# adjust plot
plt.xlim(1e3,50e3)
plt.ylim(-87,-15)
plt.ylabel(r'Amplitude (dBm)')
plt.xlabel(r'Frequency (Hz)')
plt.legend(loc=1)
plt.grid()
plt.savefig('Images\IIIB1.eps', format='eps')
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# import data, visualize and adjust plot
fig, axs = plt.subplots(3,1, figsize=(6, 12))
lst = np.array([73518,  460729, 1290055, 2527993, 4178954])/1000
a = 0.7

data = pd.read_csv("IIIB2\K1tm100.csv")
f = data['Freq']
dBm = data['Amp']
axs[0].plot(f/1000, dBm, color='navy', alpha=a, label='Measurement 1')
data = pd.read_csv("IIIB2\K1tm100_2.csv")
f = data['Freq']
dBm = data['Amp']
axs[0].plot(f/1000, dBm, color='teal', alpha=a, label='Measurement 2')

axs[0].vlines(lst, -100, -50, 'k')
axs[0].set_xlabel(r'Frequency (kHz)')
axs[0].set_ylabel(r'Amplitude (dBm)')
axs[0].set_xlim(0, 100)  
axs[0].set_ylim(-100,-50) 
axs[0].legend()
axs[0].grid(True)

data = pd.read_csv("IIIB2\K1tm400.csv")
f = data['Freq']
dBm = data['Amp']
axs[1].plot(f/1000, dBm, color='navy', alpha=a, label='Measurement 1')
data = pd.read_csv("IIIB2\K1tm400_2.csv")
f = data['Freq']
dBm = data['Amp']
axs[1].plot(f/1000, dBm, color='teal', alpha=a, label='Measurement 2')

axs[1].vlines(lst, -100, -50, 'k')
axs[1].set_xlabel(r'Frequency (kHz)')
axs[1].set_ylabel(r'Amplitude (dBm)')
axs[1].set_xlim(0, 400)  
axs[1].set_ylim(-100,-50) 
axs[1].legend()
axs[1].grid(True)

data = pd.read_csv("IIIB2\K1tm1600.csv")
f = data['Freq']
dBm = data['Amp']
axs[2].plot(f/1000, dBm, color='navy', alpha=a, label='Measurement 1')
data = pd.read_csv("IIIB2\K1tm1600_2.csv")
f = data['Freq']
dBm = data['Amp']
axs[2].plot(f/1000, dBm, color='teal', alpha=a, label='Measurement 2')

axs[2].vlines(lst, -100, -50, 'k')
axs[2].set_xlabel(r'Frequency (kHz)')
axs[2].set_ylabel(r'Amplitude (dBm)')
axs[2].set_xlim(0, 1600)  
axs[2].set_ylim(-100,-50) 
axs[2].legend()
axs[2].grid(True)



plt.tight_layout()
plt.savefig('Images\IIIB2_K.eps', format='eps')
plt.show()

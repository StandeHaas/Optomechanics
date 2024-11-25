# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# import data, visualize and adjust plot
a= 0.7
max = []
data = pd.read_csv("IIIB4\IIIB4_0.csv")
f = data['Freq']
dBm = data['Amp']
max.append(np.max(dBm))
plt.plot(f/1000, dBm, 'o', linestyle='-', alpha=a, color='navy')
data = pd.read_csv("IIIB4\IIIB4_10.csv")
f = data['Freq']
dBm = data['Amp']
max.append(np.max(dBm))
plt.plot(f/1000, dBm, 'o', linestyle='-',alpha=a, color='blue')
data = pd.read_csv("IIIB4\IIIB4_15.csv")
f = data['Freq']
dBm = data['Amp']
max.append(np.max(dBm))
plt.plot(f/1000, dBm,'o', linestyle='-', alpha=a, color='royalblue')
data = pd.read_csv("IIIB4\IIIB4_25.csv")
f = data['Freq']
dBm = data['Amp']
max.append(np.max(dBm))
plt.plot(f/1000, dBm, 'o', linestyle='-',alpha=a, color='cyan')
data = pd.read_csv("IIIB4\IIIB4_40.csv")
f = data['Freq']
dBm = data['Amp']
max.append(np.max(dBm))
plt.plot(f/1000, dBm, 'o', linestyle='-',alpha=a, color='violet')
data = pd.read_csv("IIIB4\IIIB4_50.csv")
f = data['Freq']
dBm = data['Amp']
max.append(np.max(dBm))
plt.plot(f/1000, dBm, 'o', linestyle='-',alpha=a, color='palevioletred')
data = pd.read_csv("IIIB4\IIIB4_75.csv")
f = data['Freq']
dBm = data['Amp']
max.append(np.max(dBm))
plt.plot(f/1000, dBm, 'o', linestyle='-',alpha=a, color='brown')
data = pd.read_csv("IIIB4\IIIB4_90.csv")
f = data['Freq']
dBm = data['Amp']
max.append(np.max(dBm))
plt.plot(f/1000, dBm, 'o', linestyle='-',alpha=a, color='r')
data = pd.read_csv("IIIB4\IIIB4_100.csv")
f = data['Freq']
dBm = data['Amp']
max.append(np.max(dBm))
plt.plot(f/1000, dBm, 'o', linestyle='-',alpha=a, color='maroon')

plt.xlim(10,30)
plt.ylim(-95,-65)
plt.xlabel(r'Frequency (kHz)')
plt.ylabel(r'Amplitude (dBm)')
plt.grid(True)
plt.show()

plt.plot([100,90,85,75,60,50,25,10,0], max, 'o', color='b')
plt.xlim(0,100)
plt.ylim(-70,-60)
plt.xlabel(r'Position on the 200 $\mu m$ cantilever (%)')
plt.ylabel(r'Max amplitude (dBm)')
plt.grid(True)
plt.savefig('Images\IIIB4.eps', format='eps')
plt.show()
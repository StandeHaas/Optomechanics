# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# sort all data of the 3 measurements and add to a list
lst_data = []

data = pd.read_csv('IIIA3\close.csv')
s = data['Second']
v1 = data['Volt']
v2 = data['Volt2']
lst_data.append([s,v1,v2])

data = pd.read_csv('IIIA3\middle.csv')
v2 = data['Volt']
v1 = data['Volt2']
lst_data.append([s,v1,v2])

data = pd.read_csv('IIIA3\daway.csv')
v2 = data['Volt']
v1 = data['Volt2']
lst_data.append([s,v1,v2])

# Create a 3x1 grid of subplots
fig, axs = plt.subplots(3,1, figsize=(6, 12))

for i in range(0,3):
    axs[i].plot(lst_data[i][0], lst_data[i][2], color='b')
    axs[i].set_xlabel(r'time (s)')
    axs[i].set_ylabel(r'voltage (V)')
    axs[i].set_xlim(np.min(lst_data[i][0]), np.max(lst_data[i][0]))  
    axs[i].set_ylim(np.min(lst_data[i][2]), np.max(lst_data[i][2])) 
    axs[i].grid(True)      


plt.tight_layout()
plt.savefig('Images\IIIA3.eps', format='eps')
plt.show()

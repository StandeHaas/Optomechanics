# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# sort all data of the 3 measurements and add to a list
lst_data = []

data = pd.read_csv('IIIA6\d1260.csv')
s = data['Second']
v1 = data['Volt']
v2 = data['Volt2']
lst_data.append([s,v1,v2])

data = pd.read_csv('IIIA6\d1250.csv')
v2 = data['Volt']
v1 = data['Volt2']
lst_data.append([s,v1,v2])

data = pd.read_csv('IIIA6\d1000.csv')
v2 = data['Volt']
v1 = data['Volt2']
lst_data.append([s,v1,v2])


# Create a 2x1 grid of subplots
fig, axs = plt.subplots(2,1, figsize=(6, 12))

for i in range(2,0,-1):
    print(i)
    axs[2-i].plot(lst_data[i][0], lst_data[i][2], color='b')
    axs[2-i].set_xlabel(r'time (s)')
    axs[2-i].set_ylabel(r'voltage (V)')
    axs[2-i].set_xlim(np.min(lst_data[i][0]), np.max(lst_data[i][0]))  
    axs[2-i].set_ylim(np.min(lst_data[i][2]), np.max(lst_data[i][2])) 
    axs[2-i].grid(True)      

plt.tight_layout()
plt.savefig('Images\IIIA6.eps', format='eps')
plt.show()

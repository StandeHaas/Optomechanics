# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

#constants
lam = 635e-9

#function used to plot v1 in graph (t, v2)
def scale_list_to_range(lst, new_min, new_max):
    old_min = min(lst)
    old_max = max(lst)
    
    if old_max == old_min:
        return [new_min] * len(lst) 
    scaled_lst = [new_min + (x - old_min) * (new_max - new_min) / (old_max - old_min) for x in lst]
    return scaled_lst


# sort all data of the 4 measurements and add to a list
lst_data = []
lst_f = [50,200,400,600,800,1000,1250,1260,1500,1750,2000]
for num in lst_f:
    data = pd.read_csv(f'IIIA6\d{num}.csv')
    s = data['Second']
    v1 = data['Volt']
    v2 = data['Volt2']
    lst_data.append([s,v1,v2])

# determine the number of peaks per measurement (done by hand)
lst_peakes = [9,13,16,12,6,3,3,3,3,3,3]


# loop through the measurements and do the calculations for all the measurments.
lst_j = [] # list to get the number of found R per measurement
lst_R = [] # list to store the found values for R
lst_e = [] # list to stor the found error/standard deviations

for i in range(len(lst_data)):
    # get number of peaks and the data
    s  = lst_data[i][0]         # time
    v1 = lst_data[i][1]         # input
    v2 = lst_data[i][2]         # output
    n  = lst_peakes[i]          # n-peaks

    # split in to seperate peaks
    split_lists_s = np.array(np.array_split(s, n), dtype=object)
    split_lists_v2 = np.array(np.array_split(v2, n), dtype=object)
    split_lists_s = split_lists_s.tolist()
    split_lists_v2 = split_lists_v2.tolist()

    # determine the maximum of every peak in order to calculate the distance between the peaks later
    m = 0
    k = 0 
    lst = []
    index = []
    for list in split_lists_v2:
        panda = pd.Series(list)
        max_index = panda.idxmax()
        lst.append(split_lists_s[k][max_index]) # we create a list of all the maxima
        if max_index > 600/n:
            max_index -= m
        index.append(m + max_index) # we create a list of index to be able to know which indexes the maxima have in the input signal list
        m += len(list)
        k += 1

    # plot to be able to check the calculations
    plt.clf()
    plt.plot(s, v2, color='b')
    plt.plot(s, scale_list_to_range(v1, 1.005*np.min(v2), 0.995*np.max(v2)))
    plt.vlines(lst, ymin = 0, ymax=1, color='black', alpha = 0.7)
    plt.ylim(np.min(v2), np.max(v2))
    plt.xlim(np.min(s), np.max(s))
    plt.xlabel(r'time (s)')
    plt.ylabel(r'voltage (V)')
    plt.grid()
    plt.savefig(f'Images\IIIA6_2_{i+2}.eps', format='eps')
    #plt.show()

    # determine the distances between the peaks
    d = []
    for i in range(len(lst)-1):
        d.append(lst[i+1] - lst[i])

    # calculate R, since sometimes the distances aren't found properly, we one take the ones in account for which this is the case
    R = []
    j = 0
    for i in range(len(lst)-1):
        if d[i] > np.mean(d)*0.8 and d[i] < np.mean(d)*1.2:
            j += 1
            R.append(lam / 2 / (v1[index[i+1]] - v1[index[i]])) # we use lambda / 2 since we always check between two maxima, which has a lenght of lambda / 2


    # since v1 sometimes contains a wrong measurement a infite values might slip through we delete those
    filtered_data = [] 
    for v in R:
        if v < 1000:
            filtered_data.append(v)
    lst_j.append(j)
    lst_R.append(np.mean(filtered_data))
    lst_e.append(np.std(filtered_data, ddof=1))

print('R:', lst_R)
print('e:', lst_e)

plt.clf()
plt.errorbar(lst_f, lst_R, yerr=lst_e, fmt='o',  markersize=5, color='b')
plt.xlim(0,2100)
plt.ylim(0.5e-7, 2.5e-6)
plt.ylabel(r'Responsivity (m/V)')
plt.xlabel(r'Frequency (Hz)')
plt.grid()
plt.savefig('Images\IIIA6_2_errobar_of_r.eps', format='eps')
plt.show()
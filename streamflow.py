# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np

array1 = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv', delimiter=',',dtype=str,skip_header=1)
x = array1[:, 0].astype('datetime64')
y_1 = array1[:,1].astype(float)
y_2 = array1[:,2].astype(float)
y_3 = array1[:,3].astype(float)
y_4 = array1[:,4].astype(float)
y_5 = array1[:,5].astype(float)

# y_1 - Site 10163000
# y_2 - Site 10155200
# y_3 - Site 10155500
# y_4 - Site 10154200
# y_5 - Site 10155000

plt.plot(x, y_1, label='10163000', color='purple')
plt.plot(x, y_2, label='10155200', color='blue')
plt.plot(x, y_3, label='10155500', color='green')
plt.plot(x, y_4, label='10154200', color='orange')
plt.plot(x, y_5, label='10155000', color='red')

plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')
plt.title('Provo River Streamflow Data (2021)')
plt.grid(True)
plt.legend(title='Site Numbers', loc='upper right')
plt.show()


# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime



L = 6
Ra = 170
Rb=410
P1=100
q1=120
q2=120
x = np.linspace(0, L, 500)
V = np.zeros_like(x)
for i in range(len(x)):
  if x[i] < 2:
    V[i] = Ra-(q1*x[i])
  elif 2 < x[i] < 4:
    V[i] = Ra - (q1*2) - P1
  elif 4 < x[i] :
    V[i] = Ra - (q1*2) - P1 + Rb - (q2*(x[i]-4))
plt.plot(x, V)
plt.xlabel('x ft')
plt.ylabel('V lb')
plt.title('Shear Diagram')
plt.fill_between(x, V, color='skyblue', alpha=0.3)
#This adds a horizontal line with the different line attributes
plt.axhline(0, color='black', linestyle='-', linewidth=1.5)
plt.show()




L = 6
Ra = 170
Rb=410
P1=100
q1=120
q2=120
x = np.linspace(0, L, 500)
M = np.zeros_like(x)

for i in range(len(x)):
    if x[i] < 2:
         M[i]= (Ra * x[i]) - (q1 * x[i]**2 / 2)
    elif x[i] <= 4:
         M[i]= (Ra * x[i]) - (q1 * 2 * (x[i] - 1)) - (P1 * (x[i] - 2))
    elif x[i] <= L:
          M[i]= (
            (Ra * x[i])
            - (q1 * 2 * (x[i] - 1))
            - (P1 * (x[i] - 2))
            + (Rb * (x[i] - 4))
            - (q2 * (x[i] - 4) * ((x[i] - 4) / 2))
        )
plt.plot(x, M)
plt.xlabel('x (ft)')
plt.ylabel('M (lb-ft)')
plt.title('Moment Diagram')
plt.fill_between(x, M, color='skyblue', alpha=0.3)
#This adds a horizontal line with the different line attributes
plt.axhline(0, color='black', linestyle='-', linewidth=1.5)
plt.show()


array1 = np.genfromtxt('/content/2013-2014-Pasadena-Temperature-Data.csv', delimiter=',',dtype=str,skip_header=1)

x = [datetime.strptime(date, '%Y-%m-%d') for date in array1[:, 0]]
y_1 = array1[:, 1].astype(float)
y_2 = array1[:, 2].astype(float)



plt.figure(figsize=(10, 6))
plt.plot(x, y_1, label='High Temperature')
plt.plot(x, y_2, label='Low Temperature')
plt.xlabel('Date')
plt.ylabel('Degrees (Fahrenheit)')
plt.title('Pasadena Temperature Data 2013-2014')
plt.yticks(range(40, 101,10))
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

array2 = np.genfromtxt('/content/June-2021-Provo-River-Streamflow-Rates.csv', delimiter=',',dtype=str,skip_header=1)
x = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in array2[:, 0]]

y_1 = array2[:, 1].astype(float)
y_2 = array2[:, 2].astype(float)
y_3 = array2[:, 3].astype(float)
y_4 = array2[:, 4].astype(float)
y_5 = array2[:, 5].astype(float)



plt.figure(figsize=(10, 6))
plt.plot(x, y_1, label='Site 10163000')
plt.plot(x, y_2, label='Site 10155200')
plt.plot(x, y_3, label='Site 10155500')
plt.plot(x, y_4, label='Site 10154200')
plt.plot(x, y_5, label='Site 10155000')
plt.xlabel('Date')
plt.ylabel('Streamflow (cfs)')
plt.title('Provo River Streamflow Data (2021)')
plt.legend(title='Site Numbers',loc='upper right')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()



array3 = np.genfromtxt('/content/Fremont-Bridge-Bicycle-Count.csv', delimiter=',',dtype=str,skip_header=1)

x=[datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in array3[:, 0]]
y_1 = array3[:, 1].astype(float)
y_2 = array3[:, 2].astype(float)
y_3 = array3[:, 3].astype(float)



plt.figure(figsize=(10, 6))
plt.bar(x, y_1, label='Fremont Bridge Total')
plt.bar(x, y_2, label='Fremont Bridge East Sidewalk')
plt.bar(x, y_3, label='Fremont Bridge West Sidewalk')
plt.xlabel('Date')
plt.ylabel('Number of Bicycles')
plt.title('Fremont Bridge Bicycle Count')
plt.legend(loc='upper left')

plt.grid(True)
plt.show()



array3 = np.genfromtxt('/content/2012-US-Birth-Rates.csv', delimiter=',',dtype=str,skip_header=1)

x=[datetime.strptime(date, '%Y-%m-%d %H:%M:%S') for date in array3[:, 0]]
y_1 = array3[:, 1].astype(float)



plt.figure(figsize=(12,4))
plt.plot(x, y_1)
plt.title('Average U.S. Daily Birth Data')
plt.xlabel('Date')
plt.ylabel('Births')
plt.grid(True)
plt.show()
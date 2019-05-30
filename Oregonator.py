 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 23:41:00 2018

@author: kevinmacdonald
with additional comments by holdenorias
"""

import numpy as np
import matplotlib.pyplot as plt

A_list=[] #initializing lists that will store data.
P_list=[] #these lists track the concentrations of BrO3-, HBrO, HBrO2, Br-, 2Ce4+ -HO
X_list=[]
Y_list=[]
Z_list=[]
x_list=[]

refresh=.000001 
'''
how many times per second the reaction rates will be updated
you must change this number to the point your computer can barely run it once to show
that there is not significant change in concentration resulting from large timesteps

'''
print(1/refresh)

A = 10 #Initial concentrations of species
X = .0001
Y = .0001
Z = 0
P = 0
k1 = 1 
k2 = 10000000 
k3 = 2
k4 = 2 
k5 = 5 

z=0 #value for tracking maximum change before updating rates

for x in np.arange(0,2,refresh):
    A_list+=[A] #adding current concentrations to data.
    P_list+=[P] #if program crashes try not adding data every loop (you are runnign out of ram)
    X_list+=[X] #hbro2
    Y_list+=[Y]
    Z_list+=[Z]
    x_list+=[x]
    r1 = k1*A*Y #calculating current rates
    r2 = k2*X*Y
    r3 = k3*A*X
    r4 = k4*X*X
    r5 = k5*Z
    dA = -r1 - 2*r3 +r4 #updating current rates of change for each substance
    dX = r1-r2-2*r3+4*r3-2*r4
    dY = -r1-r2+2*r5
    dP = r1 + 2*r2 + r4
    dZ = 2*r3 - 2*r5 
    X+=dX*refresh #updating how much each changed over the change in time
    Y+=dY*refresh
    Z+=dZ*refresh
    A+=dA*refresh
    P+=dP*refresh
    if (X<0): # protection against rounding errors and negative concentration
        X=0
    if (Y<0):
        Y=0
    if (Z<0):
        Z=0
    if (abs(dZ*refresh)>abs(z)): #tracking max change
        z=dZ*refresh
    if (abs(dX*refresh)>abs(z)):
        z=dX*refresh
    if (abs(dY*refresh)>abs(z)):
        z=dY*refresh


print(z)

plt.figure(1) #graph code
plt.subplot(1,1,1)
plt.plot(x_list, X_list, 'r')
plt.plot(x_list, Y_list, 'y')
plt.plot(x_list, Z_list, 'g')
plt.title('Progression of Oregonator Modeled Rxn') # subplot 211 title
plt.ylabel('Concentration (M)')
plt.xlabel('Time (s)')
#plt.plot(x_list, P_list, 'b--')
#plt.plot(x_list, A_list, 'b')
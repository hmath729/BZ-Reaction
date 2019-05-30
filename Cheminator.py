 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:51:00 2019

@author: holdenorias
"""

import numpy as np
import matplotlib.pyplot as plt

X_list=[]
Y_list=[]
Z_list=[]
x_list=[]

refresh=.000001 #timestep. smaller number = harder to run, greater precision.

#Initial concentrations of dummy reactants
initX = 1
initY = 1
initZ = 1
X = initX
Y = initY
Z = initZ
k1 = 1 
k2 = 1
k3 = 1 

z=0 #value for tracking maximum change before updating rates

for x in np.arange(0,5,refresh): #adding current concetrations to data.
     #if program crashes try not adding data every loop (you are runnign out of ram)
    X_list+=[X]
    Y_list+=[Y]
    Z_list+=[Z]
    x_list+=[x]
    r1 = k1*X #calculating current rates
    r2 = k2*Y*Y
    r3 = k3*Z*Z*Z
    dX = -r1
    dY = -r2
    dZ = -r3
    X+=dX*refresh
    Y+=dY*refresh
    Z+=dZ*refresh #updating how much each changed over the change in time
    if (X<0): # protection against rounding errors and negative concentration
        X=0
    if (Y<0):
        Y=0
    if (Z<0):
        Z=0
    if (abs(dX*refresh)>abs(z)):
        z=dX*refresh
    if (abs((X-0.5*initX))<0.00001):
        print("half-time X")
        print(x)
    if (abs((Y-0.5*initY))<0.00001):
        print("half-time Y")
        print(x)
    if (abs((Z-0.5*initZ))<0.00001):
        print("half-time Z")
        print(x)
    


print(z)

plt.figure(1) #graph code
plt.subplot(1,1,1)
plt.plot(x_list, X_list, 'r')
plt.title('Progression of 1st-Order Modeled Rxn') # subplot 211 title
plt.ylabel('Concentration (M)')
plt.xlabel('Time (s)')

plt.figure(2) #graph code
plt.subplot(1,1,1)
plt.plot(x_list, Y_list, 'g')
plt.title('Progression of 2nd-Order Modeled Rxn') # subplot 211 title
plt.ylabel('Concentration (M)')
plt.xlabel('Time (s)')

plt.figure(3)
plt.subplot(1,1,1)
plt.plot(x_list, Z_list, 'y')
plt.title('Progression of 3rd-Order Modeled Rxn') # subplot 211 title
plt.ylabel('Concentration (M)')
plt.xlabel('Time (s)')
#plt.plot(x_list, P_list, 'b--')
#plt.plot(x_list, A_list, 'b')

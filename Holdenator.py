 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues May 28 23:14:00 2019

@author: holdenorias
"""

import numpy as np
import matplotlib.pyplot as plt

#initializing lists that will store data. 

A_list=[] #BrO3-
B_list=[] #BrO2

P_list=[] #Ce(III)
Q_list=[] #Ce(IV)

T_list=[] #Br2O4
U_list=[] #HBrO2
V_list=[] #Br2
W_list=[] #H2O
X_list=[] #H+
Y_list=[] #Br-
Z_list=[] #HOBr
x_list=[] #time
t = 0 #looper

refresh=.00001 #how many times per second the reaction rates will be updated
#you must change this number to the point your computer can barley run it once to show
#that there is not signigant change from the larger a faster running number you chose
print(1/refresh)

 #Initial concentrations
A = 0.077
B = 0
P = 0
Q = 0.0063
T = 0
U = 0
V = 0
X = 1.8
Y = 0.020
Z = 0

'''
k1 = 120000
k2 = 1
k3 = 1
k4 = 1
k5 = 1
k6 = 1000000
k7 = 1
k8 = 1
k9 = 1
k10 = 100
k11 = 1
k12 = 1000
k13 = 10
k14 = 1
'''

k1 = 2300000000 
k2 = 2
k3 = 2000000
k4 = .00002
k5 = 2
k6 = 3000
k7 = 3000
k8 = .0000000075
k9 = 33
k10 = 2200
k11 = 74000
k12 = 1400000000
k13 = 62000
k14 = 7000


z=0 #value for tracking maximum change before updating rates

#important trials: 183, 203
for x in np.arange(0,.001,refresh):
    A_list+=[A] #adding current concetrations to data.
    B_list+=[B]
    P_list+=[P] #if program crashes try not adding data every loop (you are runnign out of ram)
    Q_list+=[Q]
    T_list+=[T]
    U_list+=[U]
    V_list+=[V]
    X_list+=[X]
    Y_list+=[Y]
    Z_list+=[Z]
    x_list+=[x]
    
    #calculating current rates
    r1 = k1*X*Y*Z
    r2 = k2*V
    r3 = k3*U*X*Y
    r4 = k4*Z*Z
    r5 = k5*A*X*X*Y
    r6 = k6*U*Z
    r7 = k7*U*U
    r8 = k8*A*X*Z
    r9 = k9*A*U*X
    r10 = k10*T
    r11 = k11*T
    r12 = k12*B*B
    r13 = k13*B*P*X
    r14 = k14*Q*U
    
    #updating current rates of change for each substance
    dA = -r5 + r6 + r7 - r8 - r9 + r10
    dB = r11 - r12
    dP = -r13 + r14
    dQ = r13 - r14
    dT = -r11 + r12
    dU = -r3 + r4 + r5 - r6 - r7 + r8 - r9 + r10 + r11 - r12
    dV = r1 - r2
    dX = -r1 + r2 - r3 + r4 - r5 + r6 + r7 - r8 - r9 + r10 - r13 + r14
    dY = -r1 + r2 - r3 + r4 - r5 + r6
    dZ = -r1 + r2 + r3 - r4 + r5 - r6 + r7 - r8
    
    #updating how much each changed over the change in time
    A+=dA*refresh
    B+=dB*refresh
    P+=dP*refresh
    Q+=dQ*refresh
    T+=dT*refresh
    U+=dU*refresh
    V+=dV*refresh
    X+=dX*refresh 
    Y+=dY*refresh
    Z+=dZ*refresh
    
    # protection against rounding errors and negative concentration
    if (A<0):
        A=0
    if (B<0):
        B=0
    if (P<0):
        P=0
    if (Q<0):
        Q=0
    if (T<0):
        T=0
    if (U<0):
        U=0
    if (V<0):
        V=0
    if (X<0): 
        X=0
    if (Y<0):
        Y=0
    if (Z<0):
        Z=0
        
    
    if (abs(dU*refresh)>abs(z)): #tracking max change
        z=dU*refresh
    if (abs(dQ*refresh)>abs(z)):
        z=dQ*refresh
    if (abs(dY*refresh)>abs(z)):
        z=dY*refresh


print(z)

plt.figure(1) #graph code
#plt.figure(figsize=(10,10))
plt.subplot(1,1,1)
plt.plot(x_list, P_list, 'b')
#plt.plot(x_list, Q_list, 'c')
#plt.plot(x_list, Y_list, 'm')
plt.plot(x_list, U_list, 'r')
#plt.plot(x_list, T_list, 'y')
plt.plot(x_list, Z_list, 'g')
plt.title('Progression of Holdenator Modeled Rxn') # subplot 211 title
plt.ylabel('Concentration (M)')
plt.xlabel('Time (s)')
#plt.plot(x_list, P_list, 'b--')
#plt.plot(x_list, A_list, 'b')

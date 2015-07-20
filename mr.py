# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:24:48 2015

@author: Kevins
"""
import pylab as p


#Defining parameters

alpha = 1  
theta = 0.064 
sigma = 0.27 
R0 = 3
period = 1
n_path = 1000   #number of simulations
n = 1000     #number of partitions on time 1

#Generating Brownian motions
dt = period / n
t = p.linspace(0,period,n+1)[:-1]   
    #generation step size = 1/1000
dB = p.randn(n_path,n+1) * p.sqrt(dt) ; dB[:,0] = 0
B = dB.cumsum(axis=1)
R = p.zeros_like(B)

R[:,0] = R0

for col in range(n):
    R[:,col+1] = R[:,col] + (theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]


R_sampled = R[0:5,:-1]
p.plot(t,R_sampled.transpose())
label = 'Time , $t$' ; p.xlabel(label)          
label = 'Stock prices, $S$' ; p.ylabel(label)

para1 = '\n with $\\alpha$ = ' + str(alpha)
para2 = ', $\\theta$ = ' + str(theta)
para3 = ', and $\sigma$ = ' + str(sigma) + '\n'
p.title('5 runs of Mean reversal process for ' + label + para1 + para2 + para3)
p.show();

E_R1 = R0 * p.exp(-alpha*t[-period]) + theta*(1-p.exp(-alpha*period)) 
print('E(R1) = ' + str(E_R1))
mask = R[:,-1] > 2
P_R1 = sum(mask)/n_path
print('P(R1 > 2) = ' + str(P_R1))
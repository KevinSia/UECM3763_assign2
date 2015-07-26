import pylab as p
import numpy as np

#dRt = alpha*(theta - Rt)*dt + sigma*Rt*dBt

#Defining parameters

alpha = 1  
theta = 0.064 
sigma = 0.27 
R0 = 3
time = 1
n_path = 1000   #number of simulations
n = 1000     #number of partitions on time 1

#Generating Brownian motions

dt = time / n
t = p.linspace(0,time,n+1)   ##[:-1] 
    #generation step size = 1/1000
dB = p.randn(n_path,n+1) * p.sqrt(dt) ; dB[:,0] = 0
B = dB.cumsum(axis=1)


# Generating R with Euler-Maruyama method

R = p.zeros_like(B)
R[:,0] = R0

for col in range(n):
    R[:,col+1] = R[:,col] + (theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]


#Plotting 5 realization of R
run = 5
R_sampled = R[0:run]     # 5 runs of R is extracted
p.plot(t,R_sampled.transpose())

#Plot labelling

label = 'Time , $t$' ; p.xlabel(label)          
label = '$R_t$' ; p.ylabel(label)
para1 = '\n with $\\alpha$ = ' + str(alpha)
para2 = ', $\\theta$ = ' + str(theta)
para3 = ', and $\sigma$ = ' + str(sigma) + '\n'
p.title(str(run) + ' runs of Mean reversal process for ' + label + para1 + para2 + para3)
p.show();

#Calculations

R1 = p.array(R[:,-1])
E_R1 = np.mean(R1)
print('E(R1) = ' + str(E_R1))
mask = R[:,-1] > 2
P_R1 = sum(mask)/n_path
print('P(R1 > 2) = ' + str(P_R1))
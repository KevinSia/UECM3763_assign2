import pylab as p
import numpy as np

#Defining parameters

alpha = 1  
theta = 0.064 
sigma = 0.25 
R0 = 0.5
period = 1
n_path = 1000   #number of simulations
n = 1000     #number of partitions on time 1

#Generating Brownian motions

t = p.linspace(0,period,n+1)   
    #generation step size = 1/1000
dB = p.randn(n_path,n+1) / p.sqrt(n) ; dB[:,0] = 0
B = dB.cumsum(axis=1)


#Calculating Ito integral part of GBM

ft = p.exp(alpha*t)
ft[1:] = ft[:-1] ; ft[0] = 0  
    #taking away last value and insert 0 from front
dB = p.array(dB)
ito = ft*dB
ito = ito.cumsum(axis=1)

#Calculation of GBM

C1 = p.exp(-t)
C2 = p.exp(-alpha*t)  

Rt = theta * (1 - C2) + R0 * C2 + sigma * C1 * ito
    #Rt has 1000 runs , each run has 1001 points

#plotting 5 realizations of the mean reversal process
runs = 1
Rt_sample = Rt[0:runs]
p.plot(t,Rt_sample.transpose())
label = 'Time , $t$' ; p.xlabel(label)          
label = 'Stock prices, $S$' ; p.ylabel(label)

para1 = '\n with $\\alpha$ = ' + str(alpha)
para2 = ', $\\theta$ = ' + str(theta)
para3 = ', and $\sigma$ = ' + str(sigma) + '\n'
p.title('5 runs of Mean reversal process for ' + label + para1 + para2 + para3)
p.show();

R1 = p.array(Rt[:,-1])
E_R1 = np.mean(R1)
mask = R1 > 2
P_R1_m2 = sum(mask)/len(mask)
print('E(R1) = ',E_R1,'\nP(R1 > 2) = ',P_R1_m2)




#remainder
#t[1:1000] gets 999 numbers without t[1000]
#ft[:-1] takes all number excluding the last number
#dB[:,1:] takes all row and all column excluding the first column
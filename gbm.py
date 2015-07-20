import pylab as p
import numpy as np


#Defining parameters

mu = 0.1;
sigma = 0.26;
S0 = 39;
n_path = 1000; #number of simulations
n = 1000 ;     #number of partitiions on time 3
period = 3;

#Generating Brownian Motion

t = p.linspace(0,period,n+1)
dB = p.randn(n_path,n+1) / p.sqrt(n/period) ; dB[:,0] = 0 #1st column of dB = 0
B = dB.cumsum(axis = 1) #cumulative sum over columns for each row

#Calculate stock prices

nu = mu - sigma * sigma / 2.0
S = p.zeros_like(B) ; S[:,0] = S0
S[:,1:] = S0 * p.exp(nu * t[1:] + sigma * B[:,1:])
    #S has 1000 runs, each run has 1001 points

#plotting 5 realizations of stock price GBM

S_sample = S[0:5]
p.plot(t,S_sample.transpose());
label = 'Time , $t$' ; p.xlabel(label)
label = 'Stock prices, $S$' ; p.ylabel(label)
para1 = '\n with $\mu$ = ' + str(mu)
para2 = 'and $\sigma$ = ' + str(sigma) + '\n'
p.title('5 runs of GBM for ' + label + para1 + para2)
p.show();


S3 = p.array(S[:,-1])
E_S3 = np.mean(S3)
Var_S3 = np.var(S3)
print('E(S3) = ' + str(E_S3) , '\nVar(S3) = ' + str(Var_S3))

mask = S3 > 39                  #number of values more than 39
P_S3_m39 = sum(mask) / len(mask)    
S3_39 = S3 * mask               #extracting values more than 39
E_S3_m39 = sum(S3_39) / sum(mask)
print('P(S3 > 39) = ' + str(P_S3_m39) , '\nE(S3 | S3 > 39) = ' + str(E_S3_m39))

#theoritical expectation and variance

E = S0 * p.exp(mu*period)
Var = (S0**2)*(np.exp(2*mu*period))*(np.exp(sigma*sigma*period)-1)
print('E = ' + str(E) , '\nVar = ' + str(Var))
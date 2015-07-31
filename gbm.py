import pylab as p
import numpy as np

# dSt = mu * S0 * dt + sigma * S0 * dBt

#Defining parameters

mu = 0.1;
sigma = 0.26;
S0 = 39;
n_path = 1000; #number of simulations
n = 1000 ;     #number of partitiions on time 3
time = 3.0;

#Generating Brownian Motion

t = p.linspace(0,time,n+1)
dB = p.randn(n_path,n+1) / p.sqrt(n/time) ; dB[:,0] = 0 #1st column of dB = 0
B = dB.cumsum(axis = 1) #cumulative sum over columns for each row

#Calculate stock prices

nu = mu - sigma * sigma / 2.0
S = p.zeros_like(B) ; S[:,0] = S0
S[:,1:] = S0 * p.exp(nu * t[1:] + sigma * B[:,1:])
    #S has 1000 runs, each run has 1001 points

#Plotting 5 realizations of stock price GBM

run = 5
S_sample = S[0:run]             #5 runs of S is extracted
p.plot(t,S_sample.transpose());

#Plot labelling

label = 'Time , $t$' ; p.xlabel(label)
label = 'Stock prices, $S_t$;' ; p.ylabel(label)
p.title('GBM of ' + label + '\n with $\mu$ = ' + str(mu) + ' and $\sigma$ = ' + str(sigma))
p.show();

#Calculations

print('From data')
S3 = p.array(S[:,-1])
E_S3 = np.mean(S3)
Var_S3 = np.var(S3)
print('E(S3) = ' + str(E_S3) , '\nVar(S3) = ' + str(Var_S3))

mask = S3 > 39
P_S3 = sum(mask) / len(mask)
S3_39 = S3 * mask 
E_S3_39 = sum(S3_39) / sum(mask)
print('P(S3 > 39) = ' + str(P_S3) , '\nE(S3 | S3 > 39) = ' + str(E_S3_39))


print('\nTheoretical expectation and variance:')
E = S0 * p.exp(mu*time)
Var = (S0**2)*(np.exp(2*mu*time))*(np.exp(sigma*sigma*time)-1)
print('E(S3) = ' + str(E) , '\nVar(S3) = ' + str(Var))




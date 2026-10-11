import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def integrand_N(x):
    return np.exp(-x**2/2)/np.sqrt(2*np.pi)

def N(y):
    return quad(integrand_N, float('-inf'), y)[0]

def d1_d2(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return d1, d2

def bs_call(S, K, T, r, sigma):
    d1, d2 = d1_d2(S, K, T, r, sigma)
    return S*N(d1) - K*np.exp(-r*T)*N(d2)

def bs_put(S, K, T, r, sigma):
    d1, d2 = d1_d2(S, K, T, r, sigma)
    return K*np.exp(-r*T)*N(-d2) - S*N(-d1)

def put_call_parity(C, P, S, K, r, T):
    return C - P - S + K*np.exp(-r*T)

def call_payoff(S, K):
    return max(S - K, 0)

def put_payoff(S, K):
    return max(K - S, 0)

S, K, r, T, sigma = 100, 100, 0.05, 1, 0.2
print('Call: ', bs_call(S, K, T, r, sigma))
print('Put: ', bs_put(S, K, T, r, sigma))
print(bs_put(50, K, T, r, sigma), put_payoff(50, K))
print('K - Ke^(-rT): ', K - K*np.exp(-r*T))
print(put_call_parity(bs_call(S, K, T, r, sigma), bs_put(S, K, T, r, sigma), S, K, r, T))

callpayoff = []
putpayoff = []
bscall = []
bsput = []
S_values = []
for S in range(50, 151, 1):
    callpayoff.append(call_payoff(S, K))
    putpayoff.append(put_payoff(S, K))
    bscall.append(bs_call(S, K, T, r, sigma))
    bsput.append(bs_put(S, K, T, r, sigma))
    S_values.append(S)


plt.plot(S_values, callpayoff, color= 'g', label= 'call payoff')
plt.plot(S_values, putpayoff, color= 'b', label= 'put payoff')
plt.plot(S_values, bscall, color= 'r', label= 'call')
plt.plot(S_values, bsput, color= 'k', label= 'put')
plt.xlabel('Stock Prices')
plt.title('S = 100, K = 100, r = 0.05, T = 1, sigma (volatility) = 0.2')
plt.legend(loc= 'upper left')

plt.show()
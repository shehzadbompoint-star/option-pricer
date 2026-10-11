import math
import numpy as np
from scipy.integrate import quad
rng = np.random.default_rng()

def mc_call(S, K, T, r, sigma, N):
    Z = rng.standard_normal(N)
    payoff = []
    for i in Z:
        payoff.append(max(S * np.exp((r - (sigma**2)/2)*T + sigma*np.sqrt(T)*i) - K, 0))
    return np.mean(payoff)*np.exp(-r*T)

print(f'{'N': <10}{'call price'}')
for N in [1_000, 100_000, 1_000_000]:
    print(f'{N: <10}{mc_call(100, 100, 1, 0.05, 0.2, N): >15.4f}')

def mc_call_vec(S, K, T, r, sigma, N):
    Z = rng.standard_normal(N)
    ST = S * np.exp((r - (sigma**2)/2)*T + sigma*np.sqrt(T)*Z)
    return np.mean(np.maximum(ST - K, 0))*np.exp(-r*T)

import time
start = time.perf_counter()
price = mc_call(100, 100, 1, 0.05, 0.2, 1_000_000)
print(time.perf_counter() - start, 'seconds')
start = time.perf_counter()
price = mc_call_vec(100, 100, 1, 0.05, 0.2, 1_000_000)
print(time.perf_counter() - start, 'seconds')
print(price)


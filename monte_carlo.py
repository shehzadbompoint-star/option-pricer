import numpy as np
rng = np.random.default_rng()

def mc_call(S, K, T, r, sigma, N):
    Z = rng.standard_normal(N)
    payoff = []
    for i in Z:
        payoff.append(max(S * np.exp((r - (sigma**2)/2)*T + sigma*np.sqrt(T)*i) - K, 0))
    return np.mean(payoff)*np.exp(-r*T)

def mc_call_vec(S, K, T, r, sigma, N):
    Z = rng.standard_normal(N)
    ST = S * np.exp((r - (sigma**2)/2)*T + sigma*np.sqrt(T)*Z)
    payoff = np.maximum(ST - K, 0)*np.exp(-r*T)
    price = np.mean(payoff)
    se = np.std(payoff)/np.sqrt(N)
    return price, se

print(f'{'N': <10}{'price': <10}{'se': <10}{'lower': <10}{'upper': <10}')
for N in [1_000, 100_000, 1_000_000]:
    #print(f'{N: <10}{mc_call(100, 100, 1, 0.05, 0.2, N): >15.4f}')
    price, se = mc_call_vec(100, 100, 1, 0.05, 0.2, N)
    lower = price - 1.96 * se
    upper = price + 1.96 * se
    print(f'{N: <10}{price: <10.4f}{se: <10.4f}{lower: <10.4f}{upper: <10.4f}')

import time
start = time.perf_counter()
price = mc_call(100, 100, 1, 0.05, 0.2, 1_000_000)
print(time.perf_counter() - start, 'seconds for looping through payoffs')
start = time.perf_counter()
price, se = mc_call_vec(100, 100, 1, 0.05, 0.2, 1_000_000)
print(time.perf_counter() - start, 'seconds for calculating through an array')
print(price, se)


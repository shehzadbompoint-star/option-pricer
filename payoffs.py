import matplotlib.pyplot as plt

def call_payoff(S, K):
    return  max(S - K, 0)

def put_payoff(S, K):
    return  max(K - S, 0)

cost = 8
print(f'{'S': <6}{'call': <8}{'put': <8}{'Straddle Profit': <12}')
for S in range(80, 130, 10):
     print(f'{S: <6}{call_payoff(S, 100): <8}{put_payoff(S, 100): <8}{put_payoff(S, 100) + call_payoff(S, 100) - cost: <12}')

S_values = []
straddle = []
call = []
put = []
for S in range(50, 151, 1):
    S_values.append(S)
    call.append(call_payoff(S, 100))
    put.append(put_payoff(S, 100))
    straddle.append(call_payoff(S, 100) + put_payoff(S, 100) - cost)

plt.plot(S_values, straddle, color= 'g', label= 'straddle profit')
plt.plot(S_values, call, color='k', label= 'call')
plt.plot(S_values, put, color='r', label= 'put')
plt.xlabel('Stock Prices')
plt.ylabel('Straddle Profit')
plt.title('Straddle Profit')
plt.grid(True)

plt.legend(loc= 'upper left')

plt.show()
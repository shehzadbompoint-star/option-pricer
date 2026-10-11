import numpy as np
rng = np.random.default_rng()

def average_dice_roll():
    lst = [10, 100, 1000, 10_000, 1_000_000]
    print(f'{'N': <6}{'average': >13}')
    for N in range(len(lst)):
        print(f'{lst[N]: <6}{sum(rng.integers(low=1, high=7, size = lst[N]))/lst[N]: >13}')

average_dice_roll()
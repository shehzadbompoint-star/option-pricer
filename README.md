# Option Pricer

An option pricing engine I'm building from scratch in Python while learning to code, alongside my Financial Mathematics degree. The goal is a small pricing and risk library: Black-Scholes, Monte Carlo, binomial trees and Greeks, with a C++ core later on.

## What's in it so far

| File | What it does |
| --- | --- |
| `payoffs.py` | Call and put payoffs at expiry, plus a straddle profit chart (break-evens and maximum loss) |
| `black_scholes.py` | Black-Scholes call and put prices, using my own normal CDF built by numerically integrating the normal density (`scipy.integrate.quad`); a put-call parity check; a chart of prices against payoffs |
| `monte_carlo.py` | Monte Carlo pricer for a European call: a loop version and a vectorised NumPy version, with standard errors and 95% confidence intervals |
| `monte_carlo_dice.py` | Warm-up: estimating the average dice roll by simulation |

## Results

Test option: S = 100, K = 100, T = 1 year, r = 5%, σ = 20%.

**Black-Scholes**

| | Price |
| --- | --- |
| Call | 10.4506 |
| Put | 5.5735 |

Put-call parity (C − P = S − Ke^(−rT)) holds to about 1e-14, i.e. rounding error.

**Monte Carlo vs Black-Scholes (call)**

| Paths (N) | MC price | Standard error | 95% confidence interval |
| --- | --- | --- | --- |
| 1,000 | 10.7846 | 0.4605 | 9.8820 to 11.6872 |
| 100,000 | 10.4876 | 0.0467 | 10.3961 to 10.5790 |
| 1,000,000 | 10.4508 | 0.0147 | 10.4220 to 10.4796 |

Every interval contains the Black-Scholes price, and the interval narrows by about 10× for every 100× more paths, as the 1/√N convergence rate predicts.

**Speed: loop vs vectorised (1,000,000 paths, MacBook)**

| Version | Time |
| --- | --- |
| Python loop | ~0.63 s |
| NumPy vectorised | ~0.013 s |

Vectorising with NumPy made the simulation about **48× faster** for the same maths.

## Things I found along the way

- **A deep in-the-money European put can be worth less than its payoff.** At S = 50 the Black-Scholes put is worth about 45.12, while exercising would pay 50. The gap is roughly K(1 − e^(−rT)) ≈ 4.88, because a European put only pays the strike at expiry. Setting r = 0 makes the gap disappear. This is why the right to exercise early gives American puts extra value, while an American call on a non-dividend-paying stock is worth the same as a European one.
- **Testing needs two kinds of check.** Put-call parity passed even when I accidentally swapped r and T, so I also check against known textbook prices.

## How to run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python black_scholes.py
python monte_carlo.py
```

## Next steps

- Verify the confidence intervals empirically (do about 95% of them contain the true price?)
- Convergence chart: Monte Carlo price against N, with the Black-Scholes price and confidence band
- Binomial tree to price American options
- Greeks (delta, gamma, vega) by formula and by finite differences
- Rewrite the pricing core in C++ and call it from Python

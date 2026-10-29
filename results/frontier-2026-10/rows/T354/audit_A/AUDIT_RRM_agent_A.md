# Audit 2 of the large-n rows (agent_B/rrm_runs.txt, NOTE "Every n")

agent A, 20 Oct 2026 08:3x. Method: Monte Carlo of the reshuffled stream itself, with no elementary-symmetric recursion and no
spline. It is independent of rr_exact_m2.py and of audit 1's rrm_indep.py, which share that recursion.

Verdict: CONFIRMED. Every published row agrees with the simulation within its error bar. The three rows that read 1.2-1.6 se low on seed 7
come back within 0.1 se on seed 8 at four times the epochs.

## Method (rrm_mc_cv.py)

Model as in the NOTE: n slots per epoch, m = n/10 with b = 9, the rest b = -1, g = x + b, beta1 = 0, eps = 0. Each chain draws a
uniform m-subset per epoch and runs v_k = beta2 v_{k-1} + d g_k^2. The script subtracts the exact first-order control variate
g/sqrt(V) - g (v - V)/(2 V^1.5), whose mean is known in closed form (the lag sum in the script's docstring), and simulates only the
O(eta^2) remainder. It runs 4000 independent chains. The burn-in is ceil(35/(n d)) + 1 epochs, so beta2^(burn n) < e^-35. The root comes
from a quadratic through three x near x0 with common random numbers; a linear fit was 7 se off on the n 10 row and was replaced. The error
bar is the spread of the chain means.

## Rows

| n | beta2 | n d | MC seed 7 | MC seed 8, 4x epochs | rrm_runs.txt | MC - published |
|---|---|---|---|---|---|---|
| 10 | 0.99 | 0.1 | -1.2472 +- 0.0000 | | -1.24726 | 0 |
| 50 | 0.998 | 0.1 | -1.2107 +- 0.0001 | | -1.21075 | 0 |
| 100 | 0.99 | 1 | -0.6499 +- 0.0014 | | -0.64860 | -0.9 se |
| 500 | 0.998 | 1 | -0.5985 +- 0.0022 | | -0.59995 | +0.7 se |
| 200 | 0.99 | 2 | -0.2147 +- 0.0030 | | -0.21742 | +0.9 se |
| 500 | 0.99 | 5 | 0.3239 +- 0.0056 | 0.3329 +- 0.0028 | 0.33265 | -1.6 se / +0.1 se |
| 1000 | 0.995 | 5 | 0.3616 +- 0.0038 | | 0.35757 | +1.1 se |
| 2500 | 0.998 | 5 | 0.3752 +- 0.0082 | | 0.37156 | +0.4 se |
| 1000 | 0.98 | 20 | 0.7414 +- 0.0078 | 0.7503 +- 0.0039 | 0.75054 | -1.2 se / -0.1 se |
| 2000 | 0.99 | 20 | 0.7778 +- 0.0091 | 0.7917 +- 0.0046 | 0.79207 | -1.6 se / -0.1 se |
| 2500 | 0.98 | 50 | 0.8577 +- 0.0055 | | (none) | |

The column is (x*/x0 - 1)/d. Over the 10 published rows on seed 7 the squared deviations in se units sum to about 10; on seed 8 the three
reruns are 0.1 se or less. K_rr from the script's own lag sum matches every K printed in rrm_runs.txt to 8 digits.

The n 2500, beta2 0.98 row (n d 50) has no published counterpart. It is a single d = 0.02 root, outside the linear range in d that audit 1
identified, so 0.858 is not c(50). It is only consistent with c rising toward 1 at large n d.

Files (this directory): rrm_mc_cv.py, rrmc_batch.sh, rrmc_s8.sh, rrmc_out/*.txt.

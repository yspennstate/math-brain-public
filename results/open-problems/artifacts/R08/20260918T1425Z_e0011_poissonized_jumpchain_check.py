#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, comb, log10, lgamma, log

# Frozen data from the already checked R08 E0011 two-child block.
M = 432
N_CO = 328
N_O2 = 104
assert N_CO + N_O2 == M
K = (2**24) * comb(20,10)
assert K == 3099691319296
q_erase = Fraction(35,486)
q_exp = Fraction(1,72)

# Protected global block: 144 site clocks at 1/2 and 314 O2-edge clocks at 1/4.
Lambda = Fraction(144,2) + Fraction(314,4)
assert Lambda == Fraction(301,2)
T = Fraction(M,1) / Lambda
assert T == Fraction(864,301)
assert Lambda*T == M

# Conditional identity probabilities given a protected mark.
p_CO_label = Fraction(1,2) / Lambda
p_O2_label = Fraction(1,4) / Lambda
assert p_CO_label == Fraction(1,301)
assert p_O2_label == Fraction(1,602)

# Exact rational lower bound e^{-1} > 32/87 from the previous run's proof e < 87/32.
e_inv_lower = Fraction(32,87)

# Previous slot lower bound: one protected mark in each of M equal slots.
b1 = Fraction(K,1) * q_erase * (q_exp**20) * (e_inv_lower**M) * (p_CO_label**N_CO) * (p_O2_label**N_O2)

# New event: only require exactly M protected marks on [0,T], and require their ordered labels
# to be one of the K successful histories. Since Lambda*T=M,
# P(N(T)=M)=e^{-M} M^M/M! > (32/87)^M M^M/M!.
poisson_count_lower = (e_inv_lower**M) * Fraction(M**M, factorial(M))
b2 = Fraction(K,1) * q_erase * (q_exp**20) * poisson_count_lower * (p_CO_label**N_CO) * (p_O2_label**N_O2)

gain = Fraction(M**M, factorial(M))
assert gain > 1
assert b2 == b1 * gain
assert b2 > b1

# Exact elementary proof gain>1, independent of floating point:
# M! = product_{j=1}^M j < product_{j=1}^M M = M^M for M>1.
assert M > 1

# Approximate scales are diagnostics only; exact claims are the Fractions above.
log10_gain = M*log10(M) - lgamma(M+1)/log(10)
log10_b1 = (log10(K) + log10(35/486) + 20*log10(1/72)
            + M*log10(32/87) - N_CO*log10(301) - N_O2*log10(602))
log10_b2 = log10_b1 + log10_gain

print('PASS exact R08/E0011 Poissonized embedded-chain improvement')
print(f'M={M}')
print(f'Lambda={Lambda}')
print(f'T={T}')
print(f'Lambda*T={Lambda*T}')
print(f'K={K}')
print(f'p_CO_label={p_CO_label}')
print(f'p_O2_label={p_O2_label}')
print('b1=K*(35/486)*(1/72)^20*(32/87)^432*(1/301)^328*(1/602)^104')
print('b2=b1*(432^432/432!)')
print(f'gain_exact_gt_1={gain > 1}')
print(f'b2_gt_b1={b2 > b1}')
print(f'log10_gain_approx={log10_gain:.12f}')
print(f'log10_b1_approx={log10_b1:.12f}')
print(f'log10_b2_approx={log10_b2:.12f}')

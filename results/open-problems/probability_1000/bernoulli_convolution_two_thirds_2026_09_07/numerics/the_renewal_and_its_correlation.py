"""The tail obeys an EXACT renewal, and L^2 is one decorrelation statement.

Q(u) = prod_(j>=0) cos(pi (2/3)^j u) satisfies Q(u) = cos(pi u) Q(2u/3), so with u = (3/2) v,
    Q((3/2) v) = cos(3 pi v / 2) Q(v)      exactly,
hence for every M
    int_M^inf Q^2 du = (3/2) int_(2M/3)^inf cos^2(3 pi v/2) Q(v)^2 dv.
If cos^2(3 pi v/2) decorrelated from Q(v)^2 it would contribute its mean 1/2 and the energy would fall by
3/4 per (3/2)-step, giving exponent log(4/3)/log(3/2) = 0.7095. So measure, block by block on the ladder
N_n = (3/2)^n:
    block(N)  = int_N^(3N/2) Q^2
    corr(N)   = int_N^(3N/2) cos^2(3 pi v/2) Q^2 / ( (1/2) int_N^(3N/2) Q^2 )   -> 1 if decorrelated
    ratio(N)  = block(3N/2) / block(N)                                          -> 3/4 if decorrelated
A corr persistently above 1 by a definite margin is what would stall the decay - that is the phase
question, in the one place it can be watched directly over many scales.
"""
import numpy as np

PTS = 300
def blocks(N):
    n = max(4000, int((N/2) * PTS))
    v = N + (np.arange(n) + 0.5) * (N/2) / n
    q = np.ones(n)
    j = 0
    while True:
        a = (2.0/3.0) ** j * v
        q *= np.cos(np.pi * a)
        j += 1
        if a.max() < 1e-9:
            break
    q2 = q * q
    w = (N/2) / n
    b = q2.sum() * w
    cc = (np.cos(1.5 * np.pi * v) ** 2 * q2).sum() * w
    return b, cc

print(f"{'n':>3} {'N=(3/2)^n':>12} {'block':>12} {'ratio':>9} {'corr':>9} {'implied exp':>12}")
prev = None
for n in range(6, 34):
    N = 1.5 ** n
    b, cc = blocks(N)
    corr = cc / (0.5 * b) if b > 0 else float('nan')
    if prev is None:
        print(f"{n:>3} {N:>12.1f} {b:>12.3e} {'-':>9} {corr:>9.4f} {'-':>12}")
    else:
        r = b / prev
        exp = -np.log(r) / np.log(1.5)
        print(f"{n:>3} {N:>12.1f} {b:>12.3e} {r:>9.4f} {corr:>9.4f} {exp:>12.4f}")
    prev = b
print()
print("decorrelated prediction: ratio 0.7500, corr 1.0000, exponent 0.7095")

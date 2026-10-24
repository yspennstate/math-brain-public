"""Targeted falsification check for the exact scalar-frontier endpoint.

Search all Boolean functions through n=4 for a nonconstant Fourier law whose
support is downward closed and whose nonzero squared masses have one common
activity ratio lambda in (0,1): p_S = p_empty * lambda**|S| on the support.
This is not an FEI sweep and is not used as the proof of any universal claim.
"""

import numpy as np


def walsh(vals, n):
    h = np.array(vals, dtype=np.int64)
    step = 1
    N = 1 << n
    while step < N:
        for base in range(0, N, 2 * step):
            x = h[base : base + step].copy()
            y = h[base + step : base + 2 * step].copy()
            h[base : base + step] = x + y
            h[base + step : base + 2 * step] = x - y
        step *= 2
    return h  # unnormalised integer Walsh coefficients


def downset(support):
    F = set(support)
    for S in support:
        bits = S
        while bits:
            b = bits & -bits
            if (S ^ b) not in F:
                return False
            bits -= b
    return True


def endpoint_activity(coeffs, n):
    support = [S for S, a in enumerate(coeffs) if a != 0]
    if not support or 0 not in support or not downset(support):
        return None
    relmask = 0
    for S in support:
        relmask |= S
    if relmask == 0:
        return None
    relevant = [i for i in range(n) if (relmask >> i) & 1]
    a0 = abs(int(coeffs[0]))
    singleton = [abs(int(coeffs[1 << i])) for i in relevant]
    if any(x == 0 for x in singleton) or len(set(singleton)) != 1:
        return None
    # Compare exactly without floating point.  rho = singleton/a0.
    num = singleton[0]
    den = a0
    if num >= den:  # only the lambda=rho^2 in (0,1) endpoint is sought
        return None
    for S in support:
        k = S.bit_count()
        # |a_S| / |a_empty| = (num/den)^k
        if abs(int(coeffs[S])) * (den**k) != a0 * (num**k):
            return None
    return (num, den, support)


for n in range(1, 5):
    N = 1 << n
    hits = 0
    for truth_mask in range(1 << N):
        vals = [1 if ((truth_mask >> x) & 1) else -1 for x in range(N)]
        coeffs = walsh(vals, n)
        if endpoint_activity(coeffs, n) is not None:
            hits += 1
    print(n, hits)

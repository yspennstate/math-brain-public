"""Exhaustive discrepancy of the small Sylvester Hadamard matrices, to check the conjecture where it is
supposed to hold: disc(H_k) = sqrt(2)*sqrt(2^k) for odd k.  For k = 1 and 3 this is 2^((k+1)/2) = 2 and 4.
Also k = 2 and 4, where the answer should be sqrt(2^k) = 2 and 4 (bent functions exist in even dimension).
"""
import numpy as np, itertools

def sylvester(k):
    H = np.array([[1]])
    for _ in range(k): H = np.block([[H, H], [H, -H]])
    return H

for k in (1, 2, 3, 4):
    n = 1 << k; H = sylvester(k)
    best = None
    for bits in itertools.product((1, -1), repeat=n):
        v = int(np.abs(H @ np.array(bits)).max())
        if best is None or v < best: best = v
    pred = 2 ** ((k + 1) // 2) * (1 if k % 2 else 1)
    conj = (2 ** ((k + 1) / 2)) if k % 2 else (2 ** (k / 2))
    print(f"k = {k}  n = {n:>3}  disc(H_k) = {best:>3}   "
          f"{'conjecture (odd k): ' if k%2 else 'even k, expect sqrt(n): '}{conj:g}   "
          f"{'agrees' if abs(best-conj) < 1e-9 else 'DISAGREES'}")

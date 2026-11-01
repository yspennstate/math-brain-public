"""Family constructors shared by the survey scripts (no side effects on import)."""
import os
import numpy as np
from feilib import bent_plus_flip, one_point, tribes, majority, rec_maj3, addressing

HERE = os.path.dirname(os.path.abspath(__file__))


def maj_plus_maxfalse_flip(n):
    """Monotone: Maj_n(y) OR (z AND y == y*), y* a maximal false point of Maj_n; y = coords 0..n-1, z = n."""
    N = 1 << (n + 1)
    ystar = (1 << ((n - 1) // 2)) - 1
    tt = np.empty(N, dtype=np.int8)
    for x in range(N):
        y = x & ((1 << n) - 1); z = (x >> n) & 1
        val = (bin(y).count("1") * 2 > n) or (z == 1 and y == ystar)
        tt[x] = -1 if val else 1
    return tt


def family_list(big=True):
    L = []
    for m2 in range(1, 7 if big else 5):
        L.append((f"bent_plus_flip m={2*m2}", bent_plus_flip(m2), 2 * m2 + 1))
    for n in ((3, 5, 7, 9, 11, 13, 15) if big else (3, 5, 7)):
        L.append((f"maj{n}+maxfalse_flip", maj_plus_maxfalse_flip(n), n + 1))
    for n in ((5, 9, 13, 17) if big else (5, 9)):
        L.append((f"maj{n}", majority(n), n))
    for n in ((4, 8, 12, 16) if big else (4, 8)):
        L.append((f"one_point{n}", one_point(n), n))
    for (w, s) in (((2, 3), (2, 5), (2, 8), (3, 4), (3, 6), (4, 4)) if big else ((2, 3), (3, 3))):
        L.append((f"tribes w{w} s{s}", tribes(w, s), w * s))
    L.append(("recmaj3 depth2", rec_maj3(2), 9))
    for k in ((2, 3, 4) if big else (2, 3)):
        L.append((f"addressing k{k}", addressing(k), k + (1 << k)))
    if big:
        g = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy"))
        L.append(("numaro18", g, 18))
    return L

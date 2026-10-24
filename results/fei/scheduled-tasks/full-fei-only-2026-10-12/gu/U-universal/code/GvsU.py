"""How much of G is explained by U?  max over f of (G - b U)/I for several b (EVIDENCE)."""
import numpy as np, json
from feilib import *
from upward import Uprime
from exhaust import scan
for n in [3, 4]:
    r = scan(n); nc = r['I'] > 0; T = r['T'][nc]; p = r['p'][nc]; I = r['I'][nc]; H = r['H'][nc]
    U = Uprime(p, n); Hd1 = hadamard(n - 1); N = 1 << n; G = np.zeros_like(U)
    for i in range(n):
        pp = ((restrict(T, n, i, 0) @ Hd1.T).astype(np.float64) / (N // 2)) ** 2
        pm = ((restrict(T, n, i, 1) @ Hd1.T).astype(np.float64) / (N // 2)) ** 2
        G += U - 0.5 * (Uprime(pp, n - 1) + Uprime(pm, n - 1))
    for b in [0.0, 0.5, 0.9, 1.0, 1.5]:
        print(n, 'b=', b, 'max (G - bU)/I =', round(float(((G - b * U) / I).max()), 4), ' max (G - bH)/I =', round(float(((G - b * H) / I).max()), 4))

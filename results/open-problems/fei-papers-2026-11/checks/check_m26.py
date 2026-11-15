import sys
from fractions import Fraction as Fr
from math import comb, exp
sys.path.insert(0, r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad")
from check_conj8 import det, jacobi
m = [Fr(1), Fr(1), Fr(8,3), Fr(11), Fr(908,15), Fr(415), Fr(23840,7),
     Fr(325719,10), Fr(112135066,315), Fr(3065263961,700),
     Fr(69174280444,1155), Fr(5680684105259,6300), Fr(1112571762134554,75075), Fr(2032842751996209,7700)]
K = 13
print("\n===== m_26 =", m[K], float(m[K]))
cat = [Fr(comb(2*k, k), k+1) for k in range(K+1)]
s = [m[k] / cat[k] for k in range(K+1)]
print("s_13 =", s[K])
mins = [det([[s[i+j+1] for j in range(n)] for i in range(n)]) for n in range(1, 8)]
print("(s_{i+j+1}) 7 minors positive:", all(x > 0 for x in mins))
b = jacobi(m, K)
print("increments:", [f"{float(b[i]-b[i-1]):.5f}" for i in range(1, K)])
kap = {}
for k in range(2, K+1):
    kap[k] = m[k] - cat[k] - sum(comb(2*k, k-q) * kap[q] for q in range(2, k))
print("kappa_13 =", kap[K], float(kap[K]), " kappa_13/(13 kappa_12) =", f"{float(kap[K]/(13*kap[12])):.4f}", "kappa13>0", kap[K] > 0)
a = {k: float(m[k] / kap[k]) for k in range(2, K+1)}
print("m/kappa:", [f"{a[k]:.4f}" for k in range(2, K+1)])
r1 = {k: (k+1)*a[k+1] - k*a[k] for k in range(2, K)}
print("Richardson 1 k=4..12:", [f"{r1[k]:.4f}" for k in range(4, K)])
print("e^(1/theta^2) =", exp(1/0.686981293), " last below by", f"{1 - r1[K-1]/exp(1/0.686981293):.4f}")

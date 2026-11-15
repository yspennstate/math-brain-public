import sys
from fractions import Fraction as Fr
from math import comb, exp
sys.path.insert(0, r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad")
from check_conj8 import det, jacobi  # reuses the tested helpers (prints its own report first)

m24 = Fr(sys.argv[1])
m = [Fr(1), Fr(1), Fr(8,3), Fr(11), Fr(908,15), Fr(415), Fr(23840,7),
     Fr(325719,10), Fr(112135066,315), Fr(3065263961,700),
     Fr(69174280444,1155), Fr(5680684105259,6300), m24]
print("\n===== with m_24 =", m24, "=", float(m24))
thr = Fr(533385290252268206796914811370716813306691285889, 36005162406403257088495500297206628000)
print("threshold", float(thr), " m24 - thr =", float(m24 - thr), " relative", float(m24/thr - 1))
print("order-24 test PASSES" if m24 >= thr else "order-24 test FAILS: gamma_T is not freely infinitely divisible")
cat = [Fr(comb(2*k, k), k+1) for k in range(13)]
s12 = m24 / cat[12]
print("mixing moment s_12 =", s12)
s = [m[k] / cat[k] for k in range(13)]
mins = [det([[s[i+j] for j in range(n)] for i in range(n)]) for n in range(1, 8)]
print("(s_{i+j}) 7x7 leading minors positive:", all(x > 0 for x in mins), f"{float(mins[-1]):.4e}")
b = jacobi(m, 12)
print("b_12^2 - b_11^2 =", f"{float(b[11]-b[10]):.5f}")
print("ratio m24/m22 =", f"{float(m24/m[11]):.4f}", " diff", f"{float(m24/m[11]) - float(m[11]/m[10]):.4f}")
kap = {}
for k in range(2, 13):
    kap[k] = m[k] - cat[k] - sum(comb(2*k, k-q) * kap[q] for q in range(2, k))
print("kappa_12 =", kap[12], " ratio kappa_12/(12 kappa_11) =", f"{float(kap[12]/(12*kap[11])):.4f}")
a = {k: float(m[k] / kap[k]) for k in range(2, 13)}
print("m/kappa:", [f"{a[k]:.4f}" for k in range(2, 13)])
r1 = {k: (k+1)*a[k+1] - k*a[k] for k in range(2, 12)}
print("Richardson 1:", [f"{r1[k]:.4f}" for k in range(4, 12)])
r2 = {k: ((k+1)**2*a[k+1] - 2*k**2*a[k] + (k-1)**2*a[k-1]) / 2 for k in range(3, 12)}
print("Richardson 2:", [f"{r2[k]:.4f}" for k in range(4, 12)])
print("e^(1/theta^2) =", exp(1/0.686981293))

from fractions import Fraction as Fr
from math import comb, exp, sqrt

m = [Fr(1), Fr(1), Fr(8,3), Fr(11), Fr(908,15), Fr(415), Fr(23840,7),
     Fr(325719,10), Fr(112135066,315), Fr(3065263961,700),
     Fr(69174280444,1155), Fr(5680684105259,6300)]   # m_{2k}, k=0..11
cat = [Fr(comb(2*k, k), k+1) for k in range(12)]
s = [m[k] / cat[k] for k in range(12)]
print("mixing moments s_1..s_11:", [str(x) for x in s[1:]])
paper = [Fr(1), Fr(4,3), Fr(11,5), Fr(454,105), Fr(415,42), Fr(5960,231), Fr(108573,1430),
         Fr(56067533,225225), Fr(3065263961,3403400), Fr(17293570111,4849845), Fr(298983373961,19492200)]
print("  match paper:", s[1:] == paper)

def det(M):
    M = [row[:] for row in M]; n = len(M); d = Fr(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None: return Fr(0)
        if p != i: M[i], M[p] = M[p], M[i]; d = -d
        d *= M[i][i]
        for r in range(i+1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n): M[r][c] -= f * M[i][c]
    return d

for sh in (0, 1):
    mins = [det([[s[i+j+sh] for j in range(n)] for i in range(n)]) for n in range(1, 7)]
    print(f"Hankel (s_(i+j+{sh})) leading minors positive:", all(x > 0 for x in mins), [f"{float(x):.3e}" for x in mins])

# Gamma(3, 1/3): E V^k = 3*4*...*(k+2) / 3^k
g = [Fr(1)]
for k in range(1, 4): g.append(g[-1] * (k + 2) / 3)
print("Gamma(3,1/3) moments:", [str(x) for x in g], " s:", [str(x) for x in s[:4]])

# Jacobi coefficients of the symmetric law from moments (Chebyshev / continued fraction)
def jacobi(mom2, K):
    # moments of all orders
    M = {}
    for k, v in enumerate(mom2): M[2*k] = v; M[2*k+1] = Fr(0)
    # Hankel determinants D_n = det(M_{i+j})_{0..n-1}
    D = [Fr(1)] + [det([[M[i+j] for j in range(n)] for i in range(n)]) for n in range(1, K+2)]
    return [D[n+1] * D[n-1] / D[n]**2 for n in range(1, K+1)]
b = jacobi(m, 11)
print("b_k^2:", [str(x) for x in b[:4]], "...")
inc = [float(b[i+1] - b[i]) for i in range(len(b)-1)]
print("increments:", [f"{x:.5f}" for x in inc])

r = [float(m[k+1] / m[k]) for k in range(11)]
print("growth ratios:", [f"{x:.4f}" for x in r])
d = [r[i+1] - r[i] for i in range(10)]
print("differences of ratios:", [f"{x:.4f}" for x in d])
nxt = r[-1] + d[-1]
nxt2 = r[-1] + d[-1] + (d[-1] - d[-2])
thr = Fr(533385290252268206796914811370716813306691285889, 36005162406403257088495500297206628000)
for nx in (nxt, nxt2):
    e = float(m[11]) * nx
    print(f"next ratio {nx:.4f} -> m24 ~ {e:.5e}, margin {100*(e/float(thr)-1):.4f}%  (1 in {1/(e/float(thr)-1):.0f})")

kap = {}
for k in range(2, 12):
    kap[k] = m[k] - cat[k] - sum(comb(2*k, k-q) * kap[q] for q in range(2, k))
print("kappa_4 =", kap[4], " kappa_4^2 =", kap[4]**2, " kappa_8 =", kap[8])
kr = [float(kap[q+1] / ((q+1) * kap[q])) for q in range(2, 11)]
print("kappa_{r+1}/((r+1)kappa_r) r=2..10:", [f"{x:.4f}" for x in kr])
mk = [float(m[k] / kap[k]) for k in range(2, 12)]
print("m_2k/kappa_k k=2..11:", [f"{x:.4f}" for x in mk])
rich = [(k+1) * mk[k-1] - k * mk[k-2] for k in range(3, 10)]   # A_k = (k+1)a_{k+1} - k a_k, indices k>=2
print("Richardson (1/k):", [f"{x:.4f}" for x in rich])
th2 = 0.686981293
print("2theta^2 =", 2*th2, " e^(1/theta^2) =", exp(1/th2), " theta =", sqrt(th2))

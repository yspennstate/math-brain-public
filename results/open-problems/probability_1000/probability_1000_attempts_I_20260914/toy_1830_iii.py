"""Toy exact check that conditioning on S_n = m can KILL a common scale (Janson 18.7(iii) failure mechanism):
bulk atoms {0,1,2}; common scale C at L_C with n p_C = N; rare atom A at L_A = shift + N L_C with n p_A = delta;
rarer atom B at L_B = shift/eps with n p_B = eps (its mean shift is 'shift'). m = round(n nu).
We compute P(#C-boxes = k | S_n = m) exactly by convolution, splitting the law into C-part and the rest."""
import numpy as np
from math import comb
def power(p, Nn, L):
    res = np.zeros(L + 1); res[0] = 1.0; base = p[:L + 1].copy()
    while Nn:
        if Nn & 1: res = np.convolve(res, base)[:L + 1]
        Nn >>= 1
        if Nn: base = np.convolve(base, base)[:L + 1]
    return res
n = 4000; LC = 40; N = 6; eps = 0.05; delta = 0.05
import sys
LC = int(sys.argv[1]) if len(sys.argv) > 1 else LC
shift = 10 * N * LC; LB = int(round(shift / eps)); LA = int(round((shift + N * LC) / (1 - delta)))
pC = N / n; pA = delta / n; pB = eps / n; a = float(sys.argv[2]) if len(sys.argv) > 2 else 0.25; b = float(sys.argv[3]) if len(sys.argv) > 3 else 0.25
p = np.zeros(LB + 1); p[0] = 1 - a - b - pC - pA - pB; p[1] = a; p[2] = b; p[LC] += pC; p[LA] += pA; p[LB] += pB
nu = (np.arange(LB + 1) * p).sum(); m = int(round(nu * n))
tot = power(p, n, m)[m]
# law without any C atoms: q = p with C removed (renormalised), n summands, times P(no C) = (1-pC)^n ... exact: split by number of C-boxes k
q = p.copy(); q[LC] -= pC; q = q / q.sum()
res = []
for k in range(0, 4):
    # exactly k boxes of type C: C(n,k) pC^k (1-pC)^(n-k) * P(sum of n-k non-C summands = m - k LC)
    Pnk = power(q, n - k, m)
    val = comb(n, k) * pC ** k * (1 - pC) ** (n - k) * (Pnk[m - k * LC] if m - k * LC >= 0 else 0.0)
    res.append(val / tot)
print(f"n={n} LC={LC} N={N} LA={LA} LB={LB} shift={shift} m={m} nu={nu:.4f}")
print("P(#C = k | S_n = m) for k = 0..3:", [f"{v:.4f}" for v in res], "   unconditional P(#C=0) =", f"{(1-pC)**n:.4f}", " E#C =", N)
# and does the A atom appear?  P(exactly one A | S=m):
qA = p.copy(); qA[LA] -= pA; qA = qA / qA.sum()
PA1 = n * pA * (1 - pA) ** (n - 1) * power(qA, n - 1, m)[m - LA] / tot
print("P(exactly one A box | S_n = m) =", f"{PA1:.4f}", "  n P(xi >= LC) =", f"{n * (pC + pA + pB):.3f}")

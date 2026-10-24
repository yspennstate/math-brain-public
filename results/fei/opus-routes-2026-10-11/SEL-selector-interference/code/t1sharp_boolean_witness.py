"""Boolean counterexample search for T1-sharp from the beta->1 analysis: leaves G1 (code 2831), G2 (code 16)
on 4 data bits (pairwise orthogonal, overlapping Fourier supports); cells A_2 = one point of an r-bit selector
cube, A_1 = the rest.  gap = H(F) - [H(p) + sum_k p_k (H(q_k) + H(G_k))], exact Walsh integers, interval logs."""
import numpy as np
import mpmath
from fei_lib import fwht_int, entropy_from_W, H_interval
iv = mpmath.iv; iv.dps = 50
def table(code, n): return np.array([1 - 2*((code >> i) & 1) for i in range(1 << n)], dtype=np.int64)
G1 = table(2831, 4); G2 = table(16, 4)
print('E[G1]=', G1.mean(), 'E[G2]=', G2.mean(), 'E[G1 G2]=', np.mean(G1*G2))
W1, W2 = fwht_int(G1), fwht_int(G2)
print('G1hat*16:', W1.tolist()); print('G2hat*16:', W2.tolist())
def Hprob_interval(masses):  # masses: list of (numerator, denominator) exact rationals as Fractions
    tot = iv.mpf(0)
    for m in masses:
        if m == 0: continue
        mm = iv.mpf(m.numerator) / m.denominator
        tot += -mm * iv.log(mm) / iv.log(2)
    return tot
from fractions import Fraction
for r in range(1, 15):
    N = 1 << r
    lab = np.zeros(N, dtype=np.int64); lab[0] = 1          # cell 2 = the point x = (1,...,1)
    B = np.array([G1 if lab[b] == 0 else G2 for b in range(N)])
    F = B.T.reshape(-1)
    WF = fwht_int(F)
    HF = H_interval(WF, r + 4)
    # RHS exactly: p = (1-2^-r, 2^-r); q_k from the cell indicator spectra
    p2 = Fraction(1, N); p1 = 1 - p2
    a2 = fwht_int(np.where(lab == 1, -1, 1))   # +-1 version h of cell-2 indicator: a2 = (1-h)/2
    # ahat_2(S) = (delta_{S,empty} - hhat(S))/2 ; hhat = W/N
    hh = [Fraction(int(w), N) for w in a2]
    a2hat = [((1 if S == 0 else 0) - hh[S]) / 2 for S in range(N)]
    a1hat = [((1 if S == 0 else 0) + hh[S]) / 2 for S in range(N)]
    q1 = [x*x / p1 for x in a1hat]; q2 = [x*x / p2 for x in a2hat]
    HG1 = H_interval(W1, 4); HG2 = H_interval(W2, 4)
    rhs = Hprob_interval([p1, p2]) + iv.mpf(p1.numerator)/p1.denominator*(Hprob_interval(q1) + HG1) + iv.mpf(p2.numerator)/p2.denominator*(Hprob_interval(q2) + HG2)
    gap = HF - rhs
    print('r=%2d p2=2^-%d  gap interval = [%s, %s]   gap/p2 ~ %.5f' % (r, r, mpmath.nstr(gap.a, 8), mpmath.nstr(gap.b, 8), float(gap.a) * N), flush=True)

"""First-order structure of g at the centre, one biased input at a time.

With only input i biased (mean mu), a_T = ghat(T), b_T = ghat(T u i), T not containing i:
  sum_j It_j/V_j = I(g) + 2 mu S_i,           S_i = sum_{T not ni i} |T| a_T b_T,
  Htilde(mu) = sum_T phi((a_T + mu b_T)^2) + sum_T phi((1 - mu^2) b_T^2),
  dHtilde/dmu(0) = 2 sum_T a_T b_T log2(1/a_T^2)   (sum_T a_T b_T = E[x_i g^2]/2 = 0).
Also prints the exact class structure (distinct (a,b) pairs with multiplicity).
"""
import numpy as np
from collections import Counter
from gate import load_table, biased_spectrum, N

t = load_table()
c = biased_spectrum(t, [0.5] * N)
W = np.rint(c * (1 << N)).astype(np.int64)
idx = np.arange(1 << N)
pc = np.array([bin(x).count("1") for x in range(1 << N)], dtype=np.int64)
C = 6.521845710923047
print("distinct |Walsh numerators|:", sorted(Counter(np.abs(W[W != 0])).items()))
for i in list(range(N)):
    T = idx[(idx >> i) & 1 == 0]
    a = W[T] / 2.0 ** N
    b = W[T | (1 << i)] / 2.0 ** N
    S = float((pc[T] * a * b).sum())
    nz = a != 0
    dH = 2 * float((a[nz] * b[nz] * np.log2(1 / a[nz] ** 2)).sum())
    ab0 = float((a * b).sum())
    Lmu = 2 * C * S - dH            # d/dmu of [C sum It/V - Htilde]
    Lt = -2 * Lmu                   # d/dt, t = p - 1/2
    ci = W[1 << i] / 2.0 ** N
    zero_a = float((b[~nz] ** 2).sum())
    print("i=%2d  ghat_i=%.6f  S=%+.6e  dHt/dmu=%+.6e  sum ab=%+.1e  L_t=%+.6f  L_t/c_i=%+.4f   mass(b: a=0)=%.6f of Inf %.6f"
          % (i, ci, S, dH, ab0, Lt, Lt / ci, zero_a, float((b ** 2).sum())))

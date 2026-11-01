# Which Boolean f on n<=4 inputs have a product spectral law (DTC = 0 exactly), and what are their marginals?
import json, math
import numpy as np
from fractions import Fraction
def popc(x): return bin(int(x)).count("1")
res = {}
for n in range(1, 5):
    N = 1 << n; N2 = N * N; S = np.arange(N)
    Mx = np.array([[(-1) ** popc(s & x) for x in S] for s in S], dtype=np.int64)
    T = np.arange(1 << N, dtype=np.int64)
    F = 1 - 2 * ((T[:, None] >> S[None, :]) & 1)
    c = (F @ Mx.T) ** 2
    # exact product test: p(S) = prod_i q_i^{s_i} (1-q_i)^{1-s_i} with q_i = Inf_i, checked in integers
    infl = np.stack([c[:, (S >> i) & 1 == 1].sum(1) for i in range(n)], 1)      # N2 * Inf_i
    prod_ok = np.ones(len(T), bool)
    for s in range(N):
        num = np.ones(len(T), dtype=object)
        for i in range(n):
            num = num * (infl[:, i] if (s >> i) & 1 else (N2 - infl[:, i])).astype(object)
        prod_ok &= (c[:, s].astype(object) * N2 ** (n - 1) == num)                # p(S)*N2^n == prod (N2 q or N2(1-q))
    idx = np.nonzero(prod_ok)[0]
    marg = sorted({Fraction(int(v), N2) for v in infl[idx].ravel()})
    res[n] = {"product_law_functions": int(len(idx)), "distinct_marginals": [str(m) for m in marg]}
print(json.dumps(res))
json.dump(res, open("out/product_laws_n1_4.json", "w", encoding="utf-8"), indent=1)

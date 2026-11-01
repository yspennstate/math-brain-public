# rho* = sup over |l + beta| <= 1 of the density of L, for the comb laws of Section 13 on the second rotation, from a
# histogram of L with bins of width b; two bin widths and two halves of the samples show the estimator's noise.
import sys, math
import numpy as np
from adapted_hub import frame, sample

def rho_star(N, law="int", n=8_000_000, chunk=1_000_000, beta=0.0, seed=3):
    E = frame("irr2"); w = E[:, 0]
    rng = np.random.default_rng(seed)
    out = {}
    Ls = []
    for _ in range(n // chunk):
        X = sample(rng, law, N, (chunk, 8)); Ls.append(X @ w)
    L = np.concatenate(Ls)
    c = -beta if law != "int" else float(np.mean(L))   # combs at the integers are centred at E L, use beta = -E L
    for b in (0.02, 0.05):
        for tag, LL in (("all", L), ("half", L[: len(L) // 2])):
            h, _ = np.histogram(LL, bins=int(round(2 / b)), range=(c - 1, c + 1))
            out[(b, tag)] = h.max() / (len(LL) * b)
    return out, float(np.std(L))

if __name__ == "__main__":
    for N in [int(x) for x in sys.argv[1].split(",")]:
        o, sd = rho_star(N)
        print("int N=%3d  sd(L) %.3f  rho* bin0.02 %.4f (half %.4f)  bin0.05 %.4f (half %.4f)  N*rho* %.2f"
              % (N, sd, o[(0.02, "all")], o[(0.02, "half")], o[(0.05, "all")], o[(0.05, "half")], N * o[(0.05, "all")]), flush=True)

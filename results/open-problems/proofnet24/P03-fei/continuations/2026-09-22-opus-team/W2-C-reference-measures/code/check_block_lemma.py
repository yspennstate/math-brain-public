"""Numerical check of the block-restriction information lemma:
   I(z_R ; S cap J) = H(law of S cap J) - E_z H(f_{J|z}) <= (2/ln 2) * sum_{t in R} Inf_t(f),
and of the identity H(f) = E_z H(f_{J|z}) + I(z_R; S_J) + H(S_R | S_J)."""
import itertools, math
import numpy as np
import wlib as W
W.set_polite()
rng = np.random.default_rng(41)
C = 2 / math.log(2)
worst = 0.0; worst_id = 0.0; cnt = 0

def restr_H(tt, n, R, z):
    # f with coordinates in R fixed to bits z (bit=1 -> x=-1); returns spectrum entropy of the restriction on J
    N = 1 << n
    x = np.arange(N)
    ok = np.ones(N, dtype=bool)
    for t, b in zip(R, z):
        ok &= ((x >> t) & 1) == b
    J = [j for j in range(n) if j not in R]
    sub = tt[ok]  # ordered by x, the free bits in increasing order give the sub-index
    return W.H_of(W.spectrum(sub))

def check(tt, n, R):
    global worst, worst_id, cnt
    p = W.spectrum(tt); H = W.H_of(p); inf = W.influences(p, n)
    N = 1 << n; S = np.arange(N)
    Rm = sum(1 << t for t in R)
    SJ = S & ~Rm
    lawJ = np.bincount(SJ, weights=p, minlength=N)
    HJ = W.H_of(lawJ)
    EHz = np.mean([restr_H(tt, n, R, z) for z in itertools.product((0, 1), repeat=len(R))])
    info = HJ - EHz
    HRgJ = H - HJ
    bound = C * inf[list(R)].sum()
    cnt += 1
    if bound > 1e-12:
        worst = max(worst, info / bound)
    worst_id = max(worst_id, abs(H - (EHz + info + HRgJ)))
    return info, bound

# exhaustive n = 3, all blocks
for code in range(256):
    tt = np.array([1 - 2 * ((code >> k) & 1) for k in range(8)], dtype=np.int8)
    for r in (1, 2, 3):
        for R in itertools.combinations(range(3), r):
            check(tt, 3, list(R))
print(f"exhaustive n=3 (all functions, all blocks): max info/bound = {worst:.4f} over {cnt} cases")
for n in (4, 5, 6, 7, 8):
    for trial in range(60):
        if trial % 3 == 0:
            tt = rng.choice(np.array([-1, 1], dtype=np.int8), size=1 << n)
        elif trial % 3 == 1:
            tt = np.where(rng.uniform(size=1 << n) < rng.uniform(0.02, 0.3), -1, 1).astype(np.int8)
        else:
            tt = W.fam_ltf(rng.normal(size=n), rng.normal() * 0.5)
        r = rng.integers(1, n)
        R = sorted(rng.choice(n, size=r, replace=False).tolist())
        check(tt, n, R)
    print(f"n={n}: max info/bound so far = {worst:.4f}  (identity error {worst_id:.2e}, {cnt} cases)", flush=True)
# structured: the address bits of a mux over scrambled copies (bound should be nearly tight in order of magnitude)
g = W.fam_recmaj(2)
copies = [W.fam_recmaj(2, perm=rng.permutation(9)) for _ in range(4)]
N = 1 << 11; x = np.arange(N)
tt = np.array([copies[x[i] & 3][x[i] >> 2] for i in range(N)], dtype=np.int8)
info, bound = check(tt, 11, [0, 1])
print(f"addr2 over 4 scrambled recmaj, R = address bits: I(z;S_J) = {info:.4f} bits, bound = {bound:.4f}, Inf(R) = {bound/C:.4f}")

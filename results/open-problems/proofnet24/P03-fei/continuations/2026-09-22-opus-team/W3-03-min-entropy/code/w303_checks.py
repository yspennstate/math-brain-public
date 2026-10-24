"""Independent checks of the claims in the report (different code path from the searches).

1. n = 5 witness 0x3355000f: Hinf = 4, I = 7/4 exactly (brute-force Walsh from the truth table);
   it is an addressing function with one constant leaf.
2. Monotone n = 6 maximizer equals tribes(2,3) up to symmetry: Hinf = log2(1024/81), I = 27/16.
3. For monotone f, max_{S nonempty} |fhat(S)| = max_i Inf_i (checked on all monotone f, n <= 5, and on
   20,000 random monotone functions of 7 and 8 variables built as up-closures of random antichains).
4. Hinf <= H2 <= 2 Hinf on 10^5 random functions of 6 variables.
5. Tribes, single-coordinate restriction: Delta_inf = Hinf(f) - (Hinf(f+) + Hinf(f-))/2 and Inf_i,
   exact rationals, w = 3..10 at the best s; ratio Delta_inf / Inf_i grows like 2^w.
6. Block restriction bound for tribes: Hinf <= |R| + log2(1 / E_z (E f_{R<-z})^2) with R = one tribe.
"""
import sys, json, itertools
from fractions import Fraction
import numpy as np
import mpmath as mp
import psutil
_p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
sys.path.insert(0, __file__.rsplit("/", 1)[0].rsplit("\\", 1)[0])
from fmei_lib import stats, bits_to_pm, coeffs, popcounts, influences

out = {}
rng = np.random.default_rng(12345)

# 1
tt = bits_to_pm(np.array([0x3355000f], dtype=np.uint64), 5)[0]
s = stats(tt[None, :])
c = s["coeffs"][0]
out["n5_witness"] = dict(Hinf=float(s["Hinf"][0]), I=float(s["I"][0]), mean=float(c[0]),
                         abs_coeff_values=sorted(set(np.round(np.abs(c) * 32).astype(int).tolist())),
                         influences=influences(tt).tolist())

# 2
tt6 = bits_to_pm(np.array([18206057306133626880], dtype=np.uint64), 6)[0]
s6 = stats(tt6[None, :])
out["monotone_n6_max"] = dict(Hinf=float(s6["Hinf"][0]), I=float(s6["I"][0]), target_Hinf=float(np.log2(1024 / 81)),
                              ratio=float(s6["Hinf"][0] / s6["I"][0]), influences=influences(tt6).tolist(),
                              ones=int(np.sum(tt6 < 0)))

# 3
def up_closure(n, gens):
    N = 1 << n
    val = np.zeros(N, dtype=bool)
    xs = np.arange(N)
    for g in gens:
        val |= (xs & g) == g
    return val

viol = 0
checked = 0
for n in (7, 8):
    for _ in range(10000):
        k = int(rng.integers(1, 6))
        gens = [int(rng.integers(0, 1 << n)) for _ in range(k)]
        # sparsify generators to make influences varied
        gens = [g & int(rng.integers(0, 1 << n)) | (1 << int(rng.integers(n))) for g in gens]
        v = up_closure(n, gens)
        t = np.where(v, -1.0, 1.0)
        cc = coeffs(t)
        mx = np.abs(cc[1:]).max()
        mi = influences(t).max()
        checked += 1
        if abs(mx - mi) > 1e-12:
            viol += 1
out["monotone_max_nonempty_equals_max_influence"] = dict(random_checked=checked, violations=viol)

# 4
bad = 0
F = np.where(rng.random((100000, 64)) < 0.5, -1.0, 1.0)
st = stats(F)
nc = st["I"] > 0
bad = int(np.sum((st["Hinf"][nc] > st["H2"][nc] + 1e-9) | (st["H2"][nc] > 2 * st["Hinf"][nc] + 1e-9)))
out["renyi_sandwich_random_n6"] = dict(checked=int(nc.sum()), violations=bad)

# 5 tribes single-coordinate restriction step (exact)
def hinf_from_max(mx):
    return float(-mp.log(mp.mpf(mx.numerator) / mx.denominator, 2))

rows = []
for w in range(3, 11):
    a = Fraction(1, 2 ** w)
    s0 = int(mp.floor(mp.log(2) / -mp.log(1 - mp.mpf(2) ** (-w))))
    best = None
    for s_ in range(max(2, s0 - 2), s0 + 3):
        q = (1 - a) ** s_
        mx = max((2 * q - 1) ** 2, (2 * a * q / (1 - a)) ** 2)
        I = w * s_ * 2 * a * q / (1 - a)
        r = hinf_from_max(mx) / float(I)
        if best is None or r > best[0]:
            best = (r, s_)
    s_ = best[1]
    q = (1 - a) ** s_
    qm = (1 - a) ** (s_ - 1)                # other tribes all false
    Hf = hinf_from_max(max((2 * q - 1) ** 2, (2 * a * q / (1 - a)) ** 2))
    # f+ : coordinate false -> tribes(w, s-1)
    qp = qm
    Hp = hinf_from_max(max((2 * qp - 1) ** 2, (2 * a * (1 - a) ** (s_ - 2)) ** 2))
    # f- : coordinate true -> OR(AND_{w-1}, tribes(w, s-1)); Pr[false] = (1 - 2a) qm
    b = 2 * a
    pf = (1 - b) * qm
    m_small = 2 * b * qm                               # sets inside the shortened tribe
    m_other = 2 * a * (1 - b) * (1 - a) ** (s_ - 2)    # sets inside another tribe
    Hm = hinf_from_max(max((2 * pf - 1) ** 2, m_small ** 2, m_other ** 2))
    Inf = 2 * a * qm                                   # 2^{-(w-1)} (1-2^-w)^{s-1}
    D = Hf - (Hp + Hm) / 2
    rows.append(dict(w=w, s=s_, Hinf=Hf, Hinf_plus=Hp, Hinf_minus=Hm, Delta_inf=D, Inf_i=float(Inf),
                     ratio=D / float(Inf), I=float(w * s_ * Inf)))
out["tribes_single_coordinate_step"] = rows

# brute-force check of the step formulas on tribes(3,3) and tribes(2,4)
def hinf_of(tt):
    return float(stats(tt[None, :])["Hinf"][0])
bf = []
for (w, s_) in [(3, 3), (2, 4), (3, 4)]:
    n = w * s_
    xs = np.arange(1 << n)
    bits = ((xs[:, None] >> np.arange(n)) & 1).astype(bool)
    v = np.zeros(len(xs), dtype=bool)
    for j in range(s_):
        v |= bits[:, j * w:(j + 1) * w].all(axis=1)
    t = np.where(v, -1.0, 1.0)
    tp = t[bits[:, 0] == False]
    tm = t[bits[:, 0] == True]
    bf.append(dict(w=w, s=s_, Hinf=hinf_of(t), Hinf_plus=hinf_of(tp), Hinf_minus=hinf_of(tm),
                   Inf0=float(influences(t)[0])))
out["tribes_step_bruteforce"] = bf

# 6 block restriction bound for tribes(w,s): R = tribe 1: E_z (E f_z)^2 = 2^-w * 1 + (1-2^-w) (2 q' - 1)^2
blk = []
for w in range(3, 11):
    a = Fraction(1, 2 ** w)
    s_ = [r["s"] for r in rows if r["w"] == w][0]
    qp = (1 - a) ** (s_ - 1)
    E2 = a + (1 - a) * (2 * qp - 1) ** 2
    bound = w + float(-mp.log(mp.mpf(E2.numerator) / E2.denominator, 2))
    Hf = [r["Hinf"] for r in rows if r["w"] == w][0]
    blk.append(dict(w=w, s=s_, Hinf=Hf, block_bound=bound))
out["tribes_block_restriction_bound"] = blk

print(json.dumps(out, indent=1))

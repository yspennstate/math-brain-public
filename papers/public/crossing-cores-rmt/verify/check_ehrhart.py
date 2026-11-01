"""Lattice-point verification of the Ehrhart / Gorenstein layer of the paper.

For every pairing at 2k = 4, 6 (both ensembles; Hankel restricted to parity
mixing) and every parity-mixing pairing at 2k = 8, this script counts lattice
points of N * P directly and checks:

  - Theorem 5.1: P is a lattice polytope (Ehrhart counts fit a degree-(k+1)
    polynomial with rational coefficients that integer-evaluates), 2P has a
    unique interior lattice point, and that point is m = (1, 0, ..., 0)
  - Corollary 5.2: the h*-polynomial is palindromic of degree k with constant
    and leading coefficient one; (k+1)! p(pi) = h*(1)
  - Corollary 5.3 / (5.1): L(N) is odd for even N and even for odd N, and
    h* == (1+z)^k coefficientwise over F_2; (5.2): h*(1) >= 2^{s_2(k)}
  - Theorem 4.1 at lattice level: identical Ehrhart counts for P_H and P_T on
    parity-mixing pairings
  - Theorem 3.4: ear deletion divides the Ehrhart count by (N+1), checked on
    explicit inflation examples
  - volume consistency: leading Ehrhart coefficient equals the engine volume

Run:  python -u check_ehrhart.py
"""
import sys, os
from fractions import Fraction as Fr
from math import comb, factorial
from itertools import product

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact

FAIL = []

def check(name, got, expect):
    ok = (got == expect)
    if not ok:
        print(f"FAIL {name}: {got}  expected {expect}", flush=True)
        FAIL.append((name, got, expect))
    return ok

def word_to_pm(w):
    pos = {}
    for i, ch in enumerate(w):
        pos.setdefault(ch, []).append(i)
    pm = [0] * len(w)
    for ch, (a, b) in pos.items():
        pm[a], pm[b] = b, a
    return tuple(pm)

def forms(pm, kind):
    f = tk_core.toeplitz_forms if kind == "T" else tk_core.hankel_forms
    return tk_core.dedupe_rows(f(pm))

def ehrhart_count(rows, k, N, strict=False, kind="T"):
    """# integer z with 0 <=(<) row.z <=(<) N for all rows.  Safe boxes:
    Toeplitz t_c = W_{l+1}-W_l in [-N,N]; Hankel y = A_{l+1}+A_l in [0,2N]."""
    if kind == "T":
        rngs = [range(0, N + 1)] + [range(-N, N + 1)] * k
    else:
        rngs = [range(0, N + 1)] + [range(0, 2 * N + 1)] * k
    cnt = 0
    pts = []
    for z in product(*rngs):
        ok = True
        for r in rows:
            s = sum(a * b for a, b in zip(r, z))
            if strict:
                if not (0 < s < N):
                    ok = False
                    break
            else:
                if not (0 <= s <= N):
                    ok = False
                    break
        if ok:
            cnt += 1
            if strict:
                pts.append(z)
    return (cnt, pts) if strict else cnt

def hstar_from_counts(L, k):
    """L: list of counts at N=0..k+1 (degree k+1 polytope, codegree 2 =>
    h* has degree k).  h*_j = sum_{i=0}^{j} (-1)^i C(k+2, i) L_{j-i}."""
    d = k + 1
    h = []
    for j in range(0, k + 1):
        h.append(sum((-1) ** i * comb(d + 1, i) * L[j - i] for i in range(0, j + 1)))
    return h

def s2(n):
    return bin(n).count("1")

def run_family(pairings, kind, k, label):
    n_checked = 0
    for pm in pairings:
        rows = forms(pm, kind)
        L = [ehrhart_count(rows, k, N, kind=kind) for N in range(0, k + 2)]
        word = "-".join(map(str, pm))
        # parity refinement (Cor 5.3)
        for N, val in enumerate(L):
            check(f"{label} {word} L({N}) parity", val % 2, 1 - (N % 2))
        h = hstar_from_counts(L, k)
        # codegree 2: the coefficient of z^{k+1} vanishes
        hk1 = sum((-1) ** i * comb(k + 2, i) * L[k + 1 - i] for i in range(0, k + 2))
        check(f"{label} {word} h*_(k+1) = 0", hk1, 0)
        check(f"{label} {word} h* degree-k coeffs nonneg", all(x >= 0 for x in h), True)
        check(f"{label} {word} h* palindromic", h == h[::-1], True)
        check(f"{label} {word} h*_0 = 1", h[0], 1)
        check(f"{label} {word} h* leading = 1", h[-1], 1)
        check(f"{label} {word} h* mod 2 = (1+z)^k",
              [x % 2 for x in h], [comb(k, j) % 2 for j in range(k + 1)])
        vol = pairing_volume_exact(pm, kind)
        check(f"{label} {word} h*(1) = (k+1)! p", sum(h), factorial(k + 1) * vol)
        check(f"{label} {word} h*(1) even", sum(h) % 2, 0)
        check(f"{label} {word} h*(1) >= 2^s2(k)", sum(h) >= 2 ** s2(k), True)
        # Gorenstein: unique interior point of 2P; for Toeplitz Thm 5.1 names
        # it as m = (1,0,...,0); for Hankel it is the Thm 4.1 image of m.
        cnt, pts = ehrhart_count(rows, k, 2, strict=True, kind=kind)
        check(f"{label} {word} unique interior pt of 2P", cnt, 1)
        if cnt == 1 and kind == "T":
            check(f"{label} {word} interior pt = m", pts[0],
                  tuple([1] + [0] * k))
        n_checked += 1
    print(f"OK   {label}: {n_checked} pairings fully checked", flush=True)

# 2k = 4 and 6, all Toeplitz pairings; Hankel on parity-mixing
for n2k in (4, 6):
    k = n2k // 2
    run_family(tk_core.all_pairings(n2k), "T", k, f"T{n2k}")
    run_family(tk_core.parity_pairings(n2k), "H", k, f"H{n2k}")

# 2k = 8 parity-mixing: Toeplitz vs Hankel lattice-level equality (Thm 4.1)
k = 4
same = True
for pm in tk_core.parity_pairings(8):
    rT = forms(pm, "T")
    rH = forms(pm, "H")
    for N in range(0, 4):
        if ehrhart_count(rT, k, N, kind="T") != ehrhart_count(rH, k, N, kind="H"):
            same = False
            print(f"FAIL Thm 4.1 Ehrhart N={N} at {pm}", flush=True)
check("Thm 4.1 lattice-level H = T at 2k=8, N<=3", same, True)
print("OK   Thm 4.1 Ehrhart equality checked at 2k=8", flush=True)

# Theorem 3.4 on explicit inflations: adding an ear multiplies L by (N+1)
pairs = [
    ("121233", "1212"),      # ear 33 added to the two-pair crossing
    ("1212343455", "12123434"),
]
for big_w, core_w in pairs:
    big, core = word_to_pm(big_w), word_to_pm(core_w)
    kb, kc = len(big_w) // 2, len(core_w) // 2
    rb, rc = forms(big, "T"), forms(core, "T")
    for N in range(0, 4):
        lb = ehrhart_count(rb, kb, N)
        lc = ehrhart_count(rc, kc, N)
        check(f"Thm 3.4 {big_w}: L = (N+1)*L(core) at N={N}", lb, (N + 1) * lc)
print("OK   Thm 3.4 inflation checked", flush=True)

print(flush=True)
if FAIL:
    print(f"*** {len(FAIL)} FAILURES ***")
    for f in FAIL[:40]:
        print("   ", f)
    sys.exit(1)
print("ALL EHRHART/GORENSTEIN CHECKS PASSED")

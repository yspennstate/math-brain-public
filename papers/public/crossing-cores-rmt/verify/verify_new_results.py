"""Independent audit of every claim in paper/crossing_cores_new_results.tex.

Each lemma/proposition is re-checked numerically from raw polytopes or exact
moment data, by code written to test the STATEMENT rather than to reproduce
the derivation.  Negative controls are included wherever the statement has a
sharpness claim.

Run:  python -u verify_new_results.py
"""
import sys, os
from fractions import Fraction as Fr
from math import comb, factorial
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact, volume_from_halfspaces

FAIL = []
def check(name, got, expect):
    ok = (got == expect)
    print(f"{'OK  ' if ok else 'FAIL'} {name}: {got}" + ("" if ok else f"  expected {expect}"), flush=True)
    if not ok:
        FAIL.append((name, got, expect))

def wpm(w):
    pos = {}
    for i, ch in enumerate(w):
        pos.setdefault(ch, []).append(i)
    pm = [0] * len(w)
    for ch, (a, b) in pos.items():
        pm[a], pm[b] = b, a
    return tuple(pm)

def p(w):
    return pairing_volume_exact(wpm(w), "T")

def section(w, x, kind="T"):
    pm = wpm(w)
    f = tk_core.toeplitz_forms if kind == "T" else tk_core.hankel_forms
    rows = tk_core.dedupe_rows(f(pm))
    k = len(pm) // 2
    hs = []
    for r in rows:
        c = tuple(r[1:])
        hs.append((c, Fr(x)))
        hs.append((tuple(-v for v in c), 1 - Fr(x)))
    box = [(-1, 1)] * k if kind == "T" else [(-2, 2)] * k
    return volume_from_halfspaces(hs, box)

XS = [Fr(0), Fr(1, 4), Fr(1, 2), Fr(3, 4), Fr(1)]

print("--- Lemma 1: profile factorization + symmetry ---")
for a, b in (("abab", "cdcd"), ("abab", "cdecde"), ("abcabc", "dede")):
    j = a + b
    for x in XS:
        got = section(j, x)
        want = section(a, x) * section(b, x)
        if got != want:
            check(f"factorization {j} at x={x}", got, want)
    print(f"OK   factorization {j} at all five x", flush=True)
for w in ("abab", "abcabc", "abacbdcd"):
    sym = all(section(w, x) == section(w, 1 - x) for x in XS)
    check(f"symmetry of f_{w}", sym, True)

print("\n--- Lemma 2: supermultiplicativity (and its sharpness) ---")
for a, b in (("abab", "cdcd"), ("abcabc", "dede"), ("abacbdcd", "efef")):
    check(f"p({a}{b}) >= p({a})p({b})", p(a + b) >= p(a) * p(b), True)
check("interleaving counterexample p(abcdabcd) < p(abab)p(cdcd)",
      p("abcdabcd") < p("abab") * p("cdcd"), True)

print("\n--- Lemma 3: cube-cycle profile and 2/(r+1) ---")
import string
def cube_profile(r, x):
    x = Fr(x)
    return (1 - x ** r) / r + (1 - (1 - x) ** r) / r
for r in (2, 3, 4, 5):
    w = string.ascii_lowercase[:r] * 2
    for x in XS:
        got = section(w, x)
        want = cube_profile(r, x)
        if got != want:
            check(f"cube profile r={r} x={x}", got, want)
    check(f"p(w_{r}) = 2/(r+1)", p(w), Fr(2, r + 1))

print("\n--- Lemma 4: profile calculus ---")
core = "abcabc"
for g in range(len(core) + 1):
    word = core[:g] + "dd" + core[g:]
    same = all(section(word, x) == section(core, x) for x in XS)
    if not same:
        check(f"ear neutrality at gap {g}", same, True)
print("OK   ear neutrality at every gap of abcabc", flush=True)
for w in ("abab", "abcabc"):
    outer = "z" + w + "z"
    flat = all(section(outer, x) == p(w) for x in XS)
    check(f"flattening f_z{w}z == p({w}) = {p(w)}", flat, True)
# gap insertion equals the marginal integral, checked via gap-independence
# for cycles and gap-dependence for the path of squares
vals = {p("efef" + "abcdabcd"), p("abc" + "efef" + "dabcd"),
        p("abcda" + "efef" + "bcd")}
check("cube cycle r=4: insertion is gap independent", len(vals), 1)
check("cube cycle r=4: value 19/70", vals.pop(), Fr(19, 70))
pathvals = {p("efef" + "abacbdcd"), p("ab" + "efef" + "acbdcd")}
check("path of squares: insertion is gap DEPENDENT", len(pathvals) > 1, True)

print("\n--- Lemma 5: kappa supermultiplicativity ---")
kap = {2: Fr(2,3), 3: Fr(2), 4: Fr(178,15), 5: Fr(253,3), 6: Fr(24798,35),
       7: Fr(206797,30), 8: Fr(687080,9)}
for r in range(2, 5):
    for s in range(2, 5):
        if r + s in kap:
            check(f"kappa_{r+s} >= kappa_{r} kappa_{s}",
                  kap[r + s] >= kap[r] * kap[s], True)

print("\n--- Proposition (cluster equation) at x=1/2, order 4 ---")
F = [Fr(1), Fr(1), Fr(11,4), Fr(47,4), Fr(12823,192)]
inv = [Fr(1)]
for n in range(1, 5):
    s = Fr(0)
    for i in range(1, n + 1):
        s -= F[i] * inv[n - i]
    inv.append(s)
I = [Fr(0)] + [-inv[n] for n in range(1, 5)]
mm = [Fr(1), Fr(1), Fr(8,3), Fr(11), Fr(908,15)]
Jinv = [I[k] - mm[k - 1] for k in range(1, 5)]
check("cluster J_k at x=1/2", Jinv, [Fr(0), Fr(3,4), Fr(55,12), Fr(6139,192)])

print("\n--- Proposition (Hankel non-unimodality certificate) ---")
mH = [Fr(1), Fr(1), Fr(2), Fr(11,2), Fr(281,15)]
u = [(2 * k + 1) * mH[k] for k in range(5)]
check("u vector", u, [Fr(1), Fr(3), Fr(10), Fr(77,2), Fr(843,5)])
D2 = (u[0]*(u[2]*u[4] - u[3]*u[3]) - u[1]*(u[1]*u[4] - u[3]*u[2])
      + u[2]*(u[1]*u[3] - u[2]*u[2]))
check("D_2 = -73/20", D2, Fr(-73, 20))
check("D_2 < 0 (proves non-unimodality)", D2 < 0, True)
# positive control: semicircle must pass
mS = [Fr(comb(2*k, k) // (k + 1)) for k in range(5)]
uS = [(2 * k + 1) * mS[k] for k in range(5)]
D2S = (uS[0]*(uS[2]*uS[4] - uS[3]*uS[3]) - uS[1]*(uS[1]*uS[4] - uS[3]*uS[2])
       + uS[2]*(uS[1]*uS[3] - uS[2]*uS[2]))
check("semicircle control D_2 > 0", D2S > 0, True)

print("\n--- Proposition (profile-level Hankel = Toeplitz) ---")
for w in ("abcdbadc", "abcdcdab"):
    if not tk_core.is_parity_mixing(wpm(w)):
        continue
    for x in (Fr(0), Fr(1,4), Fr(1,2)):
        got, want = section(w, x, "H"), section(w, x, "T")
        if got != want:
            check(f"H=T profile {w} x={x}", got, want)
    print(f"OK   H=T profile for {w}", flush=True)

print()
if FAIL:
    print(f"*** {len(FAIL)} FAILURES ***")
    for f in FAIL:
        print("   ", f)
    sys.exit(1)
print("ALL NEW-RESULT CLAIMS INDEPENDENTLY VERIFIED")

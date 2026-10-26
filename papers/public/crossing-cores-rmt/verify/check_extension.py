"""Verification of the Section-14 extension results (owner-supplied checker,
re-derived and extended here).

1. Re-run the aggregate order-22 Ehrhart reconstruction exactly as given.
2. Cross-checks the extension moment tables against everything this session
   computed independently:
   - m_16(gamma_H) vs tonight's reduced-core computation (exact match test)
   - m_16(gamma_T) vs the (13.2) Schur threshold (the free-ID verdict)
   - the implied kappa_8^T, banked for the running local sweep
   - growth-ratio sanity on all new moments
3. Conditional-positivity minors of the Toeplitz free cumulants through
   order 22, re-derived from scratch (their claim: all positive).

Run:  python -u check_extension.py
"""
from fractions import Fraction as F
from math import comb, factorial

FAIL = []

def check(name, got, expect):
    ok = (got == expect)
    print(f"{'OK  ' if ok else 'FAIL'} {name}: {got}" + ("" if ok else f"  expected {expect}"))
    if not ok:
        FAIL.append((name, got, expect))

def cat(k):
    return comb(2 * k, k) // (k + 1)

T = {2: F(1), 4: F(8, 3), 6: F(11), 8: F(908, 15), 10: F(415),
     12: F(23840, 7), 14: F(325719, 10),
     16: F(112135066, 315), 18: F(3065263961, 700),
     20: F(69174280444, 1155), 22: F(5680684105259, 6300)}
H = {2: F(1), 4: F(2), 6: F(11, 2), 8: F(281, 15), 10: F(2717, 36),
     12: F(1052, 3), 14: F(1331087, 720),
     16: F(9179819, 840), 18: F(803482581, 11200)}

# ---- 1. the order-22 aggregate Ehrhart reconstruction, verbatim
A11 = [13749310575, 8166944847600, 687866115262095, 18568659405067200,
       251106522168243951, 2151002429342092656]

def hstar_prefix(values, degree):
    hs = []
    for n, value in enumerate(values):
        correction = sum(hs[i] * comb(n + degree - i, degree)
                         for i in range(len(hs)) if n + degree - i >= degree)
        hs.append(value - correction)
    return hs

prefix = hstar_prefix(A11, 12)
hstar = prefix + prefix[::-1]
check("order-22 h* palindrome length", len(hstar), 12)
check("h*_0 = number of pairings (21-1)!! = 13749310575",
      hstar[0], 13749310575)
check("aggregate h* sums to 12! * m_22", F(sum(hstar), factorial(12)), T[22])
check("h* coefficients all positive", all(x > 0 for x in hstar), True)

# ---- 2. cross-checks against tonight's independent computations
mine_H16 = F(9179819, 840)   # this session, reduced-core route, own engine
check("m_16(gamma_H): extension table == tonight's independent value",
      H[16], mine_H16)

THRESH = F(3863516832738344459, 10908088231950)   # (13.2), verified earlier
check("m_16(gamma_T) exceeds the Schur threshold (free-ID test passes)",
      T[16] > THRESH, True)
margin = T[16] - THRESH
print(f"     margin above threshold: {margin} ~ {float(margin):.4f}")

KNOWN_PART = F(29362422, 105)  # Cat_8 + sum_{r<8} C(16,8-r) kappa_r^T
implied_kappa8T = T[16] - KNOWN_PART
print(f"     implied kappa_8^T = {implied_kappa8T} ~ {float(implied_kappa8T):.4f}"
      f"  (local sweep will verify independently)")

# growth-ratio smell test: ratios m_{2k+2}/m_{2k} should grow smoothly ~ linearly
for tab, name in ((T, "T"), (H, "H")):
    ks = sorted(tab)
    ratios = [float(tab[ks[i + 1]] / tab[ks[i]]) for i in range(len(ks) - 1)]
    diffs = [ratios[i + 1] - ratios[i] for i in range(len(ratios) - 1)]
    print(f"     {name} growth ratios: " +
          ", ".join(f"{r:.3f}" for r in ratios))
    check(f"{name} ratios strictly increasing", all(d > 0 for d in diffs), True)

# ---- 3. free-cumulant conditional-positivity minors through order 22
def free_cumulants(m_even, top):
    m = {0: F(1)}
    for k, v in m_even.items():
        m[k] = v
    for n in range(1, top + 1):
        m.setdefault(n, F(0))
    M = [m.get(i, F(0)) for i in range(top + 1)]
    powers = {1: M[:]}
    for s in range(2, top + 1):
        prev = powers[s - 1]
        cur = [F(0)] * (top + 1)
        for i, a in enumerate(prev):
            if a:
                for j in range(0, top + 1 - i):
                    if M[j]:
                        cur[i + j] += a * M[j]
        powers[s] = cur
    r = {}
    for n in range(1, top + 1):
        acc = m[n]
        for s in range(1, n):
            if r.get(s):
                acc -= r[s] * powers[s][n - s]
        r[n] = acc
    return r

rT = free_cumulants(T, 22)
print("     free cumulants r_16..r_22:",
      ", ".join(f"r{n}={rT[n]}" for n in (16, 18, 20, 22)))

def minors(seq_idx, r):
    out = []
    for t in range(1, len(seq_idx) + 1):
        idx = seq_idx[:t]
        A = [[r[i + j] for j in idx] for i in idx]
        det = F(1)
        sz = t
        Ac = [row[:] for row in A]
        for c in range(sz):
            piv = next((rr for rr in range(c, sz) if Ac[rr][c] != 0), None)
            if piv is None:
                det = F(0)
                break
            if piv != c:
                Ac[c], Ac[piv] = Ac[piv], Ac[c]
                det = -det
            det *= Ac[c][c]
            for rr in range(c + 1, sz):
                if Ac[rr][c]:
                    f = Ac[rr][c] / Ac[c][c]
                    for cc in range(c, sz):
                        Ac[rr][cc] -= f * Ac[c][cc]
        out.append(det)
    return out

odd = minors([1, 3, 5, 7, 9, 11], rT)      # indices i+j even via odd+odd
even = minors([2, 4, 6, 8, 10], rT)
print("     odd-block minors:", ["+" if d > 0 else str(d) for d in odd])
print("     even-block minors:", ["+" if d > 0 else str(d) for d in even])
check("odd-block minors positive through order 22", all(d > 0 for d in odd), True)
check("even-block minors positive through order 22", all(d > 0 for d in even), True)

# ---- the owner checker's own auxiliary identities, verbatim
rho = F(2, 5)
check("pathwise mixed moment 1 + (5/3)rho^2", 1 + F(5, 3) * rho ** 2, F(19, 15))
check("pathwise mixed moment 2/3 + 2rho^2", F(2, 3) + 2 * rho ** 2, F(74, 75))
for d in range(1, 9):
    assert 2 + F(2, 3) ** d > 2
    assert 5 + 6 * F(2, 3) ** d + 4 * F(1, 2) ** d > 5
print("OK   tensor low-moment inequalities d=1..8")

print()
if FAIL:
    print(f"*** {len(FAIL)} FAILURES ***")
    for f in FAIL:
        print("   ", f)
else:
    print("EXTENSION CHECKS ALL PASS")

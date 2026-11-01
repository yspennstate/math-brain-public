"""The order-24 analogue of (13.2): the exact value of m_24 that decides
the next free conditional-positivity test for gamma_T.

Equation (13.2) works at order sixteen: the even block indexed by
{2,4,6} is enlarged by the row and column at index 8, and the Schur
complement condition r_16 - v^T A^{-1} v >= 0 becomes a threshold on
m_16.  With moments now known through order 22, that test and its
successors at 18, 20, 22 are all decided (they pass).  The first
undecided one is the enlargement whose new diagonal entry is r_24, and
this script computes the exact rational threshold it puts on m_24 -- the
next finite target, stated in the same form as (13.2).

Both parity blocks are treated: the even block indexed by
{2,4,...,2M} and the odd block indexed by {1,3,...,2M-1}; the binding
threshold is the larger.

Run:  python -u order24_threshold.py
"""
from fractions import Fraction as Fr

mT = {2: Fr(1), 4: Fr(8,3), 6: Fr(11), 8: Fr(908,15), 10: Fr(415),
      12: Fr(23840,7), 14: Fr(325719,10), 16: Fr(112135066,315),
      18: Fr(3065263961,700), 20: Fr(69174280444,1155),
      22: Fr(5680684105259,6300)}
TOP = 24

def free_cumulants(mom_even, top, m_top_zero=False):
    m = {0: Fr(1)}
    for k, v in mom_even.items():
        m[k] = v
    for n in range(1, top + 1):
        m.setdefault(n, Fr(0))
    if m_top_zero:
        m[top] = Fr(0)
    M = [m.get(i, Fr(0)) for i in range(top + 1)]
    powers = {1: M[:]}
    for s in range(2, top + 1):
        prev = powers[s - 1]
        cur = [Fr(0)] * (top + 1)
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

# r_24 = m_24 + C, with C obtained by setting m_24 = 0
r0 = free_cumulants(mT, TOP, m_top_zero=True)
C = r0[TOP]
print(f"r_24 = m_24 + ({C})")
print(f"     = m_24 - {-C}" if C < 0 else "")

r = dict(r0)   # all r_n for n < 24 are unaffected by m_24

def solve(A, v):
    n = len(A)
    M = [row[:] + [v[i]] for i, row in enumerate(A)]
    for c in range(n):
        piv = next(rr for rr in range(c, n) if M[rr][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for rr in range(n):
            if rr != c and M[rr][c] != 0:
                f = M[rr][c]
                M[rr] = [a - f * b for a, b in zip(M[rr], M[c])]
    return [M[i][n] for i in range(n)]

def det(A):
    n = len(A)
    B = [row[:] for row in A]
    d = Fr(1)
    for c in range(n):
        piv = next((rr for rr in range(c, n) if B[rr][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            B[c], B[piv] = B[piv], B[c]
            d = -d
        d *= B[c][c]
        for rr in range(c + 1, n):
            if B[rr][c]:
                f = B[rr][c] / B[c][c]
                for cc in range(c, n):
                    B[rr][cc] -= f * B[c][cc]
    return d

for name, idx in (("even", [2, 4, 6, 8, 10, 12]), ("odd", [1, 3, 5, 7, 9, 11])):
    core = idx[:-1]
    last = idx[-1]
    A = [[r[i + j] for j in core] for i in core]
    dA = det(A)
    print(f"\n{name} block indexed by {idx}:")
    print(f"   leading block {core} determinant = {dA} "
          f"({'positive definite' if dA > 0 else 'NOT positive'})")
    if 2 * last != TOP:
        # the new diagonal entry is r_{2*last}; only proceed if it is r_24
        diag = r.get(2 * last)
        v = [r[i + last] for i in core]
        x = solve([row[:] for row in A], v[:])
        q = sum(a * b for a, b in zip(v, x))
        slack = diag - q
        print(f"   new diagonal r_{2*last} = {diag}")
        print(f"   v^T A^-1 v = {q}")
        print(f"   Schur slack = {slack} = {float(slack):.6g}  "
              f"{'PASSES' if slack >= 0 else 'FAILS'}")
        continue
    v = [r[i + last] for i in core]
    x = solve([row[:] for row in A], v[:])
    q = sum(a * b for a, b in zip(v, x))
    thresh = q - C
    print(f"   v^T A^-1 v = {q}")
    print(f"   condition r_24 >= v^T A^-1 v  becomes")
    print(f"   m_24 >= {thresh}")
    print(f"        = {float(thresh):.6f}")

print("\nInterpretation: an exact m_24 below the displayed threshold would")
print("disprove free infinite divisibility of gamma_T; a value at or above")
print("it passes the order-24 test.  This is the next finite target, in the")
print("same form as (13.2) at order sixteen.")

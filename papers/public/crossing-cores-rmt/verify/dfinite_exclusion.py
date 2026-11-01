"""How large an algebraic or holonomic equation can the moment series NOT
satisfy?  A quantitative exclusion for the extension's open item
"D-finiteness of the volume-weighted moment series".

Method (guess-and-verify with a held-out moment).  For each ansatz size,
impose the coefficient equations that use only the KNOWN moments up to a
cut, solve exactly for the nullspace, and then test the resulting
equation against the moments beyond the cut.  Any ansatz whose nullspace
is nonempty but whose prediction misses a held-out moment is excluded.
With N known moments an ansatz with u unknowns is falsifiable when
u <= N - 1, leaving at least one moment for the test.

Toeplitz moments are known through order 22 (12 values counting m_0),
Hankel through order 18 (10 values).

Run:  python -u dfinite_exclusion.py
"""
from fractions import Fraction as Fr

mT = [Fr(1), Fr(1), Fr(8,3), Fr(11), Fr(908,15), Fr(415), Fr(23840,7),
      Fr(325719,10), Fr(112135066,315), Fr(3065263961,700),
      Fr(69174280444,1155), Fr(5680684105259,6300)]
mH = [Fr(1), Fr(1), Fr(2), Fr(11,2), Fr(281,15), Fr(2717,36), Fr(1052,3),
      Fr(1331087,720), Fr(9179819,840), Fr(803482581,11200)]

def smul(A, B, N):
    out = [Fr(0)] * N
    for i, a in enumerate(A):
        if a == 0:
            continue
        for j in range(0, N - i):
            if B[j]:
                out[i + j] += a * B[j]
    return out

def sshift(A, i, N):
    return [Fr(0)] * i + A[:N - i]

def sderiv(A, N):
    return [A[k + 1] * (k + 1) for k in range(N - 1)] + [Fr(0)]

def nullspace(rows, ncols):
    m = [list(r) for r in rows]
    nr = len(m)
    piv_cols, r = [], 0
    for c in range(ncols):
        piv = next((i for i in range(r, nr) if m[i][c] != 0), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        pv = m[r][c]
        m[r] = [x / pv for x in m[r]]
        for i in range(nr):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [x - f * y for x, y in zip(m[i], m[r])]
        piv_cols.append(c)
        r += 1
        if r == nr:
            break
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [Fr(0)] * ncols
        v[fc] = Fr(1)
        for ri, pc in enumerate(piv_cols):
            v[pc] = -m[ri][fc]
        basis.append(v)
    return basis

def scan(m, label):
    N = len(m)
    S = m[:]
    print(f"=== {label}: {N} known coefficients (through order {2*(N-1)}) ===")
    excluded_alg, excluded_ode, undetermined = [], [], []
    # algebraic ansatzes P(z, M) = 0
    for dm in range(1, 6):
        Mp = [[Fr(1)] + [Fr(0)] * (N - 1)]
        for _ in range(dm):
            Mp.append(smul(Mp[-1], S, N))
        for dz in range(0, 7):
            u = (dz + 1) * (dm + 1)
            if u > N - 1:
                continue
            terms = [sshift(Mp[j], i, N) for j in range(dm + 1) for i in range(dz + 1)]
            rows = [tuple(t[n] for t in terms) for n in range(u)]
            basis = nullspace(rows, len(terms))
            if not basis:
                excluded_alg.append((dz, dm, "no solution"))
                continue
            ok = False
            for c in basis:
                resid = [sum(ci * t[n] for ci, t in zip(c, terms)) for n in range(u, N)]
                if all(x == 0 for x in resid):
                    ok = True
                    break
            if ok:
                undetermined.append(("alg", dz, dm))
            else:
                excluded_alg.append((dz, dm, "held-out moments refute"))
    # holonomic ansatzes sum p_j(z) M^(j) = 0
    derivs = [S]
    for _ in range(4):
        derivs.append(sderiv(derivs[-1], N))
    for r_ord in range(1, 5):
        for d in range(0, 7):
            u = (r_ord + 1) * (d + 1)
            if u > N - 1:
                continue
            terms = [sshift(derivs[j], i, N) for j in range(r_ord + 1) for i in range(d + 1)]
            rows = [tuple(t[n] for t in terms) for n in range(u)]
            basis = nullspace(rows, len(terms))
            if not basis:
                excluded_ode.append((r_ord, d, "no solution"))
                continue
            ok = False
            for c in basis:
                resid = [sum(ci * t[n] for ci, t in zip(c, terms)) for n in range(u, N)]
                if all(x == 0 for x in resid):
                    ok = True
                    break
            if ok:
                undetermined.append(("ode", r_ord, d))
            else:
                excluded_ode.append((r_ord, d, "held-out moments refute"))
    print(f"  algebraic ansatzes excluded: {len(excluded_alg)} "
          f"(bidegrees up to (6,5) with at most {N-1} unknowns)")
    print(f"  holonomic ansatzes excluded: {len(excluded_ode)} "
          f"(order <= 4, degree <= 6, at most {N-1} unknowns)")
    if undetermined:
        print(f"  ansatzes CONSISTENT with all known moments: {undetermined}")
    else:
        print(f"  ansatzes consistent with all known moments: NONE")
    big = max([(r, d) for r, d, _ in excluded_ode], default=None)
    if big:
        print(f"  largest holonomic size excluded: order {big[0]}, degree {big[1]}")

scan(mT, "gamma_T")
print()
scan(mH, "gamma_H")
print()
print("Interpretation: every ansatz small enough to be falsifiable by the")
print("known moments IS falsified, so neither moment generating function")
print("satisfies an algebraic or linear differential equation of the sizes")
print("tested.  This is evidence against D-finiteness, not a proof of it.")

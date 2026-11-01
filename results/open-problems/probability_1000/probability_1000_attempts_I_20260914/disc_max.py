"""Open Problem 11 of the Randomstrasse 2024 list: the value of

    sup_n  sup_{A in {+-1}^{n x n}}  disc(A)/sqrt(n),      disc(A) = min_{x in {+-1}^n} ||Ax||_inf.

The list notes the 2x2 Hadamard matrix gives sqrt(2) and reports no known lower bound above it.

EXACT REFORMULATION.  disc(A) >= v means: for every sign vector x there is a row r of A with
|r.x| >= v.  Rows and sign vectors both matter only up to a global sign, so put

    U = {+-1}^n / +-1   (2^(n-1) sign vectors),      R = the same set, used as candidate rows,
    C_v(r) = { x in U : |r.x| >= v }.

Then max over A of disc(A) is the largest v for which n of the sets C_v(r) cover U.  That is a set-cover
feasibility question with 2^(n-1) sets over a universe of 2^(n-1) points, choosing n of them, and for
small n it can be decided exactly by integer programming.

|r.x| has the parity of n, so only v of that parity need testing.
"""
import numpy as np, sys, itertools
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csc_matrix


def vectors(n):
    """the 2^(n-1) sign vectors up to global sign, as a (2^(n-1), n) array of +-1"""
    m = 1 << (n - 1)
    b = ((np.arange(m)[:, None] >> np.arange(n)[None, :]) & 1)
    b[:, n - 1] = 0                      # fix the last coordinate to +1, killing the global sign
    return 1 - 2 * b


def inner(n):
    V = vectors(n)
    return np.abs(V @ V.T)               # |r.x| for every (row, sign vector) pair


def counting_bound(n, v):
    """n rows can each cover at most this many sign vectors at level v, so if n times it is below
    2^(n-1) the level is impossible - no solver needed"""
    from math import comb
    k = (n - v) // 2
    per = sum(comb(n, j) for j in range(0, k + 1))
    return n * per >= (1 << (n - 1))


def coverable(T, v, n, time_limit=120.0):
    if not counting_bound(n, v):
        return False, None
    """can n rows cover every sign vector at level v?  exact, by integer programming"""
    M = (T >= v)                          # sets as a boolean matrix, rows = candidate rows
    if not M.any(axis=0).all():
        return False, None                # some x is covered by no row at all
    m = M.shape[0]
    A = csc_matrix(M.T.astype(np.int8))   # constraint: each x covered at least once
    cons = [LinearConstraint(A, lb=1, ub=np.inf),
            LinearConstraint(csc_matrix(np.ones((1, m), dtype=np.int8)), lb=0, ub=n)]
    res = milp(c=np.zeros(m), constraints=cons, integrality=np.ones(m),
               bounds=Bounds(0, 1), options={'time_limit': time_limit, 'presolve': True})
    # status 0 = solved, 1 = hit the time limit (verdict unknown), 2 = infeasible
    if res.status == 0 and res.x is not None:
        return True, np.where(res.x > 0.5)[0]
    if res.status == 2:
        return False, None
    raise TimeoutError(f"solver did not decide n={n} v={v}: status {res.status}")


def max_disc(n, time_limit=120.0):
    T = inner(n)
    best, wit = 0, None
    for v in range(n - (n % 2 == 0), 0, -2) if n % 2 else range(n, 0, -2):
        ok, pick = coverable(T, v, n, time_limit)
        if ok:
            best, wit = v, pick
            break
    return best, wit, T


if __name__ == '__main__':
    hi = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    print(f"{'n':>3} {'max disc':>9} {'ratio':>8} {'vs sqrt2':>9}  rows attaining it")
    for n in range(2, hi + 1):
        b, wit, T = max_disc(n)
        V = vectors(n)
        r = b / np.sqrt(n)
        mark = 'BEATS' if r > np.sqrt(2) + 1e-12 else ('ties' if abs(r - np.sqrt(2)) < 1e-12 else '')
        rows = [''.join('+' if t > 0 else '-' for t in V[i]) for i in (wit if wit is not None else [])]
        print(f"{n:>3} {b:>9} {r:>8.4f} {mark:>9}  {' '.join(rows[:n])}", flush=True)

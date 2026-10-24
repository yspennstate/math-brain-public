"""Decide the single open case n = 12, v = 6: can twelve sign vectors, with their complements, cover
{+-1}^12 within Hamming distance 3?  If yes, max disc over 12x12 sign matrices is 6 and the ratio is
6/sqrt(12) = 1.732, above the 5/3 attained at n = 9.  Equivalent to whether a complement-closed binary
covering code of length 12, size 24 and radius 3 exists; the published K(12,3) = 28 > 24 says NO.
"""
import numpy as np
from disc_max import inner, vectors
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csc_matrix

n, v = 12, 6
T = inner(n)
M = (T >= v)
print(f"n={n}, v={v}: {M.shape[0]} candidate rows, {M.shape[1]} sign vectors to cover")
print(f"each row covers {M[0].sum()} of them; {n} rows cover at most {n*M[0].sum()}")
A = csc_matrix(M.T.astype(np.int8))
cons = [LinearConstraint(A, lb=1, ub=np.inf),
        LinearConstraint(csc_matrix(np.ones((1, M.shape[0]), dtype=np.int8)), lb=0, ub=n)]
res = milp(c=np.zeros(M.shape[0]), constraints=cons, integrality=np.ones(M.shape[0]),
           bounds=Bounds(0, 1), options={'time_limit': 3000.0, 'presolve': True, 'disp': False})
print("solver status", res.status, "-", {0: 'FEASIBLE', 1: 'time limit, undecided', 2: 'INFEASIBLE'}.get(res.status, res.message))
if res.status == 0:
    V = vectors(n); pick = np.where(res.x > 0.5)[0]
    A2 = V[pick]
    d = int(np.abs(V @ A2.T).max(axis=1).min())
    print("verified discrepancy of the witness:", d, " ratio", d/np.sqrt(n))
    for r in A2: print('   ', ''.join('+' if t > 0 else '-' for t in r))

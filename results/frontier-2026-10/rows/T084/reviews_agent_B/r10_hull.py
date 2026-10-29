# T084, agent B: R10 pair (0,1) at q = 0 (and q = 0.05). For each negative term, is its exponent in the convex hull of the
# positive terms' exponents (LP)? A negative exponent outside that hull makes N < 0 somewhere. Also: which negative terms
# fail SAGE at RAD 4 alone (each negative given every positive term, no sharing).
import json, numpy as np
from scipy.optimize import linprog
MARK = chr(10) + 'if __name__ =='
exec(open('sage_cert.py').read().split(MARK)[0])
A = [0b11001, 0b11100, 0b01110, 0b00111, 0b10011]
colsR10 = [1 << i for i in range(5)] + [sum(((A[row] >> (4 - c)) & 1) << row for row in range(5)) for c in range(5)]
C = Npoly(colsR10, 0, 1); keys = list(C.keys()); M = np.array(keys, float)
for qv in [0.0, 0.05]:
    cv = np.array([float(sp.Poly(C[k], q).eval(sp.Rational(qv).limit_denominator(10**9))) for k in keys])
    neg = [i for i in range(len(keys)) if cv[i] < -1e-15]; pos = [i for i in range(len(keys)) if cv[i] > 1e-15]
    out = []
    for k in neg:
        P = M[pos]; n = len(pos)
        r = linprog(np.zeros(n), A_eq=np.vstack([P.T, np.ones(n)]), b_eq=np.concatenate([M[k], [1]]), bounds=[(0, None)] * n, method='highs')
        out.append(r.status == 0)
    print(json.dumps(dict(q=qv, negatives=len(neg), in_hull=sum(out), outside=[(keys[k], str(sp.factor(C[keys[k]]))) for k, o in zip(neg, out) if not o][:5])), flush=True)

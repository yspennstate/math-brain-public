# T084, agent B: for each negative term of R10 (0,1) at q = 0, the smallest L1 radius RAD such that its exponent is in the
# convex hull of the positive exponents within RAD.
import json, numpy as np
from collections import Counter
from scipy.optimize import linprog
MARK = chr(10) + 'if __name__ =='
exec(open('sage_cert.py').read().split(MARK)[0])
A = [0b11001, 0b11100, 0b01110, 0b00111, 0b10011]
colsR10 = [1 << i for i in range(5)] + [sum(((A[row] >> (4 - c)) & 1) << row for row in range(5)) for c in range(5)]
C = Npoly(colsR10, 0, 1); keys = list(C.keys()); M = np.array(keys, float)
cv = np.array([float(sp.Poly(C[k], q).eval(0)) for k in keys])
neg = [i for i in range(len(keys)) if cv[i] < 0]; pos = np.array([i for i in range(len(keys)) if cv[i] > 0])
need = []
for k in neg:
    d = np.abs(M[pos] - M[k]).sum(1)
    for R in range(1, 17):
        J = pos[d <= R]
        if len(J) == 0: continue
        r = linprog(np.zeros(len(J)), A_eq=np.vstack([M[J].T, np.ones(len(J))]), b_eq=np.concatenate([M[k], [1]]), bounds=[(0, None)] * len(J), method='highs')
        if r.status == 0: need.append(R); break
print(json.dumps(dict(negatives=len(neg), radius_needed=dict(Counter(need)))))

"""Fresh exact symbolic small cases, path determinants and perturbation algebra.

No author code is used. A 240s alarm bounds this single-process computation.
"""
import json
import os
from pathlib import Path
import signal
import time

os.environ.update(OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.nice(10 - os.getpriority(os.PRIO_PROCESS, 0))
import sympy as sp


def timeout(signum, frame):
    raise TimeoutError("240-second computation limit")


signal.signal(signal.SIGALRM, timeout)
signal.alarm(240)
start = time.monotonic()
x = sp.Symbol("x")
w = sp.Symbol("w", positive=True)
rows = []
for n in (4, 6, 8):
    for k in range(2, n//2+1):
        edges = [(i, (i+1) % n, sp.Integer(1)) for i in range(n)] + [(0, k, w)]
        degrees = [sp.Integer(0)] * n
        L = sp.zeros(n)
        for i, j, c in edges:
            degrees[i] += c
            degrees[j] += c
            e = sp.zeros(n, 1)
            e[i], e[j] = 1, -1
            L += c * e * e.T
        D = sp.diag(*degrees)
        p = sp.factor((L-x*D).det(method="domain-ge"))
        M = sp.zeros(n)
        for i, j, c in edges:
            denominator = 2+w if i in (0, k) or j in (0, k) else sp.Integer(2)
            e = sp.zeros(n, 1)
            e[i], e[j] = 1, -1
            M += c / denominator * e * e.T
        q = sp.factor(M.charpoly(x).as_expr())
        assert sp.diff(p, x).subs(x, 0) != 0
        row = dict(n=n, k=k, rw_generalized_determinant=str(p), mh_characteristic_polynomial=str(q))
        if n == 4:
            expected_rw = x*(x-1)*(x-2*(w+1)/(w+2))*(x-(w+4)/(w+2))
            expected_mh = x*(x-2/(w+2))*(x-2*(w+1)/(w+2))*(x-4/(w+2))
            assert sp.simplify(p / sp.prod(degrees) - expected_rw) == 0
            assert sp.simplify(q - expected_mh) == 0
            row["C4_gap_rw"] = "1"
            row["C4_gap_mh"] = "2/(w+2)"
        if 2*k == n:
            a = 1-sp.cos(2*sp.pi/n)
            assert sp.simplify(p.subs(x, a)) == 0
            row["antipodal_a_exact_root"] = True
        rows.append(row)

# Rebuild the Dirichlet path determinant without importing author code.
path_results = []
for m in range(2, 16):
    T = sp.diag(*([2]*(m-1)))
    for i in range(m-2):
        T[i, i+1] = T[i+1, i] = -1
    p = T.charpoly(x).as_expr()
    assert sp.expand(p - (-1)**(m-1)*sp.chebyshevu(m-1, 1-x/2)) == 0
    path_results.append(m)

nn, tt = sp.symbols("n t", positive=True)
v = nn + 2*w*tt**2 - (2*w*tt)**2/(2*nn+2*w)
assert sp.simplify(v - nn*(1+2*w*tt**2/(nn+w))) == 0
aa, cc, ss, rr = sp.symbols("a c s r", real=True)
assert sp.expand(2*((aa*cc-ss*rr)**2+(aa*cc+ss*rr)**2)-4*(aa**2*cc**2+ss**2*rr**2)) == 0
out = dict(small_exact_cases=rows, path_m_values=path_results,
           variance_identity=True, four_edge_identity=True,
           seconds=round(time.monotonic()-start, 3), passed=True)
Path(__file__).with_name("referee_exact.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps(out, indent=2))

"""Exact certificate for the regular graph of Regev and Shinkar (arXiv:1506.08631, Appendix A, Figure 2):
the cube {0,1}^3 (vertices 0..7, adjacent when the binary labels differ in one bit) with a square pyramid on
the faces x0 = 0 (apex 8) and x0 = 1 (apex 9). It is 4-regular on 10 vertices. For the edge x = 0, y = 8
(a face vertex and its apex) we certify, at t* = 7, that r(t*) > 1 and r'(t*) < 0, where
r(t) = H_t(x,y)/H_t(x,x) and H_t = exp(-t(I - A/d)).
H_t = exp(-s M), M = dI - A (integer), s = t/d. Taylor series in exact rationals, tail bounded by
sum_{k>K} (||M||_inf s)^k / k! entrywise (||M||_inf = 2d). Sign of r' is the sign of h = b'a - b a'."""
from fractions import Fraction as F
import numpy as np, sys

EDGES = [(a, b) for a in range(8) for b in range(a + 1, 8) if bin(a ^ b).count('1') == 1]
EDGES += [(a, 8) if a % 2 == 0 else (a, 9) for a in range(8)]
X, Y = 0, 8
n, d = 10, 4
A = [[0] * n for _ in range(n)]
for u, v in EDGES:
    A[u][v] = A[v][u] = 1
deg = [sum(r) for r in A]
assert all(g == d for g in deg), deg
# connected
seen = {0}; st = [0]
while st:
    u = st.pop()
    for v in range(n):
        if A[u][v] and v not in seen: seen.add(v); st.append(v)
assert len(seen) == n
assert A[X][Y] == 1
M = [[(d if i == j else 0) - A[i][j] for j in range(n)] for i in range(n)]

# locate the dip numerically
L = np.eye(n) - np.array(A, float) / d
w, V = np.linalg.eigh(L)
ts = np.linspace(0, 40, 40001)
E = np.exp(-np.outer(ts, w))
a = E @ (V[X] ** 2); b = E @ (V[X] * V[Y]); r = b / a
i0 = int(np.argmax(r))
print('numeric: max r(t) = %.6f at t = %.3f; r(7) = %.6f' % (r[i0], ts[i0], r[7000]))
tstar = F(7)
s = tstar / d

# row X of M^k, exact integers
K = 120
row = [1 if j == X else 0 for j in range(n)]
rows = [row]
for k in range(K + 1):
    row = [sum(row[i] * M[i][j] for i in range(n)) for j in range(n)]
    rows.append(row)
fact = 1
aS = F(0); bS = F(0); apS = F(0); bpS = F(0)
for k in range(K + 1):
    if k: fact *= k
    c = (-s) ** k / fact
    aS += c * rows[k][X]; bS += c * rows[k][Y]
    # H' = -(1/d) M H: entries of row X of M^{k+1}
    apS += -c * rows[k + 1][X] / d; bpS += -c * rows[k + 1][Y] / d
q = 2 * d * s
term = q ** (K + 1); f2 = 1
for k in range(1, K + 2): f2 *= k
tail = F(term) / f2 * 2          # sum_{k>K} q^k/k! <= 2 q^{K+1}/(K+1)! when q <= (K+2)/2
assert q <= F(K + 2, 2)
tail_p = 2 * tail          # derivative entries: (1/d) * sum_{k>K} s^k (2d)^{k+1}/k! = 2 * (tail of the series in q)
eps = tail_p + tail
lo_a, hi_a = aS - eps, aS + eps
assert lo_a > 0
# h = b'a - b a', upper bound by interval arithmetic
def iv_mul(l1, h1, l2, h2):
    c = [l1 * l2, l1 * h2, h1 * l2, h1 * h2]; return min(c), max(c)
p1 = iv_mul(bpS - eps, bpS + eps, aS - eps, aS + eps)
p2 = iv_mul(bS - eps, bS + eps, apS - eps, apS + eps)
h_hi = p1[1] - p2[0]
print('t* =', tstar, ' tail bound', float(eps))
print('a(t*) in [%.12f, %.12f]' % (float(lo_a), float(hi_a)))
print('h(t*) = b\'a - ba\' <= %.6e' % float(h_hi))
print('r\'(t*) = h/a^2 <= %.6e' % float(h_hi / hi_a ** 2 if h_hi < 0 else h_hi / lo_a ** 2))
gap_lo = (bS - eps) - (aS + eps)
print('b(t*) - a(t*) >= %.6e, so r(t*) > 1' % float(gap_lo) if gap_lo > 0 else 'r(t*) > 1 not certified')
# the graph is not walk-regular: some diagonal of A^k is not constant
A_np = np.array(A, int)
walk_reg = all(len(set(np.diag(np.linalg.matrix_power(A_np, k)))) == 1 for k in range(2, 8))
print('walk-regular (k<=7 diagonals constant):', walk_reg)
print('RESULT', 'PASS' if h_hi < 0 and gap_lo > 0 and not walk_reg else 'FAIL')

"""Checks for 'Euclidean contractivity fails for generalized Polya urns' (Remark 3.7 of Neri-Pinto, arXiv:2607.07309).

Conventions: colours 0..d-1, R[i][j] = balls of colour j added when colour i is drawn, rows sum to the balance lam.
For an integer row vector w with sum 0 and k in {None, 0..d-1}:
    Q_k(w) = sum_{i != k} w_i ((w R)_i - lam w_i).
Reading 'full' (k = None): the condition with p = d restricted to mean-zero vectors.
Reading k: the condition with p = d - 1 after relabelling so that colour k is last.
lambda_max of the paper's matrix is < 0 for reading k iff Q_k(w) < 0 for every nonzero mean-zero w
(Neri-Pinto, Prop. 3.6: w -> w|_p is a bijection of the mean-zero hyperplane onto R^p).
Run: python checks.py   (numpy, sympy). Prints ALL PASS at the end or stops at the first failure."""
import itertools
import numpy as np
import sympy as sp

def form(R, lam, w, k=None):
    d = len(R)
    wr = [sum(w[i] * R[i][j] for i in range(d)) for j in range(d)]
    return sum(w[i] * (wr[i] - lam * w[i]) for i in range(d) if i != k)

def irreducible(R):
    d = len(R)
    for s in range(d):
        seen, todo = {s}, [s]
        while todo:
            i = todo.pop()
            for j in range(d):
                if j != i and R[i][j] > 0 and j not in seen:
                    seen.add(j); todo.append(j)
        if len(seen) < d:
            return False
    return True

def fam(d):
    """d >= 4, balance 6."""
    R = [[0] * d for _ in range(d)]
    R[0][0], R[0][1] = 5, 1
    R[1][0], R[1][2] = 5, 1
    R[d - 1][d - 1], R[d - 1][d - 2] = 5, 1
    R[d - 2][d - 1], R[d - 2][d - 3] = 5, 1
    for i in range(2, d - 2):
        R[i][i - 1] += 3; R[i][i + 1] += 3
    return R

def emb(d, x0, x1, x2, x3):
    w = [0] * d; w[0], w[1], w[d - 2], w[d - 1] = x0, x1, x2, x3
    return w

def lam_max_readings(R):
    R = np.array(R, float); d = len(R); lam = R.sum(1)[0]; M = R.T - lam * np.eye(d)
    full_all = np.linalg.eigvalsh((M + M.T) / 2).max()
    B = np.linalg.qr(np.vstack([np.ones(d), np.eye(d)[:d - 1]]).T)[0][:, 1:]
    md = np.linalg.eigvalsh(B.T @ ((M + M.T) / 2) @ B).max()
    mk = []
    for k in range(d):
        perm = [i for i in range(d) if i != k] + [k]; Rp = R[np.ix_(perm, perm)]
        C = np.hstack([np.eye(d - 1), -np.ones((d - 1, 1))]); J = np.diag([1.] * (d - 1) + [0.])
        G = C @ J @ (Rp.T - lam * np.eye(d)) @ C.T; mk.append(np.linalg.eigvalsh((G + G.T) / 2).max())
    return full_all, md, mk

def check(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)
    print("ok  ", msg)

# 1. Literal p = d: the all-ones vector gives 0, so lambda_max >= 0 for every balanced urn (symbolic, d = 2..6).
for d in range(2, 7):
    Rs = sp.Matrix(d, d, lambda i, j: sp.Symbol(f"r{i}{j}"))
    lam = sp.Symbol("lam")
    Rb = Rs.subs({sp.Symbol(f"r{i}{d-1}"): lam - sum(sp.Symbol(f"r{i}{j}") for j in range(d - 1)) for i in range(d)})
    one = sp.ones(d, 1)
    val = sp.simplify((one.T * (Rb.T - lam * sp.eye(d)) * one)[0])
    check(val == 0, f"1^T (R^T - lam I) 1 = 0 for a general balanced {d}x{d} matrix")

# 2. Two colours: every reading equals -(R01 + R10) times the norm.
lam, r, s, t = sp.symbols("lam r s t")
R2 = [[lam - r, r], [s, lam - s]]
w2 = [t, -t]
check(sp.expand(form(R2, lam, w2) + (r + s) * 2 * t**2) == 0, "d = 2, p = d on mean zero: Q = -(r+s)|w|^2")
check(sp.expand(form(R2, lam, w2, 1) + (r + s) * t**2) == 0, "d = 2, colour 1 omitted: Q = -(r+s) w_0^2")
check(sp.expand(form(R2, lam, w2, 0) + (r + s) * t**2) == 0, "d = 2, colour 0 omitted: Q = -(r+s) w_1^2")

# 3. The family, d >= 5: on vectors supported by colours 0, 1, d-2, d-1 the forms depend only on the 4x4 block
#    and split as f(a, b) + f(e, c), f(x, y) = -x^2 + 6xy - 6y^2; for d = 4 add 2bc (or bc for colour 1 or 2 omitted).
a, b, c, e = sp.symbols("a b c e")
f = lambda x, y: -x**2 + 6 * x * y - 6 * y**2
for d in range(4, 10):
    R = fam(d); w = emb(d, a, b, c, e)
    corr = 0 if d >= 5 else 1
    full = sp.expand(form(R, 6, w))
    check(sp.expand(full - (f(a, b) + f(e, c) + 2 * corr * b * c)) == 0, f"d = {d}: Q = f(a,b) + f(e,c) + {2*corr} bc")
    check(sp.expand(form(R, 6, w, 0) - (b * (a - 6 * b) + f(e, c) + 2 * corr * b * c)) == 0,
          f"d = {d}: colour 0 omitted, Q = b(a - 6b) + f(e,c) + {2*corr} bc")
    check(sp.expand(form(R, 6, w, 1) - (a * (5 * b - a) + f(e, c) + corr * b * c)) == 0,
          f"d = {d}: colour 1 omitted, Q = a(5b - a) + f(e,c) + {corr} bc")
    for k in range(2, d - 2):
        check(sp.expand(form(R, 6, w, k) - full) == 0, f"d = {d}: middle colour {k} omitted, same form")

# 4. Exact integer witnesses for the family, d = 4..60, every reading; tenability and irreducibility.
for d in range(4, 61):
    R = fam(d)
    assert all(sum(row) == 6 for row in R) and all(x >= 0 for row in R for x in row) and irreducible(R), d
    W = {None: emb(d, 2, 1, -1, -2), 0: emb(d, -3, 0, 1, 2), 1: emb(d, -1, -1, 1, 1),
         d - 2: emb(d, -1, -1, 1, 1), d - 1: emb(d, -2, -1, 0, 3)}
    vals = {}
    for k in [None] + list(range(d)):
        w = W.get(k, W[None])
        assert sum(w) == 0
        vals[k] = form(R, 6, w, k)
        assert vals[k] > 0, (d, k, vals[k])
    exp = {None: 2, 0: 2, 1: 2, d - 2: 2, d - 1: 2} if d == 4 else {None: 4, 0: 2, 1: 3, d - 2: 3, d - 1: 2}
    assert all(vals[k] == exp.get(k, 4) for k in vals), (d, vals)
check(True, "family d = 4..60: rows sum to 6, entries >= 0, irreducible; every reading has a positive integer witness")
print("     d = 4 values (full, omit 0..3):", [form(fam(4), 6, w, k) for k, w in
      [(None, emb(4, 2, 1, -1, -2)), (0, emb(4, -3, 0, 1, 2)), (1, emb(4, -1, -1, 1, 1)), (2, emb(4, -1, -1, 1, 1)), (3, emb(4, -2, -1, 0, 3))]])

# 5. Three colours, balance 100.
T3 = [[0, 1, 99], [1, 99, 0], [36, 0, 64]]
check(all(sum(row) == 100 for row in T3) and min(min(r) for r in T3) >= 0 and irreducible(T3), "T3: rows sum to 100, entries >= 0, irreducible")
for k, w, q in [(None, [-1, 3, -2], 11), (0, [-1, 2, -1], 57), (1, [-1, 3, -2], 23), (2, [-1, 5, -4], 9)]:
    check(sum(w) == 0 and form(T3, 100, w, k) == q, f"T3 reading {k}: w = {w}, Q = {q}")

# 5b. A small urn: six colours, balance 6, all non-principal eigenvalues with real part < 3 = lam/2.
S6 = [[0, 1, 0, 5, 0, 0], [0, 0, 0, 6, 0, 0], [1, 0, 5, 0, 0, 0], [0, 0, 0, 5, 1, 0], [0, 0, 5, 0, 0, 1], [0, 0, 6, 0, 0, 0]]
check(all(sum(row) == 6 for row in S6) and min(min(r) for r in S6) >= 0 and irreducible(S6), "S6: rows sum to 6, entries >= 0, irreducible")
for k, w, q in [(None, [0, -1, 2, -2, 0, 1], 4), (0, [-1, 0, 1, -1, 0, 1], 3), (1, [0, -1, 1, -1, 0, 1], 4),
                (2, [0, -1, 3, -2, 0, 0], 2), (3, [0, 0, -2, 3, 0, -1], 2), (4, [-1, 0, 1, -1, 1, 0], 1),
                (5, [-1, 0, 1, -1, 0, 1], 2)]:
    check(sum(w) == 0 and form(S6, 6, w, k) == q, f"S6 reading {k}: w = {w}, Q = {q}")
x, y = sp.symbols("x y")
cp = sp.Matrix(S6).charpoly(x).as_expr()
check(sp.expand(cp - (x - 6) * (x**2 + x + 1) * (x**3 - 5 * x**2 + 5 * x + 6)) == 0, "S6: char. polynomial (x-6)(x^2+x+1)(x^3-5x^2+5x+6)")
check(sp.expand((x**3 - 5 * x**2 + 5 * x + 6).subs(x, y + 3)) == y**3 + 4 * y**2 + 2 * y + 3, "S6: cubic at x = y + 3 is y^3 + 4y^2 + 2y + 3 (Hurwitz: 4*2 > 3)")

# 6. Relabelling: the full reading is invariant and reading k depends only on which colour is last.
rng = np.random.default_rng(1)
R = fam(6)
for _ in range(200):
    p = rng.permutation(6); Rp = [[R[p[i]][p[j]] for j in range(6)] for i in range(6)]
    w = [int(x) for x in rng.integers(-5, 6, size=5)]; w.append(-sum(w))
    wp = [w[p[i]] for i in range(6)]
    assert form(Rp, 6, wp) == form(R, 6, w)
    assert form(Rp, 6, wp, 5) == form(R, 6, w, int(p[5]))
check(True, "relabelling invariance of the readings (200 random permutations, d = 6)")

# 7. Floating-point eigenvalues for the record (the paper's lambda_max for each reading).
print("     d, lambda_max over R^d, mean-zero p = d, min over omitted colour of p = d - 1, max over omitted colour")
for d in range(4, 11):
    fa, md, mk = lam_max_readings(fam(d))
    print(f"     {d:2d}  {fa:9.5f}  {md:9.5f}  {min(mk):9.5f}  {max(mk):9.5f}")
fa, md, mk = lam_max_readings(T3)
print(f"     T3  {fa:9.5f}  {md:9.5f}  {np.round(mk, 5)}")
fa, md, mk = lam_max_readings(fam(4))
check(abs(md - (3 * np.sqrt(2) - 4)) < 1e-12, "d = 4: mean-zero p = d value is 3 sqrt(2) - 4 (numerically)")

# 8. Adapted inner product (Proposition 5.1): gamma = max Re of the spectrum of R on the mean-zero hyperplane H;
#    a Lyapunov solution P gives <w(R - lam I), w>_P <= -A ||w||_P^2 on H for A < lam - gamma, and no P positive
#    definite on H does better than lam - gamma.
from scipy.linalg import solve_continuous_lyapunov
def on_H(R):
    R = np.array(R, float); d = len(R); lam = R.sum(1)[0]
    B = np.linalg.qr(np.vstack([np.ones(d), np.eye(d)[:d - 1]]).T)[0][:, 1:]   # columns: orthonormal basis of H
    L = B.T @ (R - lam * np.eye(d)).T @ B        # w = v B^T, w(R - lam I) = v (B^T (R - lam I)^T B)^T B^T
    return L.T, lam                               # row-vector action v -> v L.T
for name, R in [("fam4", fam(4)), ("fam5", fam(5)), ("fam8", fam(8)), ("T3", T3), ("S6", S6)]:
    Lr, lam = on_H(R)
    gamma = lam + np.linalg.eigvals(Lr).real.max()
    ev = np.sort_complex(np.linalg.eigvals(np.array(R, float)))
    A = 0.999 * (lam - gamma)
    M = Lr + A * np.eye(len(Lr))                  # row action; P solves M P + P M^T = -I
    P = solve_continuous_lyapunov(M, -np.eye(len(Lr)))
    check(np.linalg.eigvalsh((P + P.T) / 2).min() > 0, f"{name}: Lyapunov P positive definite on H")
    S = Lr @ P; S = (S + S.T) / 2 + A * P          # v Lr P v^T + A v P v^T <= 0 for all v
    check(np.linalg.eigvalsh(S).max() < 1e-9, f"{name}: adapted contractivity with A = 0.999 (lam - gamma) = {A:.4f}; lam = {lam:g}, gamma = {gamma:.4f}, gamma/lam = {gamma/lam:.4f}")
    print("     spectrum of R:", np.round(ev, 4))
print("ALL PASS")

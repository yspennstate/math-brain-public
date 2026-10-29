"""T240 C9 (post-exit recovery), lead scratch, agent H.

Validated first-order integration of the full seven-overlap erf ODE (eta^2 term included) with exact outward
interval arithmetic (iv_exact, 160-bit fixed point). Floats only choose the reference path, the frames and the
step sizes; every checked inequality is an exact interval or rational comparison.

Error bound on segment k, as in C7: z = P_k^{-1}(x - xhat), D+|z| <= mu_k |z| + d_k, where xhat is the cubic
Hermite interpolant of rational nodes, d_k bounds |P_k^{-1}(xhat' - f(xhat))| over the segment and mu_k bounds
the Euclidean log norm of P_k^{-1} J P_k over an a priori box E_k verified to contain every solution.
Only first-order jets are used: the defect's time derivative xhat'' - J(X) xhat' is enclosed with the plain
interval Jacobian over the Hermite range box X.
"""
import sys, json, math, time
sys.path[:0] = ['.']
from fractions import Fraction as F
from math import isqrt
import numpy as np
from scipy.integrate import solve_ivp
from iv_exact import I, S
import iv_scm, fdrive

N = 7
ETA = I(I.of('0.4999999999').lo, I.of('0.5000000001').hi)     # C6/C7's interval E
ETA_F = 0.5
G64 = 1 << 64
TEACHER = [F(1), F(0), F(1), F(1), F(0), F(0), F(1)]

def up(x): return F(-((-x.numerator * G64) // x.denominator), G64)
def hi(v): return F(v.hi, S)
def lo(v): return F(v.lo, S)
def iv(a, b): return I(I.of(a).lo, I.of(b).hi)
def pm(r): return iv(-r, r)
def maxabs(v): return F(v.maxabs(), S)
def hull(a, b): return I(min(a.lo, b.lo), max(a.hi, b.hi))

def norm2_up(vec):
    s2 = sum(v.maxabs() ** 2 for v in vec)
    root = isqrt(s2)
    if root * root < s2: root += 1
    return F(root, S)

def matvec(M, vec): return [sum((I.of(M[i][j]) * vec[j] for j in range(len(vec))), I.of(0)) for i in range(len(M))]
def mm_rat_iv(A, B): return [[sum((I.of(A[i][l]) * B[l][j] for l in range(len(B))), I.of(0)) for j in range(len(B[0]))] for i in range(len(A))]
def mm_iv_rat(B, A): return [[sum((B[i][l] * I.of(A[l][j]) for l in range(len(A))), I.of(0)) for j in range(len(A[0]))] for i in range(len(B))]

def lognorm_up(B):   # Gershgorin bound of lambda_max of the symmetric part, B an interval matrix
    n = len(B)
    Ss = [[(B[i][j] + B[j][i]) * I.of(F(1, 2)) for j in range(n)] for i in range(n)]
    return max(hi(Ss[i][i]) + sum(maxabs(Ss[i][j]) for j in range(n) if j != i) for i in range(n))

def invert_rational(a):
    n = len(a)
    a = [list(row) + [F(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        p = next(i for i in range(j, n) if a[i][j])
        a[j], a[p] = a[p], a[j]
        d = a[j][j]; a[j] = [v / d for v in a[j]]
        for i in range(n):
            if i != j:
                d = a[i][j]; a[i] = [v - d * w for v, w in zip(a[i], a[j])]
    return [row[n:] for row in a]

def posdef(D):   # exact rational LDL^T: all pivots > 0
    n = len(D); A = [row[:] for row in D]
    for k in range(n):
        if A[k][k] <= 0: return False
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]
            for j in range(k + 1, n): A[i][j] -= m * A[k][j]
    return True

def opnorm2_up(M):   # upper bound of the spectral norm of an exact rational matrix
    n = len(M)
    G = [[sum(M[k][i] * M[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    lam = float(max(np.linalg.eigvalsh(np.array([[float(G[i][j]) for j in range(n)] for i in range(n)]))))
    lu = F(lam) * (1 + F(1, 10 ** 12)) + F(1, 10 ** 30)
    while not posdef([[(lu if i == j else 0) - G[i][j] for j in range(n)] for i in range(n)]):
        lu = lu * (1 + F(1, 10 ** 9)) + F(1, 10 ** 20)
    lu = up(lu)
    r = F(math.sqrt(float(lu)) * (1 + 1e-14))
    while r * r < lu: r *= 1 + F(1, 10 ** 12)
    return up(r)

def expu(x):
    if x <= 0: return up(1 + x + x * x / 2)
    assert x < F(1, 2)
    return up(1 / (1 - x))

def drv(box, eta=ETA):
    return iv_scm.full_driver(iv_scm.variables(box), eta)

def f_point(x, eta=ETA):
    # values only: zero-length jets (the derivative part is never read here)
    return [r.v for r in iv_scm.full_driver([iv_scm.J(I.of(v), []) for v in x], eta)]
def jv_box(box, vel, eta=ETA):
    # forward AD with the single interval seed vel: encloses J(x) v for all x in box, v in vel
    return [r.d[0] for r in iv_scm.full_driver([iv_scm.J(box[i], [vel[i]]) for i in range(N)], eta)]
def jac_box(box, eta=ETA):
    d = drv(box, eta)
    return [[d[i].d[j] for j in range(N)] for i in range(N)]

def frame(Jf):
    """Real eigenbasis (complex pairs as real/imaginary parts), columns normalized; rational P and exact inverse."""
    w, V = np.linalg.eig(Jf)
    cols = []; used = set()
    for k in np.argsort(-w.real):
        if k in used: continue
        if abs(w[k].imag) < 1e-12:
            v = np.real(V[:, k]); cols.append(v / np.linalg.norm(v)); used.add(k)
        else:
            kk = [j for j in range(len(w)) if j not in used and j != k and abs(w[j] - np.conj(w[k])) < 1e-9][0]
            v = V[:, k]; sc = np.linalg.norm(np.concatenate([v.real, v.imag])) / math.sqrt(2)
            cols += [v.real / sc, v.imag / sc]; used |= {k, kk}
    P = np.column_stack(cols)
    Pr = [[F(float(P[a][b])) for b in range(N)] for a in range(N)]
    return Pr, invert_rational(Pr)

# ---------- Hermite pieces ----------
def hermite_coeffs(x0, x1, m0, m1, h):
    out = []
    for i in range(N):
        p0, p1, d0, d1 = x0[i], x1[i], h * m0[i], h * m1[i]
        out.append([p0, d0, -3 * p0 - 2 * d0 + 3 * p1 - d1, 2 * p0 + d0 - 2 * p1 + d1])
    return out

def poly_range(a, c, w):
    n = len(a); b = [F(0)] * n
    for k in range(n):
        for j in range(k, n): b[k] += a[j] * math.comb(j, k) * c ** (j - k)
    rad = sum(abs(b[k]) * w ** k for k in range(1, n))
    return iv(b[0] - rad, b[0] + rad), b[0]

def deriv(a): return [k * a[k] for k in range(1, len(a))]

def segment(x0, x1, m0, m1, h, P, Pinv, r0, nsub):
    A = hermite_coeffs(x0, x1, m0, m1, h)
    A1 = [deriv(a) for a in A]; A2 = [deriv(a) for a in A1]
    w = F(1, 2 * nsub); dmax = F(0); boxes = []
    for j in range(nsub):
        sc = F(2 * j + 1, 2 * nsub)
        X = []; xc = []; V = []; vc = []; Acc = []
        for i in range(N):
            rX, cX = poly_range(A[i], sc, w); X.append(rX); xc.append(cX)
            rV, cV = poly_range(A1[i], sc, w); V.append(rV * I.of(1 / h)); vc.append(cV / h)
            rA, _ = poly_range(A2[i], sc, w); Acc.append(rA * I.of(1 / (h * h)))
        fc = f_point(xc)
        dc = [I.of(vc[i]) - fc[i] for i in range(N)]
        Jx = jac_box(X)
        dprime = [Acc[i] - sum((Jx[i][k] * V[k] for k in range(N)), I.of(0)) for i in range(N)]
        drange = [dc[i] + dprime[i] * pm(w * h) for i in range(N)]
        dmax = max(dmax, norm2_up(matvec(Pinv, drange)))
        boxes.append(X)
    X = [I(min(b[i].lo for b in boxes), max(b[i].hi for b in boxes)) for i in range(N)]
    dk = up(dmax)
    R = up(2 * r0 + 2 * dk * h + F(1, 10 ** 15))
    for attempt in range(6):
        E = [X[i] + sum((I.of(P[i][k]) * pm(R) for k in range(N)), I.of(0)) for i in range(N)]
        mu = lognorm_up(mm_iv_rat(mm_rat_iv(Pinv, jac_box(E)), P))
        mup = max(mu, F(0))
        if mu * h > F(1, 2): return None
        rmax = up((r0 + dk * h) * expu(mup * h))
        if rmax < R:
            r1 = up(expu(mu * h) * r0 + dk * h * expu(mup * h))
            return {'d': dk, 'mu': mu, 'R': R, 'r1': r1, 'Xw': max(float(hi(v) - lo(v)) for v in X)}
        R = up(2 * rmax)
    return None

# ---------- reference path ----------
def ff(t, y): return fdrive.f(y, ETA_F)

def build(p0, T, W, hmax=2.0):
    """Rational nodes along the float solution from the exact rational start p0."""
    sol = solve_ivp(ff, (0, T), [float(v) for v in p0], method='DOP853', rtol=1e-13, atol=1e-15, dense_output=True)
    ts = [0.0]
    while ts[-1] < T - 1e-12:
        v = np.linalg.norm(ff(0, sol.sol(ts[-1])))
        ts.append(ts[-1] + min(max(W / v, 0.002), hmax, T - ts[-1]))
    tq = [F(0)] + [F(t).limit_denominator(1 << 20) for t in ts[1:]]
    nodes = [list(p0)] + [[F(float(v)) for v in sol.sol(float(t))] for t in tq[1:]]
    slopes = [[F(float(v)) for v in ff(0, np.array([float(u) for u in x]))] for x in nodes]
    return tq, nodes, slopes

def fl(x): return np.array([float(u) for u in x])

def run_chain(tq, nodes, slopes, P0, Pinv0, r_in, k0, k1, out, nsub=6):
    r = F(r_in); P, Pinv = P0, Pinv0
    t0 = time.time()
    with open(out, 'w') as fh:
        fh.write(json.dumps({'piece': [k0, k1], 'r_in': str(r), 't0': float(tq[k0]), 't1': float(tq[k1])}) + '\n')
        for k in range(k0, k1):
            h = tq[k + 1] - tq[k]
            res = segment(nodes[k], nodes[k + 1], slopes[k], slopes[k + 1], h, P, Pinv, r, nsub)
            if res is None:
                fh.write(json.dumps({'k': k, 'fail': True, 't': float(tq[k]), 'r': float(r)}) + '\n'); return None
            Pn, Pinvn = frame(fdrive.jac(fl(nodes[k + 1]), ETA_F))
            sw = opnorm2_up([[sum(Pinvn[i][l] * P[l][j] for l in range(N)) for j in range(N)] for i in range(N)])
            r = up(res['r1'] * sw); P, Pinv = Pn, Pinvn
            fh.write(json.dumps({'k': k, 't': float(tq[k]), 'h': float(h), 'd': float(res['d']), 'mu': float(res['mu']),
                                 'R': float(res['R']), 'r': float(r), 'sw': float(sw), 'Xw': res['Xw'],
                                 'el': round(time.time() - t0, 1)}) + '\n'); fh.flush()
        fh.write(json.dumps({'piece_done': [k0, k1], 'r_out': str(r), 'r_out_f': float(r)}) + '\n')
    return r, P, Pinv

"""T240 target 1, deterministic entry: validated first-order integration of the symmetric (q,c,r) ODE
from (q0,0,0) with a piecewise-constant local eigenframe, ending inside a certified contracting trap ball
around the C6 plateau. Reviewer/lead scratch (agent H). Floats only choose the reference path,
frames and step sizes; every inequality that is checked uses exact outward interval arithmetic (iv_exact).

Error bound on segment k: z = P_k^{-1}(x - xhat), d|z|/dt <= mu_k |z| + d_k, where xhat is the cubic Hermite
interpolant of float nodes, d_k bounds |P_k^{-1}(xhat' - f(xhat))| and mu_k bounds the log norm of
P_k^{-1} J P_k over a box E_k verified a posteriori to contain the solution.
Usage: python entry.py Q0 T W OUT.jsonl
"""
import sys, json, time, math
sys.path[:0] = ['scripts', '.']
from fractions import Fraction as F
from math import isqrt
import numpy as np
from scipy.integrate import solve_ivp
from iv_exact import I, S
import iv_scm, iv_h2
import check_symmetric_closed as cs
from certify_plateau import invert_rational

ETA = I(I.of('0.4999999999').lo, I.of('0.5000000001').hi)
ETA_F = 0.5
XSTAR = [F('0.36771969907760643'), F('0.32538554792403124'), F('0.4143941508524791')]
G64 = 1 << 64

def up(x):   # rational upper rounding to the 2^-64 grid
    return F(-((-x.numerator * G64) // x.denominator), G64)
def hi(v): return F(v.hi, S)
def lo(v): return F(v.lo, S)
def iv(a, b): return I(I.of(a).lo, I.of(b).hi)
def pm(r): return iv(-r, r)
def maxabs(v): return F(v.maxabs(), S)

def norm2_up(vec):   # upper bound of the Euclidean norm of an interval vector
    s2 = sum(v.maxabs() ** 2 for v in vec)          # units S^2
    root = isqrt(s2)
    if root * root < s2: root += 1
    return F(root, S)

def matvec_rat(M, vec):  # rational matrix times interval vector
    return [sum((I.of(M[i][j]) * vec[j] for j in range(len(vec))), I.of(0)) for i in range(len(M))]

def matmul_rat_iv(A, B):  # rational A times interval B
    n = len(A); m = len(B[0])
    return [[sum((I.of(A[i][l]) * B[l][j] for l in range(len(B))), I.of(0)) for j in range(m)] for i in range(n)]

def matmul_iv_rat(B, A):
    n = len(B); m = len(A[0])
    return [[sum((B[i][l] * I.of(A[l][j]) for l in range(len(A))), I.of(0)) for j in range(m)] for i in range(n)]

def lognorm_up(B):   # Gershgorin bound of lambda_max(sym B), B interval matrix
    n = len(B)
    Ssym = [[(B[i][j] + B[j][i]) * I.of(F(1, 2)) for j in range(n)] for i in range(n)]
    return max(hi(Ssym[i][i]) + sum(maxabs(Ssym[i][j]) for j in range(n) if j != i) for i in range(n))

def det3(D):
    return (D[0][0] * (D[1][1] * D[2][2] - D[1][2] * D[2][1]) - D[0][1] * (D[1][0] * D[2][2] - D[1][2] * D[2][0])
            + D[0][2] * (D[1][0] * D[2][1] - D[1][1] * D[2][0]))

def opnorm2_up(M):   # exact rational M (3x3): lu - M^T M proved positive definite by exact Sylvester minors
    n = len(M)
    G = [[sum(M[k][i] * M[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    lam = float(max(np.linalg.eigvalsh(np.array([[float(G[i][j]) for j in range(n)] for i in range(n)]))))
    lu = F(lam) * (1 + F(1, 10 ** 12)) + F(1, 10 ** 30)
    while True:
        D = [[(lu if i == j else 0) - G[i][j] for j in range(n)] for i in range(n)]
        if D[0][0] > 0 and D[0][0] * D[1][1] - D[0][1] * D[1][0] > 0 and det3(D) > 0: break
        lu = lu * (1 + F(1, 10 ** 9)) + F(1, 10 ** 20)
    lu = up(lu)
    r = F(math.sqrt(float(lu)) * (1 + 1e-14))
    while r * r < lu: r *= 1 + F(1, 10 ** 12)
    return up(r)

def expu(x):   # upper bound of e^x, x rational
    if x <= 0: return up(1 + x + x * x / 2)
    assert x < F(1, 2)
    return up(1 / (1 - x))

# ---------- Hermite polynomial pieces (exact rationals, variable s in [0,1]) ----------
def hermite_coeffs(x0, x1, m0, m1, h):
    """Per component: coefficients a0..a3 of xhat(s)."""
    out = []
    for i in range(3):
        p0, p1, d0, d1 = x0[i], x1[i], h * m0[i], h * m1[i]
        a0 = p0; a1 = d0
        a2 = -3 * p0 - 2 * d0 + 3 * p1 - d1
        a3 = 2 * p0 + d0 - 2 * p1 + d1
        out.append([a0, a1, a2, a3])
    return out

def poly_shift(a, c):   # coefficients of p(c+u) in u
    n = len(a); b = [F(0)] * n
    for k in range(n):
        for j in range(k, n):
            b[k] += a[j] * math.comb(j, k) * c ** (j - k)
    return b

def poly_range(a, c, w):  # range of p over [c-w, c+w] as interval
    b = poly_shift(a, c)
    rad = sum(abs(b[k]) * w ** k for k in range(1, len(b)))
    return iv(b[0] - rad, b[0] + rad), b[0]

def deriv(a): return [k * a[k] for k in range(1, len(a))]

def frame(J):
    w, V = np.linalg.eig(J)
    if np.all(np.abs(w.imag) < 1e-12):
        P = np.real(V); P = P / np.linalg.norm(P, axis=0)
    else:
        i = int(np.argmax(w.imag)); v = V[:, i]
        j = [k for k in range(3) if abs(w[k].imag) < 1e-12][0]
        sc = np.linalg.norm(np.concatenate([v.real, v.imag])) / math.sqrt(2)
        P = np.column_stack([v.real / sc, v.imag / sc, np.real(V[:, j]) / np.linalg.norm(V[:, j])])
    Pr = [[F(float(P[a][b])) for b in range(3)] for a in range(3)]
    return Pr, invert_rational(Pr)

ff = lambda t, y: cs.closed(y[0], y[1], y[2], ETA_F)[3:]
def jac_f(x, h=1e-7):
    Jm = np.zeros((3, 3))
    for k in range(3):
        d = np.zeros(3); d[k] = h; Jm[:, k] = (ff(0, x + d) - ff(0, x - d)) / (2 * h)
    return Jm

def point_f(x):
    return [r.v for r in iv_scm.symmetric_driver([I.of(v) for v in x], ETA)]

def jac_box_centered(box):
    """Jacobian enclosure over an interval box: J(c) + H(box)(box - c)."""
    c = [F(v.lo + v.hi, 2 * S) for v in box]
    jc = iv_scm.symmetric_driver([I.of(v) for v in c], ETA)
    hb = iv_h2.symmetric_driver(box, ETA)
    dx = [box[k] - I.of(c[k]) for k in range(3)]
    Jm = [[jc[i].d[j] + sum((hb[i].h[j][k] * dx[k] for k in range(3)), I.of(0)) for j in range(3)] for i in range(3)]
    # also intersect with the plain first-order enclosure
    jb = iv_scm.symmetric_driver(box, ETA)
    out = []
    for i in range(3):
        row = []
        for j in range(3):
            a, b = Jm[i][j], jb[i].d[j]
            row.append(I(max(a.lo, b.lo), min(a.hi, b.hi)))
        out.append(row)
    return out

def segment(x0, x1, m0, m1, h, P, Pinv, r0, nsub):
    A = hermite_coeffs(x0, x1, m0, m1, h)
    A1 = [deriv(a) for a in A]; A2 = [deriv(a) for a in A1]
    w = F(1, 2 * nsub)
    dmax = F(0); boxes = []
    for j in range(nsub):
        sc = F(2 * j + 1, 2 * nsub)
        X = []; xc = []; V = []; Acc = []; vc = []
        for i in range(3):
            rX, cX = poly_range(A[i], sc, w); X.append(rX); xc.append(cX)
            rV, cV = poly_range(A1[i], sc, w); V.append(rV * I.of(1 / h)); vc.append(cV / h)
            rA, _ = poly_range(A2[i], sc, w); Acc.append(rA * I.of(1 / (h * h)))
        jc = iv_scm.symmetric_driver([I.of(v) for v in xc], ETA)
        fc = [row.v for row in jc]
        dc = [I.of(vc[i]) - fc[i] for i in range(3)]
        hb = iv_h2.symmetric_driver(X, ETA)
        dxs = [X[k] - I.of(xc[k]) for k in range(3)]
        Jx = [[jc[i].d[j] + sum((hb[i].h[j][k] * dxs[k] for k in range(3)), I.of(0)) for j in range(3)] for i in range(3)]
        dprime = [Acc[i] - sum((Jx[i][k] * V[k] for k in range(3)), I.of(0)) for i in range(3)]
        drange = [dc[i] + dprime[i] * pm(w * h) for i in range(3)]
        dmax = max(dmax, norm2_up(matvec_rat(Pinv, drange)))
        boxes.append(X)
    X = [I(min(b[i].lo for b in boxes), max(b[i].hi for b in boxes)) for i in range(3)]
    dk = up(dmax)
    R = up(2 * r0 + 2 * dk * h + F(1, 10 ** 15))
    for attempt in range(6):
        E = [X[i] + sum((I.of(P[i][k]) * pm(R) for k in range(3)), I.of(0)) for i in range(3)]
        Jm = jac_box_centered(E)
        mu = lognorm_up(matmul_iv_rat(matmul_rat_iv(Pinv, Jm), P))
        mup = max(mu, F(0))
        if mu * h > F(1, 2): return None
        rmax = up((r0 + dk * h) * expu(mup * h))
        if rmax < R:
            r1 = up(expu(mu * h) * r0 + dk * h * expu(mup * h))
            return {'d': dk, 'mu': mu, 'R': R, 'r1': r1, 'Xw': max(float(hi(v) - lo(v)) for v in X)}
        R = up(2 * rmax)
    return None

def trap(Pstar, Pinv_star, rho, nsplit):
    xs = XSTAR
    worst = None
    cells = [(-rho + 2 * rho * F(a, nsplit), -rho + 2 * rho * F(a + 1, nsplit)) for a in range(nsplit)]
    for c0 in cells:
        for c1 in cells:
            for c2 in cells:
                z = [iv(*c0), iv(*c1), iv(*c2)]
                box = [I.of(xs[i]) + sum((I.of(Pstar[i][k]) * z[k] for k in range(3)), I.of(0)) for i in range(3)]
                Jm = jac_box_centered(box)
                mu = lognorm_up(matmul_iv_rat(matmul_rat_iv(Pinv_star, Jm), Pstar))
                worst = mu if worst is None else max(worst, mu)
    res = norm2_up(matvec_rat(Pinv_star, point_f(xs)))
    return worst, res

def build(q0, T, W):
    q0 = F(q0); T = float(T); W = float(W)
    sol = solve_ivp(ff, (0, T), [float(q0), 0.0, 0.0], method='DOP853', rtol=1e-13, atol=1e-15, dense_output=True)
    ts = [0.0]
    while ts[-1] < T - 1e-12:
        v = np.linalg.norm(ff(0, sol.sol(ts[-1])))
        h = min(max(W / v, 0.002), 2.0, T - ts[-1])
        ts.append(ts[-1] + h)
    tq = [F(t).limit_denominator(1 << 20) for t in ts]
    tq[0] = F(0)
    nodes = [[q0, F(0), F(0)]] + [[F(float(v)) for v in sol.sol(float(t))] for t in tq[1:]]
    slopes = [[F(float(v)) for v in ff(0, np.array([float(u) for u in x]))] for x in nodes]
    return tq, nodes, slopes

def fl(x): return np.array([float(u) for u in x])

def run_piece(q0, T, W, out, k0, k1, r_in, nsub=6):
    tq, nodes, slopes = build(q0, T, W)
    k1 = min(int(k1), len(tq) - 1); k0 = int(k0)
    r = F(r_in)
    P, Pinv = frame(jac_f(fl(nodes[k0])))
    t0 = time.time()
    with open(out, 'w') as fh:
        fh.write(json.dumps({'piece': [k0, k1], 'r_in': str(r), 't0': float(tq[k0]), 't1': float(tq[k1]), 'nseg_total': len(tq) - 1}) + '\n')
        for k in range(k0, k1):
            h = tq[k + 1] - tq[k]
            res = segment(nodes[k], nodes[k + 1], slopes[k], slopes[k + 1], h, P, Pinv, r, nsub)
            if res is None:
                fh.write(json.dumps({'k': k, 'fail': True, 't': float(tq[k])}) + '\n'); print('FAIL at', float(tq[k])); return
            Pn, Pinvn = frame(jac_f(fl(nodes[k + 1])))
            sw = opnorm2_up([[sum(Pinvn[i][l] * P[l][j] for l in range(3)) for j in range(3)] for i in range(3)])
            r = up(res['r1'] * sw)
            P, Pinv = Pn, Pinvn
            rec = {'k': k, 't': float(tq[k]), 'h': float(h), 'd': float(res['d']), 'mu': float(res['mu']), 'R': float(res['R']),
                   'r': float(r), 'sw': float(sw), 'Xw': res['Xw'], 'el': round(time.time() - t0, 1)}
            fh.write(json.dumps(rec) + '\n'); fh.flush()
        fh.write(json.dumps({'piece_done': [k0, k1], 'r_out': str(r), 'r_out_f': float(r)}) + '\n')

def run_trap(q0, T, W, out, r_end):
    tq, nodes, slopes = build(q0, T, W)
    K = len(tq) - 1
    P, Pinv = frame(jac_f(fl(nodes[K])))
    r = F(r_end)
    Ps, Pinvs = frame(jac_f(fl(XSTAR)))
    diff = [I.of(nodes[K][i] - XSTAR[i]) for i in range(3)]
    off = norm2_up(matvec_rat(Pinvs, diff))
    swf = opnorm2_up([[sum(Pinvs[i][l] * P[l][j] for l in range(3)) for j in range(3)] for i in range(3)])
    need = up(off + swf * r)
    result = {'r_end': str(r), 'offset': float(off), 'need_rho': float(need), 'K': K}
    with open(out, 'w') as fh:
        for rho in [F(2, 10 ** 4), F(3, 10 ** 4), F(5, 10 ** 4), F(1, 10 ** 3)]:
            if rho <= need: continue
            for ns in (1, 2, 4, 8):
                mu, resid = trap(Ps, Pinvs, rho, ns)
                ok = mu < 0 and resid < -mu * rho
                result['trap_%s_%d' % (float(rho), ns)] = {'mu': float(mu), 'resid': float(resid), 'ok': bool(ok)}
                fh.write(json.dumps(result) + '\n'); fh.flush()
                if ok:
                    result['PASS'] = {'rho': str(rho), 'nsplit': ns, 'mu': str(mu)}
                    fh.write(json.dumps(result) + '\n'); return

if __name__ == '__main__':
    from resource_limits import apply_limits; apply_limits()
    mode = sys.argv[1]
    if mode == 'count':
        tq, nodes, slopes = build(*sys.argv[2:5])
        print(len(tq) - 1, [(k, float(tq[k])) for k in range(0, len(tq), max(1, len(tq) // 12))])
    elif mode == 'piece': run_piece(*sys.argv[2:9])
    elif mode == 'trap': run_trap(*sys.argv[2:7])

"""T240 entry on a nondegenerate eta cell [ETA0 - WE, ETA0 + WE]. Reviewer/lead scratch (agent H).

Reference affine in eta: xhat(t, eta) = x0(t) + (eta - ETA0) y(t), with x0 the cubic Hermite interpolant of the float
eta0 path (same nodes as entry.py) and y the cubic Hermite interpolant of a float sensitivity d x / d eta. The defect
delta(t, eta) = xhat_t - f(xhat, eta) is enclosed on each sub-box by the two-variable mean value form
    delta(t_c, eta0) + d_t delta(box) (t - t_c) + d_eta delta(box) (eta - eta0),
    d_t delta = xhat_tt - f_x(xhat, eta) xhat_t,   d_eta delta = y_t - f_x(xhat, eta) y - f_eta(xhat, eta).
Everything else (frames, log norm over the a-priori box, switch norms, exponential bounds) is entry.py with eta an
interval. The trap ball is centred on xs0 + (eta - eta0) ys with ys = -f_x^-1 f_eta at xs0 (float, then exact rational).
Usage: python entry_eta.py piece ETA0 WE T W OUT K0 K1 R_IN | trap ETA0 WE T W OUT R_END | count ETA0 WE T W
q0 = 1 throughout.
"""
import sys, json, time, os, pickle
sys.path[:0] = ['scripts', '.']
from fractions import Fraction as F
import numpy as np
from scipy.integrate import solve_ivp
from iv_exact import I, S
import iv_scm, iv_h2
import check_symmetric_closed as cs
import entry
from entry import up, iv, pm, norm2_up, matvec_rat, matmul_rat_iv, matmul_iv_rat, lognorm_up, opnorm2_up, expu
from entry import hermite_coeffs, poly_range, deriv, frame, fl
from certify_plateau import invert_rational

def setup(eta0, we):
    global ETA0, WE, H, DH, ETA0F
    ETA0 = F(eta0); WE = F(we); ETA0F = float(ETA0)
    H = iv(ETA0 - WE, ETA0 + WE); DH = pm(WE)
    entry.ETA = H          # jac_box_centered and point_f now range over the whole cell
    entry.ETA_F = ETA0F
    entry.ff = lambda t, y: cs.closed(y[0], y[1], y[2], ETA0F)[3:]

def fe(x, eta): return cs.closed(x[0], x[1], x[2], eta)[3:]

def jac_float(x, eta, h=1e-7):
    return np.column_stack([(fe(x + h * e, eta) - fe(x - h * e, eta)) / (2 * h) for e in np.eye(3)])

def sym4(box, eta):
    """First-order jets in (q, c, r, eta): rows with .v and .d[0:3] = f_x, .d[3] = f_eta."""
    q, c, r, e = iv_scm.variables(list(box) + [eta])
    f = iv_scm.full_driver([q, c, q, r, r, r, r], e)
    return [f[0], f[1], f[3]]

def sym4_h2(box, eta):
    """Second-order jets in (q, c, r, eta) over a box: .h[a][b], index 3 = eta."""
    q, c, r, e = iv_h2.variables(list(box) + [eta])
    f = iv_h2.full_driver([q, c, q, r, r, r, r], e)
    return [f[0], f[1], f[3]]

def build(T, W, eps=1e-5):
    key = 'cache_eta_%s_%s_%s.pkl' % (str(ETA0).replace('/', '_'), T, W)
    if os.path.exists(key):
        return pickle.load(open(key, 'rb'))
    tq, nodes, slopes = entry.build(1, T, W)
    sols = [solve_ivp(lambda t, x, e=e: fe(x, e), (0, float(T)), [1.0, 0, 0], method='DOP853', rtol=1e-13, atol=1e-15,
                      dense_output=True) for e in (ETA0F - eps, ETA0F + eps)]
    ys = [[F(0)] * 3]
    for t in tq[1:]:
        ys.append([F(float(v)) for v in (sols[1].sol(float(t)) - sols[0].sol(float(t))) / (2 * eps)])
    fe_eta = lambda x: (fe(x, ETA0F + 1e-7) - fe(x, ETA0F - 1e-7)) / 2e-7
    yslopes = [[F(float(v)) for v in jac_float(fl(x), ETA0F) @ fl(y) + fe_eta(fl(x))] for x, y in zip(nodes, ys)]
    out = (tq, nodes, slopes, ys, yslopes)
    pickle.dump(out, open(key + '.tmp', 'wb')); os.replace(key + '.tmp', key)
    return out

def segment(x0, x1, m0, m1, y0, y1, n0, n1, h, P, Pinv, r0, nsub):
    A = hermite_coeffs(x0, x1, m0, m1, h); B = hermite_coeffs(y0, y1, n0, n1, h)
    A1 = [deriv(a) for a in A]; A2 = [deriv(a) for a in A1]
    B1 = [deriv(b) for b in B]; B2 = [deriv(b) for b in B1]
    w = F(1, 2 * nsub)
    dmax = F(0); boxes = []
    eta0 = I.of(ETA0)
    for j in range(nsub):
        sc = F(2 * j + 1, 2 * nsub)
        X = []; xc = []; V = []; Acc = []; vc = []; Y = []; VY = []; YTT = []; yc = []; ypc = []
        for i in range(3):
            rX, cX = poly_range(A[i], sc, w); rY, cY = poly_range(B[i], sc, w)
            X.append(rX + DH * rY); xc.append(cX); Y.append(rY); yc.append(cY)
            rV, cV = poly_range(A1[i], sc, w); rVY, cVY = poly_range(B1[i], sc, w)
            V.append((rV + DH * rVY) * I.of(1 / h)); vc.append(cV / h); VY.append(rVY * I.of(1 / h)); ypc.append(cVY / h)
            rA, _ = poly_range(A2[i], sc, w); rAY, _ = poly_range(B2[i], sc, w)
            Acc.append((rA + DH * rAY) * I.of(1 / (h * h))); YTT.append(rAY * I.of(1 / (h * h)))
        # delta at (t_c, eta0): exact point
        fc = iv_scm.symmetric_driver([I.of(v) for v in xc], eta0)
        dc = [I.of(vc[i]) - fc[i].v for i in range(3)]
        # d_t delta over the box, Jacobian by the centred form about xc with eta over the cell
        jcH = iv_scm.symmetric_driver([I.of(v) for v in xc], H)
        hb = iv_h2.symmetric_driver(X, H)
        dxs = [X[k] - I.of(xc[k]) for k in range(3)]
        Jx = [[jcH[i].d[jj] + sum((hb[i].h[jj][k] * dxs[k] for k in range(3)), I.of(0)) for jj in range(3)] for i in range(3)]
        jb = iv_scm.symmetric_driver(X, H)
        Jx = [[I(max(Jx[i][jj].lo, jb[i].d[jj].lo), min(Jx[i][jj].hi, jb[i].d[jj].hi)) for jj in range(3)] for i in range(3)]
        dt = [Acc[i] - sum((Jx[i][k] * V[k] for k in range(3)), I.of(0)) for i in range(3)]
        # d_eta delta = g(t, eta) = y_t - f_x y - f_eta, centred about (t_c, eta0):
        # g in g(t_c, eta0) + d_t g(box) (t - t_c) + d_eta g(box) (eta - eta0), second derivatives from 4-variable jets
        p4 = sym4([I.of(v) for v in xc], eta0)
        gc = [I.of(ypc[i]) - sum((p4[i].d[k] * I.of(yc[k]) for k in range(3)), I.of(0)) - p4[i].d[3]
              for i in range(3)]
        h4 = sym4_h2(X, H)
        gt = []; ge = []
        for i in range(3):
            Hm = h4[i].h
            gt.append(YTT[i]
                      - sum((Hm[jj][k] * V[k] * Y[jj] for jj in range(3) for k in range(3)), I.of(0))
                      - sum((Jx[i][jj] * VY[jj] for jj in range(3)), I.of(0))
                      - sum((Hm[3][k] * V[k] for k in range(3)), I.of(0)))
            ge.append(I.of(0)
                      - sum(((sum((Hm[jj][k] * Y[k] for k in range(3)), I.of(0)) + Hm[jj][3]) * Y[jj] for jj in range(3)), I.of(0))
                      - sum((Hm[3][k] * Y[k] for k in range(3)), I.of(0)) - Hm[3][3])
        de = [gc[i] + gt[i] * pm(w * h) + ge[i] * DH for i in range(3)]
        drange = [dc[i] + dt[i] * pm(w * h) + de[i] * DH for i in range(3)]
        dmax = max(dmax, norm2_up(matvec_rat(Pinv, drange)))
        boxes.append(X)
    X = [I(min(b[i].lo for b in boxes), max(b[i].hi for b in boxes)) for i in range(3)]
    dk = up(dmax)
    R = up(2 * r0 + 2 * dk * h + F(1, 10 ** 15))
    for attempt in range(6):
        E = [X[i] + sum((I.of(P[i][k]) * pm(R) for k in range(3)), I.of(0)) for i in range(3)]
        Jm = entry.jac_box_centered(E)
        mu = lognorm_up(matmul_iv_rat(matmul_rat_iv(Pinv, Jm), P))
        mup = max(mu, F(0))
        if mu * h > F(1, 2): return None
        rmax = up((r0 + dk * h) * expu(mup * h))
        if rmax < R:
            r1 = up(expu(mu * h) * r0 + dk * h * expu(mup * h))
            return {'d': dk, 'mu': mu, 'R': R, 'r1': r1, 'Xw': max(float(entry.hi(v) - entry.lo(v)) for v in X)}
        R = up(2 * rmax)
    return None

def run_piece(T, W, out, k0, k1, r_in, nsub=6):
    tq, nodes, slopes, ys, yslopes = build(T, W)
    k1 = min(int(k1), len(tq) - 1); k0 = int(k0)
    r = F(r_in)
    P, Pinv = frame(entry.jac_f(fl(nodes[k0])))
    t0 = time.time()
    with open(out, 'w') as fh:
        fh.write(json.dumps({'piece': [k0, k1], 'r_in': str(r), 'eta0': str(ETA0), 'we': str(WE), 't0': float(tq[k0]),
                             't1': float(tq[k1]), 'nseg_total': len(tq) - 1}) + '\n')
        for k in range(k0, k1):
            h = tq[k + 1] - tq[k]
            res = segment(nodes[k], nodes[k + 1], slopes[k], slopes[k + 1], ys[k], ys[k + 1], yslopes[k], yslopes[k + 1],
                          h, P, Pinv, r, nsub)
            if res is None:
                fh.write(json.dumps({'k': k, 'fail': True, 't': float(tq[k])}) + '\n'); return
            Pn, Pinvn = frame(entry.jac_f(fl(nodes[k + 1])))
            sw = opnorm2_up([[sum(Pinvn[i][l] * P[l][j] for l in range(3)) for j in range(3)] for i in range(3)])
            r = up(res['r1'] * sw)
            P, Pinv = Pn, Pinvn
            fh.write(json.dumps({'k': k, 't': float(tq[k]), 'h': float(h), 'd': float(res['d']), 'mu': float(res['mu']),
                                 'R': float(res['R']), 'r': float(r), 'sw': float(sw), 'Xw': res['Xw'],
                                 'el': round(time.time() - t0, 1)}) + '\n'); fh.flush()
        fh.write(json.dumps({'piece_done': [k0, k1], 'r_out': str(r), 'r_out_f': float(r)}) + '\n')

def plateau_float():
    x = np.array([float(v) for v in entry.XSTAR])
    for _ in range(40):
        x = x - np.linalg.solve(jac_float(x, ETA0F), fe(x, ETA0F))
    fe_eta = (fe(x, ETA0F + 1e-7) - fe(x, ETA0F - 1e-7)) / 2e-7
    ysx = -np.linalg.solve(jac_float(x, ETA0F), fe_eta)
    return [F(float(v)) for v in x], [F(float(v)) for v in ysx]

def run_trap(T, W, out, r_end):
    tq, nodes, slopes, ys, yslopes = build(T, W)
    K = len(tq) - 1
    P, Pinv = frame(entry.jac_f(fl(nodes[K])))
    xs0, ysx = plateau_float()
    Ps, Pinvs = frame(entry.jac_f(fl(xs0)))
    r = F(r_end)
    diff = [I.of(nodes[K][i] - xs0[i]) + DH * I.of(ys[K][i] - ysx[i]) for i in range(3)]
    off = norm2_up(matvec_rat(Pinvs, diff))
    swf = opnorm2_up([[sum(Pinvs[i][l] * P[l][j] for l in range(3)) for j in range(3)] for i in range(3)])
    need = up(off + swf * r)
    cb = [I.of(xs0[i]) + DH * I.of(ysx[i]) for i in range(3)]
    f0 = iv_scm.symmetric_driver([I.of(v) for v in xs0], I.of(ETA0))
    j4 = sym4(cb, H)
    resv = [f0[i].v + (sum((j4[i].d[k] * I.of(ysx[k]) for k in range(3)), I.of(0)) + j4[i].d[3]) * DH for i in range(3)]
    res = norm2_up(matvec_rat(Pinvs, resv))
    result = {'r_end': str(r), 'offset': float(off), 'need_rho': float(need), 'resid': float(res), 'K': K,
              'eta0': str(ETA0), 'we': str(WE), 'xs0': [str(v) for v in xs0], 'ys': [str(v) for v in ysx]}
    with open(out, 'w') as fh:
        fh.write(json.dumps(result) + '\n'); fh.flush()
        for rho in [F(2, 10 ** 4), F(3, 10 ** 4), F(5, 10 ** 4), F(1, 10 ** 3), F(2, 10 ** 3), F(4, 10 ** 3)]:
            if rho <= need: continue
            for ns in (1, 2, 4):
                worst = None
                cells = [(-rho + 2 * rho * F(a, ns), -rho + 2 * rho * F(a + 1, ns)) for a in range(ns)]
                for c0 in cells:
                    for c1 in cells:
                        for c2 in cells:
                            z = [iv(*c0), iv(*c1), iv(*c2)]
                            box = [cb[i] + sum((I.of(Ps[i][k]) * z[k] for k in range(3)), I.of(0)) for i in range(3)]
                            Jm = entry.jac_box_centered(box)
                            mu = lognorm_up(matmul_iv_rat(matmul_rat_iv(Pinvs, Jm), Ps))
                            worst = mu if worst is None else max(worst, mu)
                ok = worst < 0 and res < -worst * rho
                result['trap_%s_%d' % (float(rho), ns)] = {'mu': float(worst), 'ok': bool(ok)}
                fh.write(json.dumps(result) + '\n'); fh.flush()
                if ok:
                    result['PASS'] = {'rho': str(rho), 'nsplit': ns, 'mu': str(worst)}
                    fh.write(json.dumps(result) + '\n'); return

if __name__ == '__main__':
    from resource_limits import apply_limits; apply_limits()
    mode = sys.argv[1]
    setup(sys.argv[2], sys.argv[3])
    if mode == 'count':
        b = build(sys.argv[4], sys.argv[5]); print(len(b[0]) - 1, 'max |y| %.4f' % max(np.linalg.norm(fl(y)) for y in b[3]))
    elif mode == 'piece': run_piece(*sys.argv[4:10])
    elif mode == 'trap': run_trap(*sys.argv[4:8])

"""Independent float checks of T240 C8 (agent A, 18 Oct). Reads the lead's scripts and logs, writes nothing there.
A: interval jets (values, first and second derivatives incl. eta) contain finite-difference values at points.
B: sampled defect |Pinv_k delta(t, eta)| <= logged d_k on every segment of every piece, eta over the whole cell.
C: Radau trajectories at 9 etas: error vs logged r at every node, and the limit inside the trap ball and the plateau box."""
import sys, json, numpy as np
C8 = 'T240/C8_eta_cell'
sys.path[:0] = [C8 + '/scripts']
from fractions import Fraction as F
import entry_eta as E, entry, iv_scm, iv_h2
from iv_exact import I, S
from scipy.integrate import solve_ivp
E.setup('1/2', '1/5000')
lo = lambda v: v.lo / S; hi = lambda v: v.hi / S
inside = lambda x, v, tol: lo(v) - tol <= x <= hi(v) + tol
tq, nodes, slopes, ys, yslopes = E.build('1600', '0.004')
K = len(tq) - 1; print('K', K, flush=True)
rng = np.random.default_rng(5); fe = E.fe
# A
bad = 0; nck = 0
for k in rng.choice(K, 12, replace=False):
    for eta in (0.4998, 0.5, 0.50013):
        x = entry.fl(nodes[k]) + 1e-3 * rng.standard_normal(3)
        xi = [I.of(F(float(v))) for v in x]; ei = I.of(F(eta))
        sd = iv_scm.symmetric_driver(xi, ei); s4 = E.sym4(xi, ei); h4 = E.sym4_h2(xi, ei); hs = iv_h2.symmetric_driver(xi, ei)
        g = lambda z: np.concatenate([fe(z[:3], z[3])])
        z0 = np.append(x, eta); f0 = g(z0); hh = 1e-5
        J = np.column_stack([(g(z0 + hh * e) - g(z0 - hh * e)) / (2 * hh) for e in np.eye(4)])
        Hs = np.zeros((3, 4, 4))
        for a in range(4):
            for b in range(4):
                ea, eb = np.eye(4)[a] * 1e-4, np.eye(4)[b] * 1e-4
                Hs[:, a, b] = (g(z0 + ea + eb) - g(z0 + ea - eb) - g(z0 - ea + eb) + g(z0 - ea - eb)) / 4e-8
        for i in range(3):
            checks = [(f0[i], sd[i].v, 1e-12), (f0[i], s4[i].v, 1e-12)]
            checks += [(J[i, j], sd[i].d[j], 1e-7) for j in range(3)] + [(J[i, j], s4[i].d[j], 1e-7) for j in range(4)]
            checks += [(Hs[i, a, b], h4[i].h[a][b], 2e-4) for a in range(4) for b in range(4)]
            checks += [(Hs[i, a, b], hs[i].h[a][b], 2e-4) for a in range(3) for b in range(3)]
            for val, v, tol in checks:
                nck += 1
                if not inside(val, v, tol * max(1, abs(val))): bad += 1; print('A MISMATCH', k, eta, i, val, lo(v), hi(v))
print(f'A: {nck} jet entries checked against finite differences, {bad} outside', flush=True)
# B
logs = {}
for n in ['q1', 'q2', 'q3', 'q4', 'q5', 'q6b', 'q6c', 'q6d']:
    for l in open(f'{C8}/logs/{n}.jsonl'):
        r = json.loads(l)
        if 'k' in r: logs[r['k']] = r
worst = 0; viol = 0
for k in range(K):
    h = float(tq[k + 1] - tq[k]); A = np.array(entry.hermite_coeffs(nodes[k], nodes[k + 1], slopes[k], slopes[k + 1], tq[k + 1] - tq[k]), dtype=float)
    B = np.array(entry.hermite_coeffs(ys[k], ys[k + 1], yslopes[k], yslopes[k + 1], tq[k + 1] - tq[k]), dtype=float)
    P, Pinv = entry.frame(entry.jac_f(entry.fl(nodes[k]))); Pinv = np.array(Pinv, dtype=float)
    for s in np.concatenate([[0, 1, 0.5], rng.random(15)]):
        pw = np.array([1, s, s * s, s ** 3]); dpw = np.array([0, 1, 2 * s, 3 * s * s]) / h
        for de in np.concatenate([[-2e-4, 2e-4, 0], rng.uniform(-2e-4, 2e-4, 3)]):
            x = A @ pw + de * (B @ pw); v = A @ dpw + de * (B @ dpw)
            d = np.linalg.norm(Pinv @ (v - fe(x, 0.5 + de)))
            ratio = d / logs[k]['d']; worst = max(worst, ratio)
            if ratio > 1: viol += 1
print(f'B: sampled defect / logged d over {K} segments: max ratio {worst:.4f}, violations {viol}', flush=True)
# C
tr = json.loads(open(f'{C8}/logs/trap.jsonl').readlines()[-1]); xs0 = np.array([float(F(v)) for v in tr['xs0']]); ysx = np.array([float(F(v)) for v in tr['ys']])
Ps, Pinvs = entry.frame(entry.jac_f(xs0)); Pinvs = np.array(Pinvs, dtype=float); rho = float(F(tr['PASS']['rho']))
cells = [json.loads(l) for l in open(f'{C8}/logs/plateau_cells.jsonl')]; cells = [c for c in cells if c.get('result') == 'pass']
tqf = [float(t) for t in tq]; worst = 0
for eta in np.linspace(0.4998, 0.5002, 9):
    sol = solve_ivp(lambda t, x: fe(x, eta), (0, 8000), [1.0, 0, 0], method='Radau', rtol=1e-12, atol=1e-14, dense_output=True)
    for k in range(1, K + 1):
        xh = entry.fl(nodes[k]) + (eta - 0.5) * entry.fl(ys[k]); P, Pinv = entry.frame(entry.jac_f(entry.fl(nodes[k])))
        r = logs[k - 1]['r']; z = np.linalg.norm(np.array(Pinv, dtype=float) @ (sol.sol(tqf[k]) - xh)); worst = max(worst, z / r)
    xe = sol.sol(8000); zt = np.linalg.norm(Pinvs @ (xe - xs0 - (eta - 0.5) * ysx)); fn = np.linalg.norm(fe(xe, eta))
    c = [c for c in cells if float(F(c['eta_lo'])) <= eta <= float(F(c['eta_hi']))][0]
    inbox = np.max(np.abs(xe - np.array(c['center']))) <= c['info'][0]
    print(f'C: eta {eta:.5f}: |z(8000)| about c(eta) {zt:.3e} (rho {rho:.0e}), |f| {fn:.1e}, in its plateau box {inbox}', flush=True)
print(f'C: max over 9 etas and all nodes of |z_true| / r_logged = {worst:.4e}')

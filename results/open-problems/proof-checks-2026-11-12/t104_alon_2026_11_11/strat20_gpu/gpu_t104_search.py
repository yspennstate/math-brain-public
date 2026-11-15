"""an agent: GPU (MLX) batched search for T < 0 on T104 disconnected D=2 splits n1+n2 (4+5, 5+5), with isolates
and with lower trace s in [0, k-(n1+n2)+1]. Same functional as my_35_search.py (from the STRAT17/18 RESULT.md formula,
checked against Codex's K3+K5 value 56/1215 at k=6). Each block: u unit zero-sum, P = I - J/n - uu^T,
A = J/n + P F F^T P (PSD, A1 = 1, Au = 0); entrywise A >= 0 by a growing penalty. Adam on a batch of random starts per k,
float32 on the GPU, the best near-feasible points re-scored in float64 with numpy.
Usage: python gpu_t104_search.py N1 N2 BATCH STEPS ROUNDS SEED OUTPREFIX. Corroboration only, not proof: a negative value
here is a CANDIDATE to be replayed exactly, never a counterexample by itself."""
import sys, time, json
import numpy as np
import mlx.core as mx
import mlx.optimizers as optim

N1, N2, BATCH, STEPS, ROUNDS, SEED = (int(a) for a in sys.argv[1:7])
OUT = sys.argv[7]
SIZES = (N1, N2)
NTOT = N1 + N2
mx.random.seed(SEED)
rng = np.random.default_rng(SEED)


def build(ur, F, n):
    u = ur - mx.mean(ur, axis=1, keepdims=True)
    u = u / mx.sqrt(mx.sum(u * u, axis=1, keepdims=True) + 1e-20)
    I = mx.eye(n)[None]
    J = mx.ones((1, n, n)) / n
    P = I - J - u[:, :, None] * u[:, None, :]
    G = P @ F
    A = J + G @ mx.swapaxes(G, 1, 2)
    return u, A


def terms(z, A, n):
    I = mx.eye(n)[None]
    C = I - A
    dC = mx.sum(C * I, axis=2)
    trc = 2 * (mx.sum(dC, axis=1) - mx.sum(C * C, axis=(1, 2)))
    Bs = mx.sum(z[:, :, None] * z[:, None, :] * A * A, axis=(1, 2))
    h = mx.sum(z * z * dC, axis=1)
    off = 1 - I
    dz2 = (z[:, :, None] - z[:, None, :]) ** 2
    Y = mx.sum(off * A * dz2 * (2 - dC[:, :, None] - dC[:, None, :] - 2 * A), axis=(1, 2))
    trC = mx.sum(dC, axis=1)
    pen = mx.sum(mx.maximum(-A, 0) ** 2, axis=(1, 2))
    return trc, Bs, h, Y, trC, pen


def Tbatch(p, k, lowers):
    tr = Bs = h = Y = trC = pen = 0
    for i, n in enumerate(SIZES):
        u, A = build(p['u%d' % i], p['F%d' % i], n)
        a, b, c, d, e, f = terms(u, A, n)
        tr, Bs, h, Y, trC, pen = tr + a, Bs + b, h + c, Y + d, trC + e, pen + f
    cap = k - NTOT + 1
    s = cap * mx.sigmoid(p['t'][:, 0]) if (lowers and cap > 0) else mx.zeros(trC.shape)
    M = trC / 2 + s / 2
    X = (M - 1) / k ** 2 * (2 * (k + 1) * (k - 2) - 4 * k * M + 2 * (k + 2) * h)
    T = (tr + 2 * (k + 2) * Bs / k + X - Y) / (M * M)
    return T, pen, s


def np_T(p, b, k, lowers):
    """float64 re-score of start b (numpy), returns T, min entry of A, s."""
    tr = Bs = h = Y = trC = 0.0
    mins = []
    for i, n in enumerate(SIZES):
        ur = np.array(p['u%d' % i][b], dtype=np.float64); F = np.array(p['F%d' % i][b], dtype=np.float64)
        u = ur - ur.mean(); u /= np.linalg.norm(u)
        P = np.eye(n) - np.ones((n, n)) / n - np.outer(u, u)
        A = np.ones((n, n)) / n + P @ F @ F.T @ P
        C = np.eye(n) - A; dC = np.diag(C)
        tr += 2 * (np.trace(C) - np.sum(C * C)); Bs += np.sum(np.outer(u, u) * A * A); h += np.sum(u * u * dC)
        off = 1 - np.eye(n); dz2 = (u[:, None] - u[None, :]) ** 2
        Y += np.sum(off * A * dz2 * (2 - dC[:, None] - dC[None, :] - 2 * A)); trC += np.trace(C)
        mins.append(A.min())
    cap = k - NTOT + 1
    s = cap / (1 + np.exp(-float(np.array(p['t'][b, 0])))) if (lowers and cap > 0) else 0.0
    M = trC / 2 + s / 2
    X = (M - 1) / k ** 2 * (2 * (k + 1) * (k - 2) - 4 * k * M + 2 * (k + 2) * h)
    return (tr + 2 * (k + 2) * Bs / k + X - Y) / M ** 2, min(mins), s


# fixture: K3+K5 at k=6 must equal Codex's 56/1215 (same functional)
def fixture():
    global SIZES, NTOT
    keep = SIZES, NTOT
    SIZES, NTOT = (3, 5), 8
    p = {'u0': mx.array([[1.0, -1.0, 0.0]]), 'u1': mx.array([[1.0, -1.0, 0.0, 0.0, 0.0]]),
         'F0': mx.zeros((1, 3, 3)), 'F1': mx.zeros((1, 5, 5)), 't': mx.zeros((1, 1))}
    T, _, _ = Tbatch(p, 6.0, False)
    T64 = np_T({kk: np.array(v) for kk, v in p.items()}, 0, 6.0, False)[0]
    SIZES, NTOT = keep
    return float(T.item()), T64


fT, fT64 = fixture()
print('fixture K3+K5 k=6 gpu32 %.8f np64 %.10f Codex 56/1215 = %.10f' % (fT, fT64, 56 / 1215), flush=True)
assert abs(fT64 - 56 / 1215) < 1e-12, 'functional mismatch'

kmin = NTOT - 2
ks_iso = [float(kmin), kmin + 1.0, kmin + 2.0, kmin + 3.0, kmin + 5.0, 20.0, 50.0, 1e3]
ks_low = [float(k) for k in (NTOT, NTOT + 1, NTOT + 2, NTOT + 4, 20, 50, 1000)]
results = []
t0 = time.time()
for rnd in range(ROUNDS):
    for lowers, ks in ((False, ks_iso), (True, ks_low)):
        for k in ks:
            p = {'t': mx.random.normal((BATCH, 1))}
            for i, n in enumerate(SIZES):
                p['u%d' % i] = mx.random.normal((BATCH, n))
                p['F%d' % i] = mx.random.normal((BATCH, n, n)) * mx.random.uniform(0, 0.6, (BATCH, 1, 1))
            opt = optim.Adam(learning_rate=0.01)

            def loss(q, mu):
                T, pen, _ = Tbatch(q, k, lowers)
                return mx.sum(T + mu * pen)

            g = mx.value_and_grad(loss)
            for st in range(STEPS):
                mu = 10.0 * (1.0 + 1e4 * st / STEPS)
                if st == STEPS // 2:
                    opt.learning_rate = 0.002
                _, gr = g(p, mu)
                opt.update(p, gr)
                mx.eval(p, opt.state)
            T, pen, s = Tbatch(p, k, lowers)
            mx.eval(T, pen)
            Tn = np.array(T); pn = np.array(pen)
            feas = pn < 1e-8
            order = np.argsort(np.where(feas, Tn, np.inf))[:8]
            pn_np = {kk: np.array(v) for kk, v in p.items()}
            best = []
            for b in order:
                if not np.isfinite(Tn[b]) or not feas[b]:
                    continue
                T64, amin, s64 = np_T(pn_np, b, k, lowers)
                best.append((float(T64), float(amin), float(s64)))
            best.sort()
            rec = {'round': rnd, 'lowers': lowers, 'k': k, 'feasible': int(feas.sum()), 'best': best[:3],
                   'elapsed_s': round(time.time() - t0, 1)}
            results.append(rec)
            flag = ' CANDIDATE' if best and best[0][0] < -1e-6 and best[0][1] > -1e-6 else ''
            print('r%d lowers=%s k=%g feasible %d/%d best T64 %s%s  [%.0fs]' % (
                rnd, lowers, k, feas.sum(), BATCH, ['%.4g (Amin %.1e, s %.3f)' % b for b in best[:2]], flag,
                time.time() - t0), flush=True)
            with open(OUT + '.json', 'w') as fh:
                json.dump(results, fh)
print('done %.0fs' % (time.time() - t0), flush=True)

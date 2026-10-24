"""Bounded countersearch for the frozen lemma L(K*):
   every nonconstant Boolean f on the uniform cube has a relevant i with B_i <= K* Inf_i.
Frozen families: (A) all symmetric f on n=3..14; (B) all cyclic-shift-invariant f on n=5,6,7;
(C) iterated local search over all truth tables on n=5,6 (fixed seeds, wall cap per n).
Every float violation is re-decided exactly (prime-exponent linear form in logs)."""
import sys, json, time, numpy as np
from math import comb
sys.path.insert(0, sys.argv[1])
OUT = sys.argv[2]
CAP = float(sys.argv[3]) if len(sys.argv) > 3 else 120
from b15_engine import KSTAR, hadamard, pair_index, spectra, tables_to_pm
from exact_prime import sign_pairs_vs_kstar

res = {'KSTAR': KSTAR}
t00 = time.time()


def h2v(q):
    with np.errstate(divide='ignore', invalid='ignore'):
        qq = np.clip(q, 1e-300, 1 - 1e-16)
        v = -qq * np.log2(qq) - (1 - qq) * np.log2(1 - qq)
    return np.where((q > 0) & (q < 1), v, 0.0)


def safe_div(a, b):
    return np.where(b > 0, a / np.where(b > 0, b, 1.0), 0.0)


# ---------- (A) symmetric ----------
symA = []
for n in range(3, 15):
    K = np.array([[sum((-1) ** j * comb(k, j) * comb(n - k, w - j) for j in range(0, k + 1) if 0 <= w - j <= n - k)
                   for k in range(n + 1)] for w in range(n + 1)], dtype=np.int64)
    ts = np.arange(1 << (n + 1), dtype=np.int64)
    Fw = 1 - 2 * ((ts[:, None] >> np.arange(n + 1)[None, :]) & 1)
    Wk = Fw @ K
    P = (Wk.astype(np.float64) ** 2) / float(4 ** n)
    c = np.array([comb(n - 1, k) for k in range(n)], dtype=np.float64)
    a = P[:, :n]
    b = P[:, 1:]
    s = a + b
    Bv = (c[None, :] * s * h2v(safe_div(b, s))).sum(axis=1)
    Inf = (c[None, :] * b).sum(axis=1)
    ok = Inf > 1e-14
    E = np.where(ok, safe_div(Bv, Inf), -np.inf)
    j = int(np.argmax(E))
    d = dict(n=n, best_table_by_weight=int(ts[j]), E=float(E[j]), Inf1=float(Inf[j]), W=[int(v) for v in Wk[j]],
             float_violations=int((E > KSTAR + 1e-9).sum()))
    pairs = [(d['W'][k] ** 2, d['W'][k + 1] ** 2, comb(n - 1, k)) for k in range(n)]
    d['exact_sign_vs_Kstar'] = sign_pairs_vs_kstar(pairs)[0]
    symA.append(d)
res['A_symmetric'] = symA
print('A', [(d['n'], round(d['E'], 6), d['float_violations'], d['exact_sign_vs_Kstar']) for d in symA], round(time.time() - t00, 1), flush=True)

# ---------- (B) cyclic invariant ----------
cycB = []
for n in (5, 6, 7):
    D = 1 << n
    orb = -np.ones(D, dtype=np.int64)
    reps = []
    for x in range(D):
        if orb[x] >= 0:
            continue
        y = x
        k = len(reps)
        while orb[y] < 0:
            orb[y] = k
            y = ((y << 1) | (y >> (n - 1))) & (D - 1)
        reps.append(x)
    m = len(reps)
    best = (-np.inf, None, None)
    nviol = 0
    viol_codes = []
    Hm = hadamard(n)
    i0, i1 = pair_index(n, 0)
    for st in range(0, 1 << m, 1 << 15):
        cs = np.arange(st, min(st + (1 << 15), 1 << m), dtype=np.int64)
        F = 1 - 2 * ((cs[:, None] >> orb[None, :]) & 1)
        W = (F @ Hm).astype(np.float64)
        P = W * W / (D * D)
        a = P[:, i0]
        b = P[:, i1]
        s = a + b
        Bv = (s * h2v(safe_div(b, s))).sum(axis=1)
        Inf = b.sum(axis=1)
        ok = Inf > 1e-14
        E = np.where(ok, safe_div(Bv, Inf), -np.inf)
        vv = np.nonzero(E > KSTAR + 1e-9)[0]
        nviol += len(vv)
        viol_codes += [int(cs[v]) for v in vv[:5]]
        j = int(np.argmax(E))
        if E[j] > best[0]:
            best = (float(E[j]), int(cs[j]), [int(v) for v in W[j]])
    cycB.append(dict(n=n, orbits=m, functions=1 << m, float_violations=nviol, best_E=best[0], best_code=best[1],
                     best_W=best[2], sample_violation_codes=viol_codes[:10]))
    print('B', n, m, nviol, best[0], round(time.time() - t00, 1), flush=True)
res['B_cyclic'] = cycB


# ---------- (C) iterated local search ----------
def Evals(F, n):
    D = 1 << n
    W = spectra(F, n).astype(np.float64)
    P = W * W / (D * D)
    R = np.full((F.shape[0], n), np.inf)
    for i in range(n):
        i0, i1 = pair_index(n, i)
        a = P[:, i0]
        b = P[:, i1]
        s = a + b
        Bv = (s * h2v(safe_div(b, s))).sum(axis=1)
        Inf = b.sum(axis=1)
        R[:, i] = np.where(Inf > 1e-14, safe_div(Bv, Inf), np.inf)
    E = R.min(axis=1)
    E[~np.isfinite(E)] = -np.inf
    soft = np.where(np.isfinite(R), R, 0).mean(axis=1)
    return E, soft


ils = []
for n in (5, 6):
    D = 1 << n
    rng = np.random.default_rng(20261011 + n)
    t0 = time.time()
    best = (-np.inf, None)
    tops = {}
    steps = 0
    restarts = 0
    while time.time() - t0 < CAP:
        restarts += 1
        if rng.random() < 0.5:
            cur = (rng.random(D) < rng.choice([1 / D, 2 / D, 3 / D, 4 / D, 0.1, 0.2])).astype(np.int64)
        else:
            cur = rng.integers(0, 2, D).astype(np.int64)
        e0, s0 = Evals(1 - 2 * cur[None, :], n)
        cv = e0[0] + 1e-3 * s0[0]
        stall = 0
        while stall < 30 and time.time() - t0 < CAP:
            Nb = np.repeat(cur[None, :], D, axis=0)
            Nb[np.arange(D), np.arange(D)] ^= 1
            e, s = Evals(1 - 2 * Nb, n)
            obj = e + 1e-3 * s
            j = int(np.argmax(obj))
            steps += 1
            if obj[j] > cv + 1e-12:
                cur = Nb[j].copy()
                cv = obj[j]
                stall = 0
                if e[j] > best[0]:
                    best = (float(e[j]), cur.copy())
                if e[j] > KSTAR - 0.05:
                    tops[int(sum(int(v) << k for k, v in enumerate(cur)))] = float(e[j])
            else:
                stall += 1
                flips = rng.choice(D, size=int(rng.integers(1, 4)), replace=False)
                cur = cur.copy()
                cur[flips] ^= 1
                ee, ss = Evals(1 - 2 * cur[None, :], n)
                cv = ee[0] + 1e-3 * ss[0]
                if ee[0] > best[0]:
                    best = (float(ee[0]), cur.copy())
                if ee[0] > KSTAR - 0.05:
                    tops[int(sum(int(v) << k for k, v in enumerate(cur)))] = float(ee[0])
    tl = sorted(tops.items(), key=lambda kv: -kv[1])[:40]
    ils.append(dict(n=n, steps=steps, restarts=restarts, best_E=best[0],
                    best_table=(str(sum(int(v) << k for k, v in enumerate(best[1]))) if best[1] is not None else None), top=[(str(k), v) for k, v in tl]))
    print('C', n, steps, restarts, best[0], [(str(k), round(v, 6)) for k, v in tl[:6]], round(time.time() - t00, 1), flush=True)
res['C_ils'] = ils


def certify(table, n):
    F = np.array([[1 - 2 * ((table >> x) & 1) for x in range(1 << n)]], dtype=np.int64)
    W = spectra(F, n)[0]
    out = []
    for i in range(n):
        i0, i1 = pair_index(n, i)
        L = int(sum(int(W[t]) ** 2 for t in i1))
        if L == 0:
            out.append(None)
            continue
        pairs = [(int(W[a]) ** 2, int(W[b]) ** 2, 1) for a, b in zip(i0, i1)]
        out.append(sign_pairs_vs_kstar(pairs)[0])
    return out


json.dump(res, open(OUT, 'w', encoding='utf-8'), indent=1)
cert = []
for d in ils:
    for key, val in d['top']:
        if val > KSTAR + 1e-12:
            sg = certify(int(key), d['n'])
            cert.append(dict(n=d['n'], table=key, E_float=val, exact_signs=sg,
                             violation=all(s is None or s > 0 for s in sg) and any(s is not None for s in sg)))
res['exact_violation_certificates'] = cert
res['seconds'] = time.time() - t00
json.dump(res, open(OUT, 'w', encoding='utf-8'), indent=1)
print('certs', [(c['n'], c['table'], round(c['E_float'], 6), c['exact_signs'], c['violation']) for c in cert[:10]])

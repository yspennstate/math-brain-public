# FROZEN SPEC (written before the first run, 2026-10-11 ~23:00 UTC; not changed after):
#   objective  R(f) = min over relevant i of B_i(f)/I_i(f), bits, uniform measure,
#              B_i = H(S_i | S_-i) of the squared Walsh spectrum.  Float64 search only.
#   domain     Boolean f on n bits, n in {5, 6}; n is never raised.
#   starts     rng = numpy.random.default_rng(20261011 + n); each restart draws a density
#              rho from {1/32,1/16,1/8,3/16,1/4,3/8,1/2} and a table with P(f=-1)=rho
#              (redrawn until nonconstant).
#   moves      steepest ascent over all single-point flips; when none improves by >1e-12,
#              steepest ascent over all two-point flips; when none improves, restart.
#   budget     150 s wall clock per n, nothing adaptive.
#   output     best R per n, its truth table, the 10 best distinct local maxima; the best
#              table per n is then certified EXACTLY (integer Walsh coefficients, certified
#              log2 enclosures): sign of B_i/I_i - K* and B_i/I_i - 107/40 for every
#              relevant i, K* = 4 + (5/2)log2 5 - (9/2)log2 3 = K_B(4).
# A float maximum is evidence only.  Only the exact signs are claims.
import sys, os, json, time
import numpy as np
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from certlog import sign_form, enclose_form, add_mlogm

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'out')
RHOS = [1/32, 1/16, 1/8, 3/16, 1/4, 3/8, 1/2]

def setup(n):
    N = 1 << n
    pc = np.array([bin(v).count('1') for v in range(N)])
    Hm = np.array([[(-1) ** int(pc[x & S]) for S in range(N)] for x in range(N)], dtype=np.int64)
    iT = np.array([[T for T in range(N) if not T >> i & 1] for i in range(n)])
    iTi = iT | (1 << np.arange(n))[:, None]
    m = np.arange(N * N + 1, dtype=np.float64)
    G = np.zeros_like(m); G[1:] = m[1:] * np.log2(m[1:])
    return N, Hm, iT, iTi, G

def evalR(F, n, ctx):
    N, Hm, iT, iTi, G = ctx
    W = F @ Hm; q = W * W
    A = q[:, iT]; Bq = q[:, iTi]
    Bn = (G[A + Bq] - G[A] - G[Bq]).sum(-1)
    D = Bq.sum(-1)
    with np.errstate(divide='ignore', invalid='ignore'):
        r = np.where(D > 0, Bn / np.where(D > 0, D, 1), np.inf)
    R = r.min(1)
    R[(D == 0).all(1)] = -np.inf
    return R

def search(n, budget=150.0):
    ctx = setup(n); N = ctx[0]
    rng = np.random.default_rng(20261011 + n)
    pj, pk = np.triu_indices(N, 1)
    t0 = time.time(); maxima = {}; restarts = 0; steps = 0
    while time.time() - t0 < budget:
        rho = RHOS[rng.integers(len(RHOS))]
        while True:
            f = np.where(rng.random(N) < rho, -1, 1).astype(np.int64)
            if 0 < (f == -1).sum() < N:
                break
        cur = evalR(f[None, :], n, ctx)[0]; restarts += 1
        while time.time() - t0 < budget:
            F1 = np.tile(f, (N, 1)); F1[np.arange(N), np.arange(N)] *= -1
            R1 = evalR(F1, n, ctx); k = int(np.argmax(R1))
            if R1[k] > cur + 1e-12:
                f = F1[k]; cur = R1[k]; steps += 1; continue
            F2 = np.tile(f, (len(pj), 1)); r = np.arange(len(pj))
            F2[r, pj] *= -1; F2[r, pk] *= -1
            R2 = evalR(F2, n, ctx); k = int(np.argmax(R2))
            if R2[k] > cur + 1e-12:
                f = F2[k]; cur = R2[k]; steps += 1; continue
            break
        key = round(float(cur), 10)
        if key not in maxima:
            maxima[key] = (f.copy(), 1)
        else:
            maxima[key] = (maxima[key][0], maxima[key][1] + 1)
    top = sorted(maxima.items(), key=lambda kv: -kv[0])[:10]
    return {'n': n, 'restarts': restarts, 'improving_moves': steps, 'seconds': round(time.time() - t0, 1),
            'distinct_local_maxima': len(maxima),
            'top10': [{'R_float': k, 'hits': v[1], 'truth_table_points_minus1': [int(x) for x in np.nonzero(v[0] == -1)[0]]}
                      for k, v in top]}, top[0][1][0]

def certify(f, n):
    """Exact data for every relevant coordinate of f."""
    N = 1 << n
    W = []
    for S in range(N):
        W.append(sum(int(f[x]) * (-1) ** bin(x & S).count('1') for x in range(N)))
    q = [w * w for w in W]
    KSTAR = {2: 8, 5: 5, 3: -9}                       # 2 K* = 8 log2 2 + 5 log2 5 - 9 log2 3
    rows = []
    for i in range(n):
        bit = 1 << i
        D = sum(q[T | bit] for T in range(N) if not T & bit)
        if D == 0:
            continue
        form = {}
        for T in range(N):
            if T & bit:
                continue
            a, b = q[T], q[T | bit]
            add_mlogm(form, a + b, 1); add_mlogm(form, a, -1); add_mlogm(form, b, -1)
        # N^2 B_i = form . log2 ;  N^2 I_i = D
        e1 = {p: 2 * v for p, v in form.items()}
        for p, v in KSTAR.items():
            e1[p] = e1.get(p, 0) - D * v
        e2 = {p: 40 * v for p, v in form.items()}; e2[2] = e2.get(2, 0) - 107 * D
        lo, hi = enclose_form(form)
        rows.append({'coord': i, 'N2_I_i': D, 'B_i_over_I_i_lo': f'{float(lo / D):.15f}',
                     'B_i_over_I_i_hi': f'{float(hi / D):.15f}',
                     'sign(B_i/I_i - K*)': sign_form(e1), 'sign(B_i/I_i - 107/40)': sign_form(e2)})
    return {'walsh_W': W, 'rows': rows,
            'all_relevant_exceed_Kstar': all(r['sign(B_i/I_i - K*)'] > 0 for r in rows),
            'all_relevant_exceed_107/40': all(r['sign(B_i/I_i - 107/40)'] > 0 for r in rows)}

if __name__ == '__main__':
    res = {'spec': 'see header of search_n56.py (frozen before running)'}
    for n in (5, 6):
        rep, fbest = search(n)
        rep['exact_certificate_of_best'] = certify(fbest, n)
        res[f'n{n}'] = rep
        print(json.dumps({k: v for k, v in rep.items() if k != 'exact_certificate_of_best'}, indent=1))
        print(json.dumps({k: v for k, v in rep['exact_certificate_of_best'].items() if k != 'walsh_W'}, indent=1))
        sys.stdout.flush()
    with open(os.path.join(OUT, 'search_n56.json'), 'w', encoding='utf-8') as fh:
        json.dump(res, fh, indent=1)

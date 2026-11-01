# Intermediate assignment rules for the distinguished-element decomposition of a linear threshold function: each set A
# (|A| >= 2) is divided among its elements with shares proportional to w_j^{-gamma} (gamma = 0: equal division, the
# damped scheme; gamma -> infinity: the lightest elements own it) or to rho_j^{-1} (rho_j = P(j pivotal), an intrinsic
# version).  Each coordinate's charge sum share * P(A) ln(sigma_A^2/P(A)) is compared with its budget
# K_j = sum share * |A| * P(A) (the budgets sum to J).  Reports max_j charge_j/K_j per rule on random threshold
# functions, on the heavy-plus-light family, and on the instance that broke the lightest-owner rule.
import mpmath as mp, random, sys
from slab_damped import biased_transform, popcount

RULES = ['w^0', 'w^-1', 'w^-2', 'rho^-1']

def ratios(w, theta, q):
    n = len(w)
    f = [1 if sum(w[i] for i in range(n) if (x >> i) & 1) >= theta else 0 for x in range(1 << n)]
    if len(set(f)) < 2: return None
    rho = []
    for j in range(n):
        s = mp.mpf(0)
        for x in range(1 << n):
            if not (x >> j) & 1 and f[x] != f[x | (1 << j)]:
                p = mp.mpf(1)
                for i in range(n):
                    if i != j: p *= q[i] if (x >> i) & 1 else 1 - q[i]
                s += p
        rho.append(s)
    g = [1 - 2 * v for v in f]
    c = biased_transform(g, q)
    out = {}
    for rule in RULES:
        ch = [mp.mpf(0)] * n; K = [mp.mpf(0)] * n
        for A in range(1, 1 << n):
            k = popcount(A)
            if k < 2 or c[A] == 0: continue
            PA = c[A] ** 2
            sA = mp.mpf(1)
            for t in range(n):
                if (A >> t) & 1: sA *= 4 * q[t] * (1 - q[t])
            term = PA * mp.log(sA / PA)
            mem = [i for i in range(n) if (A >> i) & 1]
            if rule == 'rho^-1': wt = [1 / rho[i] if rho[i] > 0 else mp.mpf(0) for i in mem]
            else:
                gmm = {'w^0': 0, 'w^-1': 1, 'w^-2': 2}[rule]
                wt = [mp.mpf(w[i]) ** (-gmm) for i in mem]
            tot = mp.fsum(wt)
            if tot == 0: wt = [mp.mpf(1)] * len(mem); tot = mp.mpf(len(mem))
            for i, x in zip(mem, wt):
                ch[i] += term * x / tot; K[i] += k * PA * x / tot
        r = [ch[i] / K[i] for i in range(n) if K[i] > 0]
        out[rule] = max(r) if r else mp.mpf(0)
    return out

def build(spec):
    mp.mp.dps = int(40 + 2 * sum(e for k, e in spec if k != 'mid') + 2 * len(spec))
    return [mp.mpf(10) ** (-mp.mpf(e)) if k == 'lo' else (1 - mp.mpf(10) ** (-mp.mpf(e)) if k == 'hi' else mp.mpf(e)) for k, e in spec]

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); nmax = int(sys.argv[3])
    print('heavy-plus-light family f = 1[m x_0 + N >= m/2], biases 1/2:')
    for m in [4, 6, 8]:
        mp.mp.dps = 40
        o = ratios([float(m)] + [1.0] * m, m / 2, [mp.mpf('0.5')] * (m + 1))
        print('  m', m, ' '.join('%s %s' % (r, mp.nstr(o[r], 4)) for r in RULES), flush=True)
    q0 = [mp.mpf(x) for x in ['8.07e-5', '5.48e-9', '2.62e-8', '0.00853', '9.59e-6', '0.895']]
    mp.mp.dps = 80
    o = ratios([4.0, 1.0, 1.0, 8.0, 2.0, 2.0], 17.593, q0)
    print('lightest-owner failure instance:', ' '.join('%s %s' % (r, mp.nstr(o[r], 4)) for r in RULES), flush=True)
    best = {r: (mp.mpf(0), None) for r in RULES}
    for t in range(T):
        n = rng.randint(2, nmax)
        kind = rng.random()
        if kind < 0.2: w = [1.0] * n
        elif kind < 0.4: w = [float(rng.randint(1, 3)) for _ in range(n)]
        elif kind < 0.6: w = [2.0 ** rng.randint(0, 6) for _ in range(n)]
        elif kind < 0.8: w = [rng.expovariate(1.0) + 0.01 for _ in range(n)]
        else: w = [float(n)] + [1.0] * (n - 1)
        theta = rng.uniform(0.001, sum(w))
        spec = []
        for _ in range(n):
            v = rng.random()
            if v < 0.35: spec.append(('lo', rng.uniform(0, 9)))
            elif v < 0.55: spec.append(('hi', rng.uniform(0, 9)))
            else: spec.append(('mid', rng.uniform(0.02, 0.98)))
        q = build(spec)
        o = ratios(w, theta, q)
        if o is None: continue
        for r in RULES:
            if o[r] > best[r][0]: best[r] = (o[r], (n, [round(v, 3) for v in w], round(theta, 3), [mp.nstr(x, 3) for x in q]))
        if t % 200 == 0: print(t, ' '.join('%s %s' % (r, mp.nstr(best[r][0], 4)) for r in RULES), flush=True)
    for r in RULES: print('DONE', r, 'max_j charge_j/K_j =', mp.nstr(best[r][0], 5), best[r][1])

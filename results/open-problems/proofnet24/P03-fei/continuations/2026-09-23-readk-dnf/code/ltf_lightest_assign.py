# Per-coordinate charges for linear threshold functions when each set A (|A| >= 2) is assigned to its LIGHTEST elements
# (ties split equally): charge_j = sum_{A assigned to j} share * P(A) ln(sigma_A^2/P(A)), against the budget
# K_j = sum_{A assigned to j} share * |A| * P(A) (so sum_j K_j = J = sum_{|A|>=2} |A| P(A)); a first version divided by
# J_j = sum_{A containing j} P(A), the wrong budget for a single-owner assignment.  For equal weights this is the
# damped scheme of section 28; for a heavy input whose derivative is a threshold of the light inputs it moves the
# level-2 sets {heavy, light} to the light inputs.  Measures max_j charge_j / K_j
# over random threshold functions and product measures, together with the heavy-plus-light family.
import mpmath as mp, random, sys
from slab_damped import biased_transform, popcount

def charges(w, theta, q):
    n = len(w)
    f = [1 if sum(w[i] for i in range(n) if (x >> i) & 1) >= theta else 0 for x in range(1 << n)]
    if len(set(f)) < 2: return None
    g = [1 - 2 * v for v in f]
    c = biased_transform(g, q)
    ch = [mp.mpf(0)] * n; J = [mp.mpf(0)] * n; K = [mp.mpf(0)] * n
    for A in range(1, 1 << n):
        k = popcount(A)
        if k < 2 or c[A] == 0: continue
        PA = c[A] ** 2
        sA = mp.mpf(1)
        for t in range(n):
            if (A >> t) & 1: sA *= 4 * q[t] * (1 - q[t])
        term = PA * mp.log(sA / PA)
        members = [i for i in range(n) if (A >> i) & 1]
        wmin = min(w[i] for i in members)
        light = [i for i in members if w[i] <= wmin * (1 + 1e-12)]
        for i in light:
            ch[i] += term / len(light)
            K[i] += k * PA / len(light)          # the budget of the sets assigned to i: sum of share * |A| * P(A)
        for i in members: J[i] += PA
    ratios = [ch[i] / K[i] for i in range(n) if K[i] > 0]
    return max(ratios) if ratios else mp.mpf(0)

def build(spec):
    mp.mp.dps = int(40 + 2 * sum(e for k, e in spec if k != 'mid') + 2 * len(spec))
    return [mp.mpf(10) ** (-mp.mpf(e)) if k == 'lo' else (1 - mp.mpf(10) ** (-mp.mpf(e)) if k == 'hi' else mp.mpf(e)) for k, e in spec]

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); nmax = int(sys.argv[3])
    print('heavy-plus-light family f = 1[m x_0 + N >= m/2], all biases 1/2:')
    for m in [4, 6, 8]:
        mp.mp.dps = 40
        w = [float(m)] + [1.0] * m; q = [mp.mpf('0.5')] * (m + 1)
        print('  m', m, 'max_j charge_j/K_j', mp.nstr(charges(w, m / 2, q), 5), flush=True)
    best = (mp.mpf(0), None)
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
        r = charges(w, theta, q)
        if r is not None and r > best[0]:
            best = (r, (n, [round(v, 3) for v in w], round(theta, 3), [mp.nstr(x, 3) for x in q]))
        if t % 200 == 0: print(t, 'max ratio so far', mp.nstr(best[0], 5), flush=True)
    print('DONE max_j charge_j / K_j =', mp.nstr(best[0], 6), best[1])

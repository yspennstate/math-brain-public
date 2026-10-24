# Adversarial search for the damped slab inequality  Psi(d) <= C Var(d),  d = 1[a <= w.y < b]  on {0,1}^m under a
# product measure (the derivative of a linear threshold function in one coordinate is such a slab indicator, with
# b - a the weight of that coordinate).  Hill-climbs over the weights, the slab and the biases; biases are signed
# log-odds exponents so that both tails are reachable.  Also scans structured families at larger m.
import mpmath as mp, random, sys, math
from slab_damped import biased_transform, popcount

def psi_ratio(w, a, b, q):
    m = len(w)
    d = [1 if a <= sum(w[i] for i in range(m) if (y >> i) & 1) < b else 0 for y in range(1 << m)]
    if len(set(d)) < 2: return None
    c = biased_transform(d, q)
    var = mp.fsum(c[B] ** 2 for B in range(1, 1 << m))
    if var == 0: return None
    psi = mp.mpf(0)
    for B in range(1, 1 << m):
        if c[B] == 0: continue
        sB = mp.mpf(1)
        for t in range(m):
            if (B >> t) & 1: sB *= 4 * q[t] * (1 - q[t])
        psi += c[B] ** 2 / (popcount(B) + 1) * mp.log(sB / c[B] ** 2)
    return psi / var

def qs(ex):
    need = 40 + 2 * sum(abs(e) for e in ex) + 2 * len(ex)
    mp.mp.dps = int(need)
    q = []
    for e in ex:
        if e > 0.3: q.append(mp.mpf(10) ** (-mp.mpf(e)))
        elif e < -0.3: q.append(1 - mp.mpf(10) ** (mp.mpf(e)))
        else: q.append(mp.mpf(0.5) - mp.mpf(e))
    return q

def climb(rng, m, steps):
    w = [rng.choice([1.0, 2.0, 3.0, 2.0 ** rng.randint(0, 5), rng.expovariate(1.0) + 0.05]) for _ in range(m)]
    tot = sum(w); a = rng.uniform(0, tot); b = a + rng.uniform(0.05, tot)
    ex = [rng.choice([rng.uniform(0.5, 8), -rng.uniform(0.5, 8), rng.uniform(-0.29, 0.29)]) for _ in range(m)]
    r = psi_ratio(w, a, b, qs(ex)); best = r if r is not None else mp.mpf(-1)
    for s in range(steps):
        w2, a2, b2, ex2 = list(w), a, b, list(ex)
        u = rng.random()
        if u < 0.25:
            i = rng.randrange(m); w2[i] = max(0.01, w2[i] * math.exp(rng.gauss(0, 0.5)))
        elif u < 0.45:
            a2 = a + rng.gauss(0, 0.3) * max(w); b2 = max(a2 + 0.01, b + rng.gauss(0, 0.3) * max(w))
        else:
            i = rng.randrange(m); ex2[i] = max(-9, min(9, ex2[i] + rng.gauss(0, 1.2)))
        r2 = psi_ratio(w2, a2, b2, qs(ex2))
        if r2 is not None and r2 > best:
            best, w, a, b, ex = r2, w2, a2, b2, ex2
    return best, (m, [round(v, 3) for v in w], round(a, 3), round(b, 3), [round(e, 2) for e in ex])

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); R = int(sys.argv[2]); steps = int(sys.argv[3]); mmax = int(sys.argv[4])
    top = (mp.mpf(-1), None)
    for r in range(R):
        m = rng.randint(2, mmax)
        b, where = climb(rng, m, steps)
        if b > top[0]: top = (b, where)
        print('restart', r, 'm', m, 'Psi/Var', mp.nstr(b, 6), 'best so far', mp.nstr(top[0], 6), top[1], flush=True)
    print('DONE', mp.nstr(top[0], 8), top[1])

# Adversarial search on the strengthened biased inequality for linear threshold functions:
#     R(f, mu) = sum_{A != empty} P(A) log2(sigma_A^2 / P(A)) / (I_mu - Var_mu)      (bits)
# over f = 1[w.x >= theta] (w >= 0; negations of inputs are covered by the biases) and product measures mu.
# The sharp value for AND_2 / OR_2 at extreme bias is 2 + 4 log2(e) = 7.7708; the question is whether any linear
# threshold function exceeds it.  Hill-climbing over weights, threshold and signed log-odds biases.
import mpmath as mp, random, sys, math
from slab_damped import biased_transform, popcount

def ratio(w, theta, ex):
    n = len(w)
    need = 40 + 2 * sum(abs(e) for e in ex) + 2 * n
    mp.mp.dps = int(need)
    q = []
    for e in ex:
        if e > 0.3: q.append(mp.mpf(10) ** (-mp.mpf(e)))
        elif e < -0.3: q.append(1 - mp.mpf(10) ** (mp.mpf(e)))
        else: q.append(mp.mpf(0.5) - mp.mpf(e))
    f = [1 if sum(w[i] for i in range(n) if (x >> i) & 1) >= theta else 0 for x in range(1 << n)]
    if len(set(f)) < 2: return None
    g = [1 - 2 * v for v in f]
    c = biased_transform(g, q)
    lhs = mp.mpf(0); I = mp.mpf(0); V = mp.mpf(0)
    for A in range(1, 1 << n):
        if c[A] == 0: continue
        PA = c[A] ** 2
        sA = mp.mpf(1)
        for t in range(n):
            if (A >> t) & 1: sA *= 4 * q[t] * (1 - q[t])
        lhs += PA * mp.log(sA / PA); I += popcount(A) * PA; V += PA
    if I - V <= mp.mpf(10) ** (-(mp.mp.dps - 15)) * I: return None
    return lhs / (I - V) / mp.log(2)

def climb(rng, n, steps):
    w = [rng.choice([1.0, 2.0, 3.0, 2.0 ** rng.randint(0, 5), rng.expovariate(1.0) + 0.05]) for _ in range(n)]
    theta = rng.uniform(0.01, sum(w))
    ex = [rng.choice([rng.uniform(0.5, 9), -rng.uniform(0.5, 9), rng.uniform(-0.29, 0.29)]) for _ in range(n)]
    r = ratio(w, theta, ex); best = r if r is not None else mp.mpf(-1)
    for s in range(steps):
        w2, th2, ex2 = list(w), theta, list(ex)
        u = rng.random()
        if u < 0.3:
            i = rng.randrange(n); w2[i] = max(0.01, w2[i] * math.exp(rng.gauss(0, 0.5)))
        elif u < 0.5:
            th2 = min(max(0.001, theta + rng.gauss(0, 0.3) * max(w2)), sum(w2))
        else:
            i = rng.randrange(n); ex2[i] = max(-12, min(12, ex2[i] + rng.gauss(0, 1.5)))
        r2 = ratio(w2, th2, ex2)
        if r2 is not None and r2 > best:
            best, w, theta, ex = r2, w2, th2, ex2
    return best, (n, [round(v, 3) for v in w], round(theta, 3), [round(e, 2) for e in ex])

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); R = int(sys.argv[2]); steps = int(sys.argv[3]); nmax = int(sys.argv[4])
    top = (mp.mpf(-1), None)
    for r in range(R):
        n = rng.randint(3, nmax)
        b, where = climb(rng, n, steps)
        if b > top[0]: top = (b, where)
        print('restart', r, 'n', n, 'ratio(bits)', mp.nstr(b, 8), 'best so far', mp.nstr(top[0], 8), top[1], flush=True)
    print('DONE', mp.nstr(top[0], 10), top[1], ' reference 2 + 4 log2 e =', mp.nstr(2 + 4 / mp.log(2), 10))

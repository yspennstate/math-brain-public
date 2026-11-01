# Exact-precision test of the biased isoperimetric inequalities (mpmath, 60 digits):
#  (*)  Var ln(1/Var) <= sum_i Inf_i ln+(c rho_i / Var) + C1 * I          rho_i = Inf_i / sig_i^2
#  (**) W ln(1/W)     <= sum_i J_i  ln+(c v_i / W)     + C2 * J          v_i = J_i / sig_i^2 = Var(d_i)
# P(A) = sig_A^2 * 4^{-|A|} (E_{x outside A} d_A g)^2 computed from integer mixed derivatives.
import math, random, sys
import mpmath as mp
mp.mp.dps = 60

def biased_spectrum(fvals, q):
    n = len(q)
    q = [mp.mpf(v) for v in q]
    g = [1 - 2 * v for v in fvals]
    P = {}
    for A in range(1, 1 << n):
        Ai = [i for i in range(n) if (A >> i) & 1]
        rest = [i for i in range(n) if not (A >> i) & 1]
        tot = mp.mpf(0)
        for r in range(1 << len(rest)):
            base = 0; wt = mp.mpf(1)
            for t, i in enumerate(rest):
                if (r >> t) & 1: base |= 1 << i; wt *= q[i]
                else: wt *= 1 - q[i]
            d = 0
            for y in range(1 << len(Ai)):
                x = base; cnt = 0
                for t, i in enumerate(Ai):
                    if (y >> t) & 1: x |= 1 << i; cnt += 1
                d += (-1) ** (len(Ai) - cnt) * g[x]
            if d: tot += wt * d
        if tot != 0:
            s2 = mp.mpf(1)
            for i in Ai: s2 *= 4 * q[i] * (1 - q[i])
            P[A] = s2 * (tot / 2 ** len(Ai)) ** 2
    return P

def stats(P, q):
    n = len(q)
    sig2 = [4 * mp.mpf(v) * (1 - mp.mpf(v)) for v in q]
    Var = mp.fsum(P.values())
    W = mp.fsum(v for A, v in P.items() if bin(A).count('1') >= 2)
    I = mp.fsum(bin(A).count('1') * v for A, v in P.items())
    J = mp.fsum(bin(A).count('1') * v for A, v in P.items() if bin(A).count('1') >= 2)
    Inf = [mp.fsum(v for A, v in P.items() if (A >> i) & 1) for i in range(n)]
    Ji = [mp.fsum(v for A, v in P.items() if (A >> i) & 1 and bin(A).count('1') >= 2) for i in range(n)]
    return sig2, Var, W, I, J, Inf, Ji

def ratios(fvals, q, c=1):
    P = biased_spectrum(fvals, q)
    sig2, Var, W, I, J, Inf, Ji = stats(P, q)
    out = {}
    if Var > 0 and I > 0:
        cred = mp.fsum(Inf[i] * max(mp.mpf(0), mp.log(c * (Inf[i] / sig2[i]) / Var)) for i in range(len(q)) if Inf[i] > 0)
        out['r1'] = float((Var * mp.log(1 / Var) - cred) / I)
    if W > 0 and J > 0:
        cred = mp.fsum(Ji[i] * max(mp.mpf(0), mp.log(c * (Ji[i] / sig2[i]) / W)) for i in range(len(q)) if Ji[i] > 0)
        out['r2'] = float((W * mp.log(1 / W) - cred) / J)
    return out

def rand_q(n, rng):
    q = []
    for _ in range(n):
        t = rng.random()
        if t < 0.3: v = 10 ** (-rng.uniform(0, 10))
        elif t < 0.6: v = 1 - 10 ** (-rng.uniform(0, 10))
        else: v = rng.uniform(0.02, 0.98)
        q.append(min(max(v, 1e-12), 1 - 1e-12))
    return q

def ltf(n, rng):
    w = [rng.choice([rng.uniform(0, 1), rng.randint(1, 5)]) for _ in range(n)]
    th = rng.uniform(0, sum(w))
    return [1 if sum(w[i] for i in range(n) if (x >> i) & 1) >= th else 0 for x in range(1 << n)]

def randmono(n, rng):
    k = rng.randint(1, 4)
    mins = [rng.getrandbits(n) for _ in range(k)]
    return [1 if any((x & m) == m for m in mins) else 0 for x in range(1 << n)]

def randfun(n, rng):
    p = rng.random()
    return [1 if rng.random() < p else 0 for _ in range(1 << n)]

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1]))
    T = int(sys.argv[2]); nmax = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    kinds = sys.argv[4].split(',') if len(sys.argv) > 4 else ['ltf', 'mono', 'rand']
    worst = {'r1': (-1e9, None), 'r2': (-1e9, None)}
    for trial in range(T):
        n = rng.randint(2, nmax)
        kind = rng.choice(kinds)
        f = ltf(n, rng) if kind == 'ltf' else (randmono(n, rng) if kind == 'mono' else randfun(n, rng))
        if len(set(f)) < 2: continue
        q = rand_q(n, rng)
        o = ratios(f, q)
        for key in o:
            if o[key] > worst[key][0]:
                worst[key] = (o[key], (kind, n, q, f))
        if trial % 200 == 0:
            print(trial, {k: round(v[0], 4) for k, v in worst.items()}, flush=True)
    for k, v in worst.items():
        print('WORST', k, v[0], v[1])

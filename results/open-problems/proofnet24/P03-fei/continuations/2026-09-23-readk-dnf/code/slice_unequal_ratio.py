# Max of Psi(d)/Var(d) over slices d = 1[N = s] with unequal biases (all s, m <= 8), to support the sentence in the
# paper that every computed slice has Psi < (2 + ln 4) Var.  Reuses the exact transform of slab_damped.py.
import mpmath as mp, random, sys
from slab_damped import biased_transform, popcount
rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); mmax = int(sys.argv[3])
best = (0, None)
for t in range(T):
    m = rng.randint(1, mmax)
    spec = []
    mode = rng.random()
    for _ in range(m):
        v = rng.random()
        if mode < 0.3: spec.append(('hi', rng.uniform(0.3, 2.5)))           # biases near one: the conjunction regime
        elif v < 0.35: spec.append(('lo', rng.uniform(0, 9)))
        elif v < 0.55: spec.append(('hi', rng.uniform(0, 9)))
        else: spec.append(('mid', rng.uniform(0.02, 0.98)))
    mp.mp.dps = int(40 + 2 * sum(e for k, e in spec if k != 'mid') + 2 * m)
    q = [mp.mpf(10) ** (-mp.mpf(e)) if k == 'lo' else (1 - mp.mpf(10) ** (-mp.mpf(e)) if k == 'hi' else mp.mpf(e)) for k, e in spec]
    for s in range(0, m + 1):
        d = [1 if bin(y).count('1') == s else 0 for y in range(1 << m)]
        c = biased_transform(d, q)
        var = c[0] * (1 - c[0])
        if var <= 0: continue
        psi = mp.mpf(0)
        for B in range(1, 1 << m):
            if c[B] == 0: continue
            sB = mp.mpf(1)
            for i in range(m):
                if (B >> i) & 1: sB *= 4 * q[i] * (1 - q[i])
            psi += c[B] ** 2 / (popcount(B) + 1) * mp.log(sB / c[B] ** 2)
        r = psi / var
        if r > best[0]: best = (r, (m, s, [mp.nstr(x, 3) for x in q]))
print('instances', T, 'm <=', mmax, 'max Psi/Var over all slices', mp.nstr(best[0], 6), best[1], ' 2 + ln 4 =', mp.nstr(2 + mp.log(4), 6))

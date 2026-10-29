"""Brute force on small graphs: I = E[c] - E_e[c] - E_f[c] + E_ef[c] (c = cycle rank, E_X conditioned on X open) for the measure
t^|A| s^c(A); I >= 0 for all s in (0,1) at fixed t is equivalent to the covariance margin falling in s. Random graphs, all edge pairs."""
import itertools, random, sys
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 1)

def crank(n, A):
    p = list(range(n)); c = 0
    def f(x):
        while p[x] != x: p[x] = p[p[x]]; x = p[x]
        return x
    for a, b in A:
        ra, rb = f(a), f(b)
        if ra == rb: c += 1
        else: p[ra] = rb
    return c

worst = (1e9, None)
for trial in range(int(sys.argv[2]) if len(sys.argv) > 2 else 30):
    n = random.choice([5, 6, 7]); E = [e for e in itertools.combinations(range(n), 2) if random.random() < 0.6]
    if len(E) > 14 or len(E) < 4: continue
    cyc = [crank(n, [E[i] for i in range(len(E)) if m >> i & 1]) for m in range(1 << len(E))]
    size = [bin(m).count("1") for m in range(1 << len(E))]
    for t in (0.1, 0.5, 2.0, 8.0):
        for s in (0.05, 0.3, 0.7, 0.95):
            w = [t ** size[m] * s ** cyc[m] for m in range(1 << len(E))]
            for i, j in itertools.combinations(range(len(E)), 2):
                def ex(mask):
                    Z = sum(w[m] for m in range(1 << len(E)) if m & mask == mask)
                    return sum(w[m] * cyc[m] for m in range(1 << len(E)) if m & mask == mask) / Z
                I = ex(0) - ex(1 << i) - ex(1 << j) + ex((1 << i) | (1 << j))
                if I < worst[0]: worst = (I, (n, E, E[i], E[j], t, s))
print("min I", worst[0], worst[1])

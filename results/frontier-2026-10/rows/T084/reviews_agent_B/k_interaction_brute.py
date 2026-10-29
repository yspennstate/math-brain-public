"""Brute force on small graphs: I_k = E[k] - E_e[k] - E_f[k] + E_ef[k] for RC weight lam^|A| q^k(A) (k = components); I_k >= 0 on
(0,1) at fixed lam is the margin falling in q. Reports the minimum separately for adjacent and disjoint pairs."""
import itertools, random, sys
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 1)

def ncomp(n, A):
    p = list(range(n)); k = n
    def f(x):
        while p[x] != x: p[x] = p[p[x]]; x = p[x]
        return x
    for a, b in A:
        ra, rb = f(a), f(b)
        if ra != rb: p[ra] = rb; k -= 1
    return k

worst = {True: (1e9, None), False: (1e9, None)}
for trial in range(int(sys.argv[2]) if len(sys.argv) > 2 else 12):
    n = random.choice([5, 6, 7]); E = [e for e in itertools.combinations(range(n), 2) if random.random() < 0.6]
    if len(E) > 14 or len(E) < 4: continue
    M = 1 << len(E)
    kk = [ncomp(n, [E[i] for i in range(len(E)) if m >> i & 1]) for m in range(M)]
    size = [bin(m).count("1") for m in range(M)]
    for lam in (0.05, 0.3, 1.0, 3.0):
        for q in (0.02, 0.2, 0.5, 0.8, 0.97):
            w = [lam ** size[m] * q ** kk[m] for m in range(M)]
            def ex(mask):
                Z = sum(w[m] for m in range(M) if m & mask == mask)
                return sum(w[m] * kk[m] for m in range(M) if m & mask == mask) / Z
            e0 = ex(0); e1 = [ex(1 << i) for i in range(len(E))]
            for i, j in itertools.combinations(range(len(E)), 2):
                adj = len(set(E[i]) & set(E[j])) == 1
                I = e0 - e1[i] - e1[j] + ex((1 << i) | (1 << j))
                if I < worst[adj][0]: worst[adj] = (I, (n, E, E[i], E[j], lam, q))
print("adjacent min I_k", worst[True][0], worst[True][1])
print("disjoint min I_k", worst[False][0], worst[False][1])

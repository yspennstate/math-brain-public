# Damped inequality for the derivatives of linear threshold functions under product measures.
# For f = 1[w.x >= theta] (w >= 0) and a product measure mu with biases q_i, the derivative
# d_j = f(x^{j<-1}) - f(x^{j<-0}) is the indicator of a slab {theta - w_j <= W_{-j} < theta} of the other coordinates.
# With the biased Fourier coefficients d~_j(B) (orthonormal basis prod_{i in B} (x_i - q_i)/sqrt(q_i(1-q_i))) and
# sigma_B^2 = prod_{i in B} 4 q_i (1 - q_i), the exact identity (every Boolean function, every product measure)
#     sum_{|A|>=2} P(A) ln(sigma_A^2/P(A)) = sum_j sigma_j^2 Psi(d_j),
#     Psi(d) = sum_{B != empty} (d~(B)^2 / (|B|+1)) ln(sigma_B^2 / d~(B)^2),
# holds, where P(A) is the biased spectral distribution of g = 1 - 2f normalised as in the paper (P(A) = sigma_A^2 ...).
# If Psi(d_j) <= C Var(d_j) for every j, then (singletons <= 2J) the strengthened biased inequality
#     sum_{A != empty} P(A) ln(sigma_A^2/P(A)) <= (2 + C) J <= 2 (2 + C) (I - Var)
# follows.  This script measures max_j Psi(d_j)/Var(d_j) over random threshold functions and product measures and checks
# the identity on every instance.
import mpmath as mp, random, sys

def biased_transform(vals, q):
    # vals: list of 2^m function values on {0,1}^m (bit i of the index = x_i); returns the coefficients
    # f~(B) indexed by the bitmask of B, for the orthonormal basis prod (x_i - q_i)/sqrt(q_i (1 - q_i))
    a = list(vals); m = len(q)
    for i in range(m):
        s = mp.sqrt(q[i] * (1 - q[i])); bit = 1 << i
        for x in range(1 << m):
            if not x & bit:
                f0, f1 = a[x], a[x | bit]
                a[x] = (1 - q[i]) * f0 + q[i] * f1
                a[x | bit] = s * (f1 - f0)
    return a

def popcount(x): return bin(x).count('1')

def analyse(w, theta, q, check=True):
    n = len(w)
    f = [1 if sum(w[i] for i in range(n) if (x >> i) & 1) >= theta else 0 for x in range(1 << n)]
    sig2 = [4 * q[i] * (1 - q[i]) for i in range(n)]
    ratios = []; Jtot = mp.mpf(0); psisum = mp.mpf(0)
    for j in range(n):
        idx = [i for i in range(n) if i != j]; qq = [q[i] for i in idx]; m = n - 1
        d = []
        for y in range(1 << m):
            x = 0
            for t, i in enumerate(idx):
                if (y >> t) & 1: x |= 1 << i
            d.append(f[x | (1 << j)] - f[x])
        c = biased_transform(d, qq)
        var = mp.fsum(c[B] ** 2 for B in range(1, 1 << m))
        psi = mp.mpf(0)
        for B in range(1, 1 << m):
            if c[B] == 0: continue
            sB = mp.mpf(1)
            for t in range(m):
                if (B >> t) & 1: sB *= 4 * qq[t] * (1 - qq[t])
            psi += c[B] ** 2 / (popcount(B) + 1) * mp.log(sB / c[B] ** 2)
        Jtot += sig2[j] * var; psisum += sig2[j] * psi
        if var > 0: ratios.append(psi / var)
    out = {'rmax': max(ratios) if ratios else mp.mpf(0), 'J': Jtot}
    if check:
        # full biased spectrum of g = 1 - 2f, P(A) = g~(A)^2 in the orthonormal basis (see the note below)
        g = [1 - 2 * v for v in f]
        cg = biased_transform(g, q)
        lhs2 = mp.mpf(0); lhs1 = mp.mpf(0); I = mp.mpf(0); V = mp.mpf(0)
        for A in range(1, 1 << n):
            if cg[A] == 0: continue
            sA = mp.mpf(1)
            for t in range(n):
                if (A >> t) & 1: sA *= 4 * q[t] * (1 - q[t])
            # the paper's P(A): the spectral weight of g in the basis prod (1 - 2x_i ...) normalised so that
            # P(A + {j}) = sigma_j^2 d~_j(A)^2 for A not containing j; with f~ the orthonormal coefficients of f,
            # f~(A + {j}) = sqrt(q_j(1-q_j)) d~_j(A), so sigma_j^2 d~_j(A)^2 = 4 f~(A+{j})^2, i.e. P(A) = 4 f~(A)^2 = g~(A)^2.
            PA = cg[A] ** 2
            k = popcount(A)
            I += k * PA; V += PA
            term = PA * mp.log(sA / PA)
            if k >= 2: lhs2 += term
            else: lhs1 += term
        out['id_err'] = abs(lhs2 - psisum) / (abs(lhs2) + mp.mpf(10) ** -30)
        out['lhs'] = lhs1 + lhs2; out['I'] = I; out['V'] = V
        out['full'] = (lhs1 + lhs2) / (I - V) if I > V else None
    return out

def gen(rng, nmax):
    n = rng.randint(2, nmax)
    kind = rng.random()
    if kind < 0.15: w = [1.0] * n
    elif kind < 0.35: w = [float(rng.randint(1, 3)) for _ in range(n)]
    elif kind < 0.55: w = [2.0 ** rng.randint(0, 6) for _ in range(n)]
    elif kind < 0.75: w = [rng.expovariate(1.0) + 0.01 for _ in range(n)]
    elif kind < 0.9: w = [float(n)] + [1.0] * (n - 1)
    else: w = [float(rng.randint(1, 3)) * (1 + 0.001 * rng.random()) for _ in range(n)]
    theta = rng.uniform(0.001, sum(w))
    spec = []
    u = rng.random()
    for _ in range(n):
        v = rng.random() if u > 0.2 else 0.0
        if v < 0.35: spec.append(('lo', rng.uniform(0, 10)))
        elif v < 0.6: spec.append(('hi', rng.uniform(0, 10)))
        else: spec.append(('mid', rng.uniform(0.02, 0.98)))
    if u <= 0.2: spec = [spec[0]] * n
    return w, theta, spec

def build(spec):
    need = 40 + 2 * sum(e for k, e in spec if k in ('lo', 'hi')) + 2 * len(spec)
    mp.mp.dps = int(need)
    q = []
    for k, e in spec:
        if k == 'lo': q.append(mp.mpf(10) ** (-mp.mpf(e)))
        elif k == 'hi': q.append(1 - mp.mpf(10) ** (-mp.mpf(e)))
        else: q.append(mp.mpf(e))
    return q

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); nmax = int(sys.argv[3])
    worst = (mp.mpf(0), None); worst_full = (mp.mpf(0), None); maxid = mp.mpf(0)
    for t in range(T):
        w, theta, spec = gen(rng, nmax)
        q = build(spec)
        o = analyse(w, theta, q, check=True)
        maxid = max(maxid, o['id_err'])
        if o['rmax'] > worst[0]:
            worst = (o['rmax'], (len(w), [round(v, 3) for v in w], round(theta, 3), [mp.nstr(v, 3) for v in q]))
        if o.get('full') is not None and o['full'] > worst_full[0]:
            worst_full = (o['full'], (len(w), [round(v, 3) for v in w], round(theta, 3), [mp.nstr(v, 3) for v in q]))
        if t % 100 == 0:
            print(t, 'max Psi/Var %s' % mp.nstr(worst[0], 5), 'max LHS/(I-V) %s nats' % mp.nstr(worst_full[0], 5),
                  'identity rel err %s' % mp.nstr(maxid, 3), flush=True)
    print('DONE max Psi/Var', mp.nstr(worst[0], 6), worst[1])
    print('max LHS/(I-V) nats', mp.nstr(worst_full[0], 6), '=', mp.nstr(worst_full[0] / mp.log(2), 6), 'bits', worst_full[1])
    print('max identity relative error', mp.nstr(maxid, 3))

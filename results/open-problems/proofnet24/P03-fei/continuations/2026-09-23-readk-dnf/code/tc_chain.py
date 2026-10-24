# Chain-rule form of the total-correlation lemma for threshold sets.  For an ordering x_{(1)}, ..., x_{(n)},
#     TC(mu_A) = sum_k I_A(x_(k) ; x_(<k)),
# and  alpha TC / I = TC / (4 sum_k delta_k)  with  delta_k = |m_k - q_k|,  m_k = mu_A(x_k = 1)
# (for an up-set, m_k - q_k = q_k (1 - q_k) rho_k / alpha).  This script measures, per coordinate,
#     c_k = I_A(x_(k) ; x_(<k)) / (4 delta_(k))
# for the orderings by decreasing and by increasing weight and, for n <= 6, the best ordering (smallest max_k c_k).
# If max_k c_k is bounded for some canonical ordering, the lemma reduces to a one-coordinate inequality.
import mpmath as mp, random, sys, itertools
import tc_pairwise as T

def prefix_entropies(n, P, inA, alpha, order):
    # H_A(x_(1..k)) for k = 0..n
    out = [mp.mpf(0)]
    for k in range(1, n + 1):
        idx = order[:k]
        tab = {}
        for x in range(1 << n):
            if not inA[x]: continue
            key = tuple((x >> i) & 1 for i in idx)
            tab[key] = tab.get(key, 0) + P[x]
        out.append(mp.fsum(-(v / alpha) * mp.log(v / alpha) for v in tab.values() if v > 0))
    return out

def chain_terms(n, q, inA, order, P=None):
    if P is None: P = T.measure(n, q)
    alpha = mp.fsum(P[x] for x in range(1 << n) if inA[x])
    marg = [mp.fsum(P[x] for x in range(1 << n) if inA[x] and (x >> j) & 1) / alpha for j in range(n)]
    Hp = prefix_entropies(n, P, inA, alpha, order)
    terms = []
    for k in range(n):
        j = order[k]
        Hcond = Hp[k + 1] - Hp[k]                    # H(x_j | x_(<k))
        mi = T.H2(marg[j]) - Hcond
        d = abs(marg[j] - q[j])
        terms.append((j, mi, d))
    return alpha, terms

def relevant(n, inA):
    # combinatorial relevance: coordinate j matters iff flipping it changes membership somewhere
    return [any(inA[x] != inA[x ^ (1 << j)] for x in range(1 << n)) for j in range(n)]

def ratios(terms, rel=None):
    # an irrelevant coordinate is independent of the others under mu_A (delta = MI = 0 exactly); skip it rather
    # than divide two rounding errors
    out = []
    for j, mi, d in terms:
        if rel is not None and not rel[j]: continue
        if d > 0: out.append(mi / (4 * d))
        elif mi > mp.mpf(10) ** (-(mp.mp.dps - 10)): out.append(mp.inf)
    return out

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); Tn = int(sys.argv[2]); nmax = int(sys.argv[3])
    keys = ['dec', 'inc', 'best']
    worst = {k: (mp.mpf(0), None) for k in keys}
    worst_tc = (mp.mpf(0), None)
    for t in range(Tn):
        n, w, theta, spec = T.gen(rng)          # T.gen reads the largest n from sys.argv[3]
        q = T.build(spec)
        base = [sum(w[i] for i in range(n) if (x >> i) & 1) >= theta for x in range(1 << n)]
        P = T.measure(n, q)
        for side in (0, 1):
            inA = base if side == 0 else [not v for v in base]
            alpha = mp.fsum(P[x] for x in range(1 << n) if inA[x])
            if alpha == 0 or alpha == 1: continue
            dec = sorted(range(n), key=lambda i: -w[i]); inc = dec[::-1]
            rel = relevant(n, inA)
            res = {}
            for name, order in (('dec', dec), ('inc', inc)):
                a, terms = chain_terms(n, q, inA, order, P)
                r = ratios(terms, rel); res[name] = max(r) if r else mp.mpf(0)
                if name == 'dec':
                    tc = mp.fsum(mi for _, mi, _ in terms); sd = mp.fsum(d for _, _, d in terms)
                    if sd > 0 and tc / (4 * sd) > worst_tc[0]:
                        worst_tc = (tc / (4 * sd), (n, [round(v, 3) for v in w], round(theta, 3), side))
            if n <= 6:
                b = mp.inf
                for order in itertools.permutations(range(n)):
                    a, terms = chain_terms(n, q, inA, list(order), P)
                    r = ratios(terms, rel); v = max(r) if r else mp.mpf(0)
                    if v < b: b = v
                res['best'] = b
            for k in keys:
                if k in res and res[k] > worst[k][0]:
                    worst[k] = (res[k], (n, [round(v, 3) for v in w], round(theta, 3), side,
                                         [mp.nstr(v, 3) for v in q], mp.nstr(alpha, 3)))
        if t % 100 == 0:
            print(t, ' '.join('%s %s' % (k, mp.nstr(worst[k][0], 4)) for k in keys), 'tc', mp.nstr(worst_tc[0], 4), flush=True)
    for k in keys:
        print('%-5s worst max_k c_k = %s at %s' % (k, mp.nstr(worst[k][0], 6), worst[k][1]))
    print('alpha TC / I worst', mp.nstr(worst_tc[0], 6), worst_tc[1])

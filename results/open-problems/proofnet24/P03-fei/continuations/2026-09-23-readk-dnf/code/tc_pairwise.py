# Total correlation of mu_A for linear threshold sets A = {w.x >= theta} (w >= 0) under product measures,
# through the one-coordinate split
#     TC(mu_A) = lam TC(mu_{A_1}) + (1 - lam) TC(mu_{A_0}) + sum_{k != j} I_A(x_j ; x_k),   lam = q_j alpha_1 / alpha,
# where A_b is the restriction x_j = b.  Multiplying by alpha, alpha lam = q_j alpha_1, and
# I(A) = Inf_j + q_j I(A_1) + (1 - q_j) I(A_0); so  alpha TC <= C I  follows by induction on n (restrictions of
# threshold sets are threshold sets) from the one-step inequality
#     (**)  alpha * sum_{k != j} I_A(x_j ; x_k) <= C * Inf_j,   Inf_j = sigma_j^2 rho_j,
# for SOME coordinate j of every threshold set.  This script measures, over random threshold sets and product
# measures (both A and its complement, which after negating every input is again a threshold set):
#   tc     = alpha TC / I
#   rmin   = min_j R_j,  R_j = alpha sum_k I_A(x_j; x_k) / Inf_j     (what the induction needs)
#   rheavy = R_j at the heaviest weight, rinf = R_j at the largest Inf_j, rrho = at the largest rho_j
#   ravg   = sum_j alpha S_j / sum_j Inf_j = 2 alpha sum_{j<k} I_A(x_j;x_k) / I   (>= rmin)
# It also checks the split identity on every fifth instance.  mpmath, with 40 digits more than the smallest
# cell probability needs (a set of measure 1 - 1e-35 is invisible at 30 digits).
import mpmath as mp, random, sys
mp.mp.dps = 30

def H2(p):
    return -(p * mp.log(p) + (1 - p) * mp.log(1 - p)) if 0 < p < 1 else mp.mpf(0)

def measure(n, q):
    N = 1 << n
    P = [mp.mpf(1)] * N
    for x in range(N):
        p = mp.mpf(1)
        for i in range(n):
            p *= q[i] if (x >> i) & 1 else (1 - q[i])
        P[x] = p
    return P

def tc_of(n, P, inA):
    alpha = mp.fsum(P[x] for x in range(1 << n) if inA[x])
    if alpha == 0: return mp.mpf(0), alpha
    H = mp.fsum(-(P[x] / alpha) * mp.log(P[x] / alpha) for x in range(1 << n) if inA[x] and P[x] > 0)
    Hm = mp.mpf(0)
    for i in range(n):
        mi = mp.fsum(P[x] for x in range(1 << n) if inA[x] and (x >> i) & 1) / alpha
        Hm += H2(mi)
    return Hm - H, alpha

def analyse(n, q, inA, check_split=True):
    N = 1 << n
    P = measure(n, q)
    TC, alpha = tc_of(n, P, inA)
    if alpha == 0 or alpha == 1: return None
    rho = []
    for j in range(n):
        s = mp.fsum(P[x] for x in range(N) if not (x >> j) & 1 and inA[x] != inA[x | (1 << j)])
        rho.append(s / (1 - q[j]))
    Inf = [4 * q[j] * (1 - q[j]) * rho[j] for j in range(n)]
    I = mp.fsum(Inf)
    # pairwise joint tables under mu_A
    cell = {}
    marg = [mp.fsum(P[x] for x in range(N) if inA[x] and (x >> j) & 1) / alpha for j in range(n)]
    S = [mp.mpf(0)] * n
    MI = {}
    for j in range(n):
        for k in range(j + 1, n):
            p11 = mp.fsum(P[x] for x in range(N) if inA[x] and (x >> j) & 1 and (x >> k) & 1) / alpha
            p10 = marg[j] - p11; p01 = marg[k] - p11; p00 = 1 - marg[j] - marg[k] + p11
            m = mp.mpf(0)
            for pab, pa, pb in ((p11, marg[j], marg[k]), (p10, marg[j], 1 - marg[k]),
                                (p01, 1 - marg[j], marg[k]), (p00, 1 - marg[j], 1 - marg[k])):
                if pab > 0 and pa > 0 and pb > 0: m += pab * mp.log(pab / (pa * pb))
            MI[(j, k)] = m; S[j] += m; S[k] += m
    R = [alpha * S[j] / Inf[j] if Inf[j] > 0 else None for j in range(n)]
    Rv = [r for r in R if r is not None]
    out = {'tc': alpha * TC / I, 'rmin': min(Rv), 'ravg': alpha * mp.fsum(S) / I, 'alpha': alpha, 'I': I,
           'rinf': R[max(range(n), key=lambda j: Inf[j])], 'rrho': R[max(range(n), key=lambda j: rho[j])]}
    if check_split:
        j = max(range(n), key=lambda j: Inf[j])
        # restrictions A_1, A_0 as sets on the other coordinates (keep the index space, fix x_j)
        a1 = mp.fsum(P[x] for x in range(N) if inA[x] and (x >> j) & 1) / q[j]
        a0 = mp.fsum(P[x] for x in range(N) if inA[x] and not (x >> j) & 1) / (1 - q[j])
        def tc_restricted(b):
            # measure on the other coordinates only: drop coordinate j
            idx = [i for i in range(n) if i != j]
            qq = [q[i] for i in idx]; m = len(idx)
            PP = measure(m, qq)
            inB = []
            for y in range(1 << m):
                x = 0
                for t, i in enumerate(idx):
                    if (y >> t) & 1: x |= 1 << i
                if b: x |= 1 << j
                inB.append(inA[x])
            return tc_of(m, PP, inB)
        t1, _ = tc_restricted(1); t0, _ = tc_restricted(0)
        lam = q[j] * a1 / alpha
        rhs = lam * t1 + (1 - lam) * t0 + S[j]
        out['split_err'] = abs(TC - rhs)
    return out

def gen(rng):
    # returns the biases as (kind, exponent) specs so that they can be built after the precision is set:
    # ('lo', e) -> 10^-e, ('hi', e) -> 1 - 10^-e, ('mid', u) -> u
    n = rng.randint(2, int(sys.argv[3]))
    kind = rng.random()
    if kind < 0.2: w = [1.0] * n
    elif kind < 0.4: w = [float(rng.randint(1, 3)) for _ in range(n)]
    elif kind < 0.55: w = [2.0 ** rng.randint(0, 6) for _ in range(n)]
    elif kind < 0.7: w = [rng.expovariate(1.0) + 0.01 for _ in range(n)]
    elif kind < 0.85: w = [float(n)] + [1.0] * (n - 1)            # one heavy input
    else: w = [float(rng.randint(1, 3)) * (1 + 0.001 * rng.random()) for _ in range(n)]
    theta = rng.uniform(0.001, sum(w))
    u = rng.random()
    if u < 0.25:
        e = rng.uniform(0, 10); spec = [('lo', e)] * n
    else:
        spec = []
        for _ in range(n):
            v = rng.random()
            if v < 0.35: spec.append(('lo', rng.uniform(0, 12)))
            elif v < 0.6: spec.append(('hi', rng.uniform(0, 12)))
            else: spec.append(('mid', rng.uniform(0.01, 0.99)))
    return n, w, theta, spec

def build(spec):
    # precision: enough digits to resolve the smallest cell probability, plus 40
    need = 40 + sum(e for k, e in spec if k in ('lo', 'hi')) + 2 * len(spec)
    mp.mp.dps = int(need)
    q = []
    for k, e in spec:
        if k == 'lo': q.append(mp.mpf(10) ** (-mp.mpf(e)))
        elif k == 'hi': q.append(1 - mp.mpf(10) ** (-mp.mpf(e)))
        else: q.append(mp.mpf(e))
    return q

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2])
    keys = ['tc', 'rmin', 'rinf', 'rrho', 'ravg']
    worst = {k: (mp.mpf(0), None) for k in keys}
    maxerr = mp.mpf(0); cnt = 0
    for t in range(T):
        n, w, theta, spec = gen(rng)
        q = build(spec)
        base = [sum(w[i] for i in range(n) if (x >> i) & 1) >= theta for x in range(1 << n)]
        for side in (0, 1):
            inA = base if side == 0 else [not v for v in base]
            o = analyse(n, q, inA, check_split=(t % 5 == 0))
            if o is None: continue
            cnt += 1
            if 'split_err' in o: maxerr = max(maxerr, o['split_err'])
            for k in keys:
                if o[k] is not None and o[k] > worst[k][0]:
                    worst[k] = (o[k], (n, [round(v, 3) for v in w], round(theta, 3), side,
                                       [mp.nstr(v, 3) for v in q], mp.nstr(o['alpha'], 3)))
        if t % 200 == 0:
            print(t, ' '.join('%s %s' % (k, mp.nstr(worst[k][0], 4)) for k in keys), 'splitErr', mp.nstr(maxerr, 3), flush=True)
    print('instances', cnt, 'max split identity error', mp.nstr(maxerr, 3))
    for k in keys:
        print('%-6s worst %s at %s' % (k, mp.nstr(worst[k][0], 6), worst[k][1]))

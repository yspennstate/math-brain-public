# Checks, on exact instances, the two bounds for the damped slice functional derived on 23 Sep (evening):
#   d = 1[N = s], N = sum of independent Ber(q_i) on m coordinates, rho = P(N = s), Lambda = sum 4 q_i (1 - q_i),
#   Psi(d) = sum_{B != empty} (d~(B)^2/(|B|+1)) ln(sigma_B^2/d~(B)^2).
#   (N)  if rho >= 1/2:  Lambda <= 930 Var(d)  and  Psi(d) <= 7.04 Var(d);
#   (Bk) if rho <  1/2:  Psi(d) <= rho (7.35 + 5.35 ln(1/rho) / sqrt(Lambda)).
# Also checks the exact coefficient formula d~(B)^2 = prod_{i in B} q_i(1-q_i) * (b-th backward difference of the pmf of
# the count outside B, at s)^2 against the direct transform, and the intermediate per-level Gibbs bound.
import mpmath as mp, random, sys
from slab_damped import biased_transform, popcount

def pmf_count(qs):
    p = [mp.mpf(1)]
    for q in qs:
        new = [mp.mpf(0)] * (len(p) + 1)
        for k, v in enumerate(p):
            new[k] += v * (1 - q); new[k + 1] += v * q
        p = new
    return p

def check(q, s):
    m = len(q)
    d = [1 if bin(y).count('1') == s else 0 for y in range(1 << m)]
    c = biased_transform(d, q)
    rho = c[0]; var = rho * (1 - rho)
    Lam = mp.fsum(4 * qi * (1 - qi) for qi in q)
    psi = mp.mpf(0); maxform = mp.mpf(0)
    W = {}
    for B in range(1, 1 << m):
        b = popcount(B)
        inside = [q[i] for i in range(m) if (B >> i) & 1]; outside = [q[i] for i in range(m) if not (B >> i) & 1]
        p = pmf_count(outside)
        get = lambda k: p[k] if 0 <= k < len(p) else mp.mpf(0)
        diff = mp.fsum((-1) ** k * mp.binomial(b, k) * get(s - k) for k in range(b + 1))
        form = diff ** 2
        for qi in inside: form *= qi * (1 - qi)
        maxform = max(maxform, abs(form - c[B] ** 2) / (c[B] ** 2 + mp.mpf(10) ** (-mp.mp.dps + 10)))
        W[b] = W.get(b, 0) + c[B] ** 2
        if c[B] == 0: continue
        sB = mp.mpf(1)
        for qi in inside: sB *= 4 * qi * (1 - qi)
        psi += c[B] ** 2 / (b + 1) * mp.log(sB / c[B] ** 2)
    # per-level Gibbs bound
    from itertools import combinations
    gib = mp.mpf(0)
    sig = [4 * qi * (1 - qi) for qi in q]
    # elementary symmetric polynomials of sigma^2
    e = [mp.mpf(1)] + [mp.mpf(0)] * m
    for x in sig:
        for k in range(m, 0, -1): e[k] += e[k - 1] * x
    for b, Wb in W.items():
        if Wb > 0: gib += Wb / (b + 1) * mp.log(e[b] / Wb)
    out = {'rho': rho, 'var': var, 'psi': psi, 'Lam': Lam, 'formula_relerr': maxform, 'gibbs': gib}
    if rho >= mp.mpf(1) / 2:
        out['N_ok'] = (Lam <= 930 * var) and (psi <= mp.mpf('7.04') * var)
        out['N_ratio'] = psi / var; out['N_lam'] = Lam / var
    else:
        bound = rho * (mp.mpf('7.35') + mp.mpf('5.35') * mp.log(1 / rho) / mp.sqrt(Lam))
        out['Bk_ok'] = psi <= bound and gib <= bound
        out['Bk_ratio'] = max(psi, gib) / bound
    return out

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); mmax = int(sys.argv[3])
    worstN = (0, None); worstB = (0, None); worstLam = (0, None); maxerr = mp.mpf(0); nN = nB = 0; fails = 0
    for t in range(T):
        m = rng.randint(1, mmax)
        spec = []
        for _ in range(m):
            v = rng.random()
            if v < 0.35: spec.append(('lo', rng.uniform(0, 9)))
            elif v < 0.55: spec.append(('hi', rng.uniform(0, 9)))
            else: spec.append(('mid', rng.uniform(0.02, 0.98)))
        mp.mp.dps = int(40 + 2 * sum(e for k, e in spec if k != 'mid') + 2 * m)
        q = [mp.mpf(10) ** (-mp.mpf(e)) if k == 'lo' else (1 - mp.mpf(10) ** (-mp.mpf(e)) if k == 'hi' else mp.mpf(e)) for k, e in spec]
        s = rng.randint(0, m)
        o = check(q, s)
        if o['var'] == 0: continue
        maxerr = max(maxerr, o['formula_relerr'])
        if 'N_ok' in o:
            nN += 1; fails += 0 if o['N_ok'] else 1
            if o['N_ratio'] > worstN[0]: worstN = (o['N_ratio'], (m, s, [mp.nstr(x, 3) for x in q]))
            if o['N_lam'] > worstLam[0]: worstLam = (o['N_lam'], (m, s, [mp.nstr(x, 3) for x in q]))
        else:
            nB += 1; fails += 0 if o['Bk_ok'] else 1
            if o['Bk_ratio'] > worstB[0]: worstB = (o['Bk_ratio'], (m, s, [mp.nstr(x, 3) for x in q], mp.nstr(o['rho'], 3)))
    print('instances rho>=1/2:', nN, ' rho<1/2:', nB, ' failures:', fails)
    print('max coefficient-formula relative error', mp.nstr(maxerr, 3))
    print('rho>=1/2: max Psi/Var', mp.nstr(worstN[0], 5), '(bound 7.04)', worstN[1])
    print('rho>=1/2: max Lambda/Var', mp.nstr(worstLam[0], 5), '(bound 930)', worstLam[1])
    print('rho<1/2: max max(Psi, Gibbs)/bound', mp.nstr(worstB[0], 5), '(must be <= 1)', worstB[1])

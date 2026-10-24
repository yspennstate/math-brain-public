# Exact audit (mpmath) of every inequality in the near-dictator case of the strengthened biased form for
# T_{t,r}: some coordinate j0 has rho_{j0} = max_j rho_j = 1 - eps with eps < delta (delta = 0.1).
# Checked on random instances built to land in that case, plus random instances filtered to it:
#   L' <= 1.128 eps, Lambda' <= 4.51 eps (Lemma B1); N'-bar = t-1
#   sigma_{j0}^2 E(e) <= 2.43 J_{j0}          (sets containing j0, |A| >= 2)
#   J_i >= 0.9 eps sigma_i^2 (i up-type), J_i >= 0.493 q sigma_i^2 (i down-type)   [q = q_{j0} <= 1/2]
#   R <= 22.3 eps Lambda_U + 1.88 q Lambda_D   (sets avoiding j0, |A| >= 2), and each family bound
#   LHS_1 <= 2J, LHS <= 26.8 J, and in case A (all rho <= 0.9) LHS <= 263 J (via LHS <= 26.3 I)
import mpmath as mp, random, sys
from isoper3 import biased_P
mp.mp.dps = 50
DELTA = mp.mpf('0.1')

def analyse(r, t, q):
    f = [1 if bin(x).count('1') >= t else 0 for x in range(1 << r)]
    P = biased_P(f, q); q = [mp.mpf(v) for v in q]
    sig2 = [4 * v * (1 - v) for v in q]
    V = mp.fsum(P[1:]); I = mp.fsum(bin(A).count('1') * P[A] for A in range(1, 1 << r))
    J = mp.fsum(bin(A).count('1') * P[A] for A in range(1, 1 << r) if bin(A).count('1') >= 2)
    Inf = [mp.fsum(P[A] for A in range(1 << r) if A >> i & 1) for i in range(r)]
    rho = [Inf[i] / sig2[i] for i in range(r)]
    Ji = [sig2[i] * rho[i] * (1 - rho[i]) for i in range(r)]
    ent = lambda A: P[A] * mp.log(mp.fprod(sig2[i] for i in range(r) if A >> i & 1) / P[A]) if P[A] > 0 else mp.mpf(0)
    lhs = mp.fsum(ent(A) for A in range(1, 1 << r))
    lhs1 = mp.fsum(ent(1 << i) for i in range(r))
    out = {'r': r, 't': t, 'lhs_over_J': lhs / J if J > 0 else None, 'lhs1_over_J': lhs1 / J if J > 0 else None}
    j0 = max(range(r), key=lambda i: rho[i]); eps = 1 - rho[j0]
    if eps >= DELTA:
        out['case'] = 'A'; out['lhs_over_I'] = lhs / I
        return out
    out['case'] = 'B'
    # normalise to q_{j0} <= 1/2 by the global negation symmetry (all quantities used are invariant)
    if q[j0] > mp.mpf('0.5'):
        q = [1 - v for v in q]; t = r - t + 1
    qq = q[j0]
    O = [i for i in range(r) if i != j0]
    qt = {i: min(q[i], 1 - q[i]) for i in O}
    Uset = [i for i in O if q[i] <= mp.mpf('0.5')]; Dset = [i for i in O if q[i] > mp.mpf('0.5')]
    Lp = mp.fsum(qt.values()); Lam_p = mp.fsum(sig2[i] for i in O)
    LU = mp.fsum(qt[i] for i in Uset); LD = mp.fsum(qt[i] for i in Dset)
    LamU = mp.fsum(sig2[i] for i in Uset); LamD = mp.fsum(sig2[i] for i in Dset)
    out['Nbar_ok'] = (len(Dset) == t - 1)
    out['Lp_over_eps'] = Lp / eps; out['Lam_over_eps'] = Lam_p / eps
    bit = 1 << j0
    Econt = mp.fsum(ent(A) for A in range(1, 1 << r) if A & bit and bin(A).count('1') >= 2)
    out['E_over_Jj0'] = Econt / Ji[j0]
    R = mp.fsum(ent(A) for A in range(1, 1 << r) if not A & bit and bin(A).count('1') >= 2)
    out['R'] = R; out['R_bound'] = 22.3 * eps * LamU + 1.88 * qq * LamD
    out['R_ratio'] = R / out['R_bound'] if out['R_bound'] > 0 else (mp.mpf(0) if R == 0 else mp.inf)
    out['JU_ratio'] = min([Ji[i] / (eps * sig2[i]) for i in Uset] or [mp.inf])
    out['JD_ratio'] = min([Ji[i] / (qq * sig2[i]) for i in Dset] or [mp.inf])
    out['lhs_over_J_caseB'] = lhs / J
    return out

def rq(rng):
    u = rng.random()
    v = 10 ** -rng.uniform(0, 12) if u < 0.35 else (1 - 10 ** -rng.uniform(0, 12) if u < 0.7 else rng.uniform(0.02, 0.98))
    return min(max(v, 1e-13), 1 - 1e-13)

def caseB_instance(rng, rmax):
    r = rng.randint(2, rmax)
    nD = rng.randint(0, r - 1)            # down-type coordinates among the others
    others = []
    for k in range(r - 1):
        small = 10 ** -rng.uniform(0.7, 10)
        others.append(1 - small if k < nD else small)
    q0 = rng.choice([10 ** -rng.uniform(0, 10), rng.uniform(0.01, 0.99), 1 - 10 ** -rng.uniform(0, 10)])
    pos = rng.randint(0, r - 1)
    q = others[:pos] + [q0] + others[pos:]
    return r, nD + 1, [min(max(v, 1e-13), 1 - 1e-13) for v in q]

if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1])); T = int(sys.argv[2]); rmax = int(sys.argv[3])
    worst = {}; counts = {'A': 0, 'B': 0}; nbar_bad = 0
    keys_max = ['Lp_over_eps', 'Lam_over_eps', 'E_over_Jj0', 'R_ratio', 'lhs_over_J_caseB', 'lhs1_over_J', 'lhs_over_I']
    keys_min = ['JU_ratio', 'JD_ratio']
    for trial in range(T):
        if trial % 2 == 0:
            r, t, q = caseB_instance(rng, rmax)
        else:
            r = rng.randint(2, rmax); t = rng.randint(1, r); q = [rq(rng) for _ in range(r)]
        o = analyse(r, t, q)
        if o.get('lhs_over_J') is None: continue
        counts[o['case']] += 1
        if o['case'] == 'B' and not o['Nbar_ok']: nbar_bad += 1
        for k in keys_max:
            if k in o and o[k] is not None:
                v = float(o[k])
                if k not in worst or v > worst[k][0]: worst[k] = (v, r, t, ['%.3g' % x for x in q])
        for k in keys_min:
            if k in o and o[k] is not None and o[k] != mp.inf:
                v = float(o[k])
                if k not in worst or v < worst[k][0]: worst[k] = (v, r, t, ['%.3g' % x for x in q])
        if trial % 250 == 0: print(trial, counts, {k: round(v[0], 4) for k, v in worst.items()}, flush=True)
    print('counts', counts, 'Nbar != t-1 in case B:', nbar_bad)
    for k, v in worst.items(): print('WORST', k, v)

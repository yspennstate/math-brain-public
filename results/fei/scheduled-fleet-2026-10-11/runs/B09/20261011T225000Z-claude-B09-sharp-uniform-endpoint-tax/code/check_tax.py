# check_tax.py v1 - B09 Claude lead, 2026-10-11.
# Numerical evidence for the uniform one-bit endpoint tax theorem, plus independent
# re-implementations of A043's composition identity and A041's refresh inequality.
# Floating point is evidence only; the theorem is proved analytically in REPORT.md.
import json, math, itertools, sys, time
import numpy as np

t0 = time.time()
LOG2E = 1.0 / math.log(2.0)
out = {}

def xlog(x):
    x = np.asarray(x, dtype=float)
    with np.errstate(divide='ignore', invalid='ignore'):
        r = np.where(x > 0, -x * np.log2(np.where(x > 0, x, 1.0)), 0.0)
    return r

def h2(x):
    x = np.asarray(x, dtype=float)
    return xlog(x) + xlog(1.0 - x)

def biased_transform(F, biases):
    """F: array (..., 2,2,...,2) over the last k axes indexed by x in {0,1};
    returns orthonormal product-biased Fourier coefficients indexed by S (bit i = i in S)."""
    k = len(biases)
    A = np.array(F, dtype=float)
    lead = A.ndim - k
    for i, p in enumerate(biases):
        ax = lead + i
        a0 = np.take(A, 0, axis=ax)
        a1 = np.take(A, 1, axis=ax)
        e = (1 - p) * a0 + p * a1
        c = math.sqrt(p * (1 - p)) * (a1 - a0)
        A = np.stack([e, c], axis=ax)
    return A

def tau_bound(p):
    return 0.5 * p * math.log2(1.0 / p) + (LOG2E - 1.0) * p

def mu_tax(p):  # B09 Maassen-Uffink tax Delta(p), one bit
    return float(h2(p)) + math.log2(max(p, 1 - p))

# ---------- A2: scalar fiber minimum m(p) -----------------------------------
def fiber_sum(phi, theta):
    return h2(np.sin(phi) ** 2) + h2(np.sin(phi + theta) ** 2)

def m_of_p(p, ngrid=20001):
    # v1.1: the coarse grid missed the minimiser when theta < grid spacing (p = 2^-30 in v1);
    # a fine grid on [-2 theta, 2 theta] is merged in and refinement uses the neighbouring nodes.
    theta = math.asin(math.sqrt(p))
    phis = np.union1d(np.linspace(-math.pi / 2, math.pi / 2, ngrid), np.linspace(-2 * theta, 2 * theta, 4001))
    vals = fiber_sum(phis, theta)
    j = int(np.argmin(vals))
    lo, hi = phis[max(j - 1, 0)], phis[min(j + 1, len(phis) - 1)]
    for _ in range(200):  # golden-section refine
        a = lo + (hi - lo) * 0.381966; b = lo + (hi - lo) * 0.618034
        if fiber_sum(a, theta) < fiber_sum(b, theta): hi = b
        else: lo = a
    phi = 0.5 * (lo + hi)
    return float(fiber_sum(phi, theta)), phi, theta

A2 = []
cross = None
prev_sym_is_min = None
for p in [2.0 ** -k for k in range(30, 1, -1)] + list(np.linspace(0.26, 0.5, 25)):
    p = float(p)
    m, phi, theta = m_of_p(p)
    sym = float(2 * h2(math.sin(theta / 2) ** 2))
    endv = float(h2(p))
    taustar = float(h2(p)) - m
    row = dict(p=p, m=m, phi_opt_over_theta=phi / theta, symmetric_value=sym, endpoint_value=endv,
               tau_star=taustar, tau_bound=(tau_bound(p) if p <= math.exp(-3) else None),
               half_MU_tax=0.5 * mu_tax(p), MU_tax=mu_tax(p),
               tau_star_over_plog=(taustar / (p * math.log2(1 / p)) if p < 1 else None))
    A2.append(row)
    sym_is_min = abs(m - sym) <= 1e-7 * sym
    if prev_sym_is_min is True and sym_is_min is False and cross is None:
        cross = p
    prev_sym_is_min = sym_is_min
out['A2_fiber_minimum'] = A2
out['A2_first_grid_p_where_symmetric_point_not_min'] = cross
out['A2_checks'] = {
    'tau_star_le_tau_bound_for_p_le_e^-3': all(r['tau_star'] <= r['tau_bound'] + 1e-15 for r in A2 if r['tau_bound'] is not None),
    'tau_star_le_half_MU_tax_all_grid': all(r['tau_star'] <= r['half_MU_tax'] + 1e-12 for r in A2),
    'm_ge_symmetric_or_endpoint_min': all(r['m'] >= min(r['symmetric_value'], r['endpoint_value']) - 1e-9 for r in A2),
}

# ---------- A1: exhaustive Boolean pairs -------------------------------------
A1 = []
global_max_ratio_bound = 0.0
for nd in (1, 2, 3):
    N = 2 ** nd
    idx = np.arange(2 ** N)
    bits = ((idx[:, None] >> np.arange(N)[None, :]) & 1)
    tables = 1.0 - 2.0 * bits                      # (2^N, N): entry at integer x
    # x integer -> bit i = (x>>i)&1 ; build array with axes (x_0, ..., x_{nd-1})
    arr = np.zeros((2 ** N,) + (2,) * nd)
    for x in range(N):
        coords = tuple(((x >> i) & 1) for i in range(nd))
        arr[(slice(None),) + coords] = tables[:, x]
    for bset in ([0.5] * 3, [1/3, 0.4, 1/7], [0.1, 0.9, 0.25]):
        bs = bset[:nd]
        G = biased_transform(arr, bs).reshape(2 ** N, N)   # coefficient vectors (unit norm)
        norms = np.sum(G ** 2, axis=1)
        assert np.allclose(norms, 1.0, atol=1e-12)
        Hg = np.sum(xlog(G ** 2), axis=1)
        for p in [2.0 ** -5, 2.0 ** -7, 2.0 ** -10, 2.0 ** -14, 2.0 ** -20]:
            g = G[:, None, :]; h = G[None, :, :]
            PT = ((1 - p) * g + p * h) ** 2
            PTX = p * (1 - p) * (h - g) ** 2
            q = (1 - p) * g ** 2 + p * h ** 2
            assert np.allclose(PT + PTX, q, atol=1e-13)
            with np.errstate(divide='ignore', invalid='ignore'):
                frac = np.where(q > 0, PTX / np.where(q > 0, q, 1.0), 0.0)
            M = np.sum(q * h2(frac), axis=2)
            J = np.sum(xlog(q), axis=2) - (1 - p) * Hg[:, None] - p * Hg[None, :]
            D = J - M
            B = tau_bound(p)
            r = float(np.max(D) / B)
            global_max_ratio_bound = max(global_max_ratio_bound, r)
            imax = np.unravel_index(int(np.argmax(D)), D.shape)
            A1.append(dict(n_data=nd, data_biases=bs, p=p, pairs=int(D.size),
                           max_J_minus_M=float(np.max(D)), bound=B, max_ratio_to_bound=r,
                           max_coeff_over_plog2=float(np.max(D) / (p * math.log2(1 / p))),
                           argmax_pair=[int(imax[0]), int(imax[1])],
                           min_J_minus_M=float(np.min(D)),
                           fiber_bound_tau_star=float(h2(p)) - m_of_p(p)[0]))
out['A1_exhaustive_pairs'] = A1
out['A1_global_max_ratio_to_explicit_bound'] = global_max_ratio_bound
out['A1_total_pairs'] = int(sum(r['pairs'] for r in A1))
out['A1_all_below_bound'] = bool(global_max_ratio_bound <= 1.0 + 1e-9)
out['A1_all_below_tau_star'] = bool(all(r['max_J_minus_M'] <= r['fiber_bound_tau_star'] + 1e-12 for r in A1))

# ---------- A3: AND family, mpmath -------------------------------------------
import mpmath as mp
mp.mp.dps = 60
def mh(x):
    return mp.mpf(0) if x == 0 else -x * mp.log(x, 2)
def mh2(x):
    return mh(x) + mh(1 - x)
A3 = []
q = mp.mpf(1) / 4; v = 4 * q * (1 - q)
for k in range(3, 61):
    p = mp.mpf(2) ** (-k)
    P = [(1 - 2 * p * q) ** 2, 4 * p * (1 - p) * q ** 2, p ** 2 * v, p * (1 - p) * v]
    assert abs(sum(P) - 1) < mp.mpf(10) ** -50
    HP = sum(mh(x) for x in P)
    D = 2 * mh2(p * v) - HP - p * mh2(v)
    lead = p * mp.log(1 / p, 2)
    A3.append(dict(k=k, J_minus_M=float(D), coeff=float(D / lead),
                   remainder_over_p=float((D - lead / 2) / p),
                   explicit_upper=float(tau_bound(float(p))) if float(p) <= math.exp(-3) else None))
out['A3_AND_q_quarter'] = A3
out['A3_coeff_at_k60'] = A3[-1]['coeff']

# ---------- A4: convexity threshold of k(d)=h2(sin^2 d) and the AND at q*(p) ----------
# k''(d) = (4/ln2) (cos(2d) ln(cot d) - 1); c(d)=cos(2d) ln(cot d) is decreasing on (0, pi/4].
def cfun(d):
    return mp.cos(2 * d) * mp.log(mp.cot(d)) - 1
lo_d, hi_d = mp.mpf('0.1'), mp.mpf('0.7')
assert cfun(lo_d) > 0 and cfun(hi_d) < 0
for _ in range(200):
    mid = (lo_d + hi_d) / 2
    if cfun(mid) > 0: lo_d = mid
    else: hi_d = mid
d0 = lo_d   # largest certified-convex endpoint: cfun(d0) > 0
out['A4_convexity_d0'] = float(d0)
out['A4_convexity_p0'] = float(mp.sin(d0) ** 2)
A4 = []
for p in [mp.mpf(2) ** (-k) for k in range(2, 41)] + [mp.mpf('0.05'), mp.mpf('0.08'), mp.mpf('0.1'), mp.mpf('0.2'), mp.mpf('0.3')]:
    qs = 1 / (2 * (1 + mp.sqrt(1 - p)))
    v = 4 * qs * (1 - qs)
    P = [(1 - 2 * p * qs) ** 2, 4 * p * (1 - p) * qs ** 2, p ** 2 * v, p * (1 - p) * v]
    D = 2 * mh2(p * v) - sum(mh(x) for x in P) - p * mh2(v)
    tsym = mh2(p) - 2 * mh2((1 - mp.sqrt(1 - p)) / 2)
    pred = (1 - p * v) * tsym
    A4.append(dict(p=float(p), q_star=float(qs), J_minus_M=float(D), predicted=float(pred),
                   rel_err=float(abs(D - pred) / pred), ratio_to_tau_sym=float(D / tsym),
                   tau_sym_over_plog=float(tsym / (p * mp.log(1 / p, 2))),
                   tau_sym_second_term=float((tsym - p * mp.log(1 / p, 2) / 2) / p)))
out['A4_AND_at_q_star'] = A4
out['A4_max_rel_err'] = max(r['rel_err'] for r in A4)
out['A4_min_ratio_over_1_minus_p'] = min(r['ratio_to_tau_sym'] / (1 - r['p']) for r in A4)
out['A4_second_term_limit_predicted'] = float(mp.log(mp.e, 2) / 2 - 1)

# ---------- B: A043 composition identity -------------------------------------
rng = np.random.default_rng(20261011)
def spectrum_of_table(tab, biases):
    return biased_transform(tab, biases).ravel()
def corrected(tab, biases):
    """returns (Hplus_bits, I, Var) for sign table tab with axes x_0..x_{k-1}."""
    k = len(biases)
    co = biased_transform(tab, biases)
    Hp = 0.0; I = 0.0; V = 0.0
    for S in itertools.product((0, 1), repeat=k):
        c2 = float(co[S]) ** 2
        s = sum(S)
        if s == 0: continue
        vS = 1.0
        for i in range(k):
            if S[i]: vS *= 4 * biases[i] * (1 - biases[i])
        if c2 > 1e-300:
            Hp += c2 * math.log2(vS / c2)
        I += s * c2; V += c2
    return Hp, I, V
def table_from_func(fn, k):
    t = np.zeros((2,) * k)
    for x in itertools.product((0, 1), repeat=k):
        t[x] = fn(x)
    return t
def sgn(b): return 1.0 - 2.0 * b
gates = {
    'maj3': lambda y: sgn(1 if y[0] + y[1] + y[2] >= 2 else 0),
    'xorand': lambda y: sgn((y[0] ^ (y[1] & y[2]))),
    'thr2of4': lambda y: sgn(1 if sum(y) >= 2 else 0),
}
children = {
    'and2': (2, lambda x: 1 if (x[0] & x[1]) else 0),
    'or2': (2, lambda x: 1 if (x[0] | x[1]) else 0),
    'lit': (1, lambda x: x[0]),
    'xor2': (2, lambda x: x[0] ^ x[1]),
    'maj3c': (3, lambda x: 1 if x[0] + x[1] + x[2] >= 2 else 0),
}
B = []
combos = [('maj3', ['and2', 'lit', 'lit']), ('maj3', ['and2', 'or2', 'lit']), ('xorand', ['or2', 'and2', 'lit']),
          ('maj3', ['maj3c', 'and2', 'or2']), ('thr2of4', ['and2', 'lit', 'or2', 'lit']), ('xorand', ['xor2', 'maj3c', 'and2'])]
for gname, ch in combos:
    gate = gates[gname]
    sizes = [children[c][0] for c in ch]
    n = sum(sizes)
    pb = list(rng.uniform(0.08, 0.92, size=n))
    # child outputs as bits; their Ber parameters
    offs = np.cumsum([0] + sizes)
    def F(x):
        ys = [children[c][1](x[offs[i]:offs[i + 1]]) for i, c in enumerate(ch)]
        return gate(ys)
    tabF = table_from_func(F, n)
    HF, IF, VF = corrected(tabF, pb)
    # children
    alpha_terms = []
    eta = []
    chstats = []
    for i, c in enumerate(ch):
        k = sizes[i]
        tab = table_from_func(lambda x, c=c: sgn(children[c][1](x)), k)
        bi = pb[offs[i]:offs[i + 1]]
        # P(child bit = 1) under its inputs
        pc = sum(np.prod([bi[j] if x[j] else 1 - bi[j] for j in range(k)]) * children[c][1](x)
                 for x in itertools.product((0, 1), repeat=k))
        eta.append(float(pc))
        chstats.append(corrected(tab, bi))
    tabg = table_from_func(gate, len(ch))
    Hg, Ig, Vg = corrected(tabg, eta)
    cog = biased_transform(tabg, eta)
    w = [0.0] * len(ch)
    for S in itertools.product((0, 1), repeat=len(ch)):
        c2 = float(cog[S]) ** 2
        for i in range(len(ch)):
            if S[i]: w[i] += c2
    vch = [4 * e * (1 - e) for e in eta]
    alpha = [w[i] / vch[i] for i in range(len(ch))]
    Hpred = Hg + sum(alpha[i] * chstats[i][0] for i in range(len(ch)))
    Ipred = sum(alpha[i] * chstats[i][1] for i in range(len(ch)))
    dpred = (Ig - Vg) + sum(alpha[i] * (chstats[i][1] - chstats[i][2]) for i in range(len(ch)))
    B.append(dict(gate=gname, children=ch, n=n, Hplus=HF, Hplus_pred=Hpred, I=IF, I_pred=Ipred, Var=VF, Var_gate=Vg,
                  delta=IF - VF, delta_pred=dpred,
                  max_abs_err=max(abs(HF - Hpred), abs(IF - Ipred), abs(VF - Vg), abs((IF - VF) - dpred))))
out['B_composition_identity'] = B
out['B_all_hold'] = bool(all(r['max_abs_err'] < 1e-10 for r in B))

# ---------- C: A041 refresh inequality ---------------------------------------
C = []
viol = 0; checks = 0
for trial in range(40):
    n = int(rng.integers(3, 9))
    w = rng.uniform(0.05, 3.0, size=n)
    if trial % 4 == 0:
        w = np.round(w * 3) / 3 + 0.01  # some near-ties
    qb = rng.uniform(0.03, 0.97, size=n)
    t = float(rng.uniform(0.2, 0.8) * w.sum())
    for i in range(n):
        others = [j for j in range(n) if j != i]
        k = n - 1
        # pivotal indicator d_i on the other coordinates
        d = np.zeros((2,) * k)
        for x in itertools.product((0, 1), repeat=k):
            s = sum(w[others[j]] * x[j] for j in range(k))
            d[x] = 1.0 if (t - w[i] <= s < t) else 0.0
        bo = [float(qb[j]) for j in others]
        rho = float(np.sum(d * np.prod(np.meshgrid(*[[1 - b, b] for b in bo], indexing='ij'), axis=0)))
        if rho <= 1e-12: continue
        co = biased_transform(d, bo)
        nu = (co ** 2) / rho
        assert abs(nu.sum() - 1) < 1e-9
        for r in (1, 2, 4):
            U = [j for j in range(k) if w[others[j]] >= w[i] / r]
            L = 2 * sum(min(bo[j], 1 - bo[j]) for j in U)
            for eps in (0.25, 0.5, 1.0):
                lhs = 0.0
                for S in itertools.product((0, 1), repeat=k):
                    K = sum(S[j] for j in U)
                    lhs += float(nu[S]) * (1 - eps) ** K
                rhs = 1.0 if L == 0 else min(1.0, r / math.sqrt(eps * L))
                checks += 1
                if lhs > rhs + 1e-9:
                    viol += 1
                    C.append(dict(trial=trial, i=i, r=r, eps=eps, lhs=lhs, rhs=rhs))
out['C_refresh_checks'] = checks
out['C_refresh_violations'] = viol
out['C_violation_rows'] = C[:20]
out['runtime_s'] = time.time() - t0
json.dump(out, open(sys.argv[1], 'w'), indent=1, default=float)
print(json.dumps({k: out[k] for k in ['A2_checks', 'A2_first_grid_p_where_symmetric_point_not_min', 'A1_total_pairs',
                                      'A1_global_max_ratio_to_explicit_bound', 'A1_all_below_bound', 'A1_all_below_tau_star',
                                      'A3_coeff_at_k60', 'A4_convexity_d0', 'A4_convexity_p0', 'A4_max_rel_err',
                                      'A4_min_ratio_over_1_minus_p', 'A4_second_term_limit_predicted', 'B_all_hold', 'C_refresh_checks', 'C_refresh_violations', 'runtime_s']},
                 indent=1, default=float))

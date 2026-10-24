# B19 exact checks: shared-data identities (main.tex Prop shared-data-collision, Cor orthogonal, Maj3 example),
# disjoint composition identity (A056/A091), rank-code reduction for every Boolean f, and the
# global-order rank-code no-go on XOR of disjoint AND_L blocks. Exact Fractions; logs by mpmath interval arithmetic.
import json, sys, random, itertools, math
from fractions import Fraction as Fr
import mpmath
from mpmath import iv
iv.dps = 40
LN2 = iv.log(iv.mpf(2))


def ivq(q):
    q = Fr(q)
    return iv.mpf(q.numerator) / q.denominator


def log2q(q):
    return iv.log(ivq(q)) / LN2


def H_of(weights):  # Shannon entropy (bits) of a list of Fractions, as an interval
    s = iv.mpf(0)
    for w in weights:
        if w > 0:
            s += ivq(w) * log2q(1 / Fr(w))
    return s


def wht(tt):  # tt: list of +-1 ints, length 2^n; returns integer list c with fhat(S) = c[S]/2^n
    a = list(tt)
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return a


def spectrum(tt):
    n = len(tt)
    c = wht(tt)
    return {S: Fr(c[S] * c[S], n * n) for S in range(n) if c[S] != 0}


def infl(sp):
    return sum((w * bin(S).count('1') for S, w in sp.items()), Fr(0))


def iv_contains_zero(x, tol=mpmath.mpf('1e-30')):
    return bool(x.a <= tol and x.b >= -tol)


res = {}
rng = random.Random(20261011)


# ---------- (A) Maj3 shared-data example ----------
def maj(a, b, c):
    return 1 if a + b + c > 0 else -1


def tt_from(fun, nbits):  # bit k of the index is 1 iff y_{k+1} = -1
    out = [0] * (1 << nbits)
    for idx in range(1 << nbits):
        y = [(-1 if (idx >> k) & 1 else 1) for k in range(nbits)]
        out[idx] = fun(y)
    return out


g_plus = tt_from(lambda y: maj(y[0], y[1], y[2]), 4)
g_minus = tt_from(lambda y: maj(y[0], -y[1], y[3]), 4)


def mux(branches, a, dbits):  # selector bits are the low a bits
    N = 1 << a
    tt = [0] * (1 << (a + dbits))
    for b in range(N):
        for yi in range(1 << dbits):
            tt[b | (yi << a)] = branches[b][yi]
    return tt


F = mux([g_plus, g_minus], 1, 4)
spF = spectrum(F)
masses = sorted(spF.values())
HFm = H_of(spF.values())
res['maj3_example'] = {
    'inner_product_E[g+ g-]': str(Fr(sum(p * q for p, q in zip(g_plus, g_minus)), 16)),
    'atom_counts': {str(m): masses.count(m) for m in sorted(set(masses))},
    'H(F)_interval': [mpmath.nstr(HFm.a, 20), mpmath.nstr(HFm.b, 20)],
    'I(F)': str(infl(spF)),
    'claim_two_atoms_1/4_eight_atoms_1/16': bool(masses.count(Fr(1, 4)) == 2 and masses.count(Fr(1, 16)) == 8 and len(masses) == 10),
}


# ---------- (B) random shared-data multiplexers: identity, upper bound, influence formulas ----------
def check_mux(a, dbits, branches):
    N = 1 << a
    n = a + dbits
    tt = mux(branches, a, dbits)
    sp = spectrum(tt)
    gsp = [spectrum(g) for g in branches]
    ghat = [wht(g) for g in branches]  # integer, /2^dbits
    D = 1 << dbits
    Hg = [H_of(s.values()) for s in gsp]
    avgH = sum(Hg, iv.mpf(0)) / N
    corr = iv.mpf(0)
    ok_prob = True
    Isel_formula = Fr(0)
    for T in range(D):
        RT = Fr(sum(ghat[b][T] ** 2 for b in range(N)), N * D * D)
        if RT == 0:
            continue
        r = [Fr(ghat[b][T] ** 2, N * D * D) / RT for b in range(N)]
        nu = []
        for S in range(N):
            s = sum(((-1) ** bin(S & b).count('1')) * ghat[b][T] for b in range(N))
            nu.append(Fr(s * s, N * N * D * D) / RT)
        ok_prob &= (sum(r) == 1 and sum(nu) == 1 and all(x >= 0 for x in nu))
        for S in range(N):  # Fhat(S,T)^2 must equal R_T nu_T(S)
            if sp.get(S | (T << a), Fr(0)) != RT * nu[S]:
                ok_prob = False
        corr += ivq(RT) * (H_of(nu) - H_of(r))
        Isel_formula += RT * sum(bin(S).count('1') * nu[S] for S in range(N))
    HF = H_of(sp.values())
    ident = HF - (a + avgH + corr)
    upper_ok = bool(HF.b <= (2 * a + avgH).a + mpmath.mpf('1e-30'))
    Isel = sum((w * bin(S & (N - 1)).count('1') for S, w in sp.items()), Fr(0))
    Idata = sum((w * bin(S >> a).count('1') for S, w in sp.items()), Fr(0))
    Idata_formula = sum((infl(s) for s in gsp), Fr(0)) / N
    infl_sel_ok = True
    for j in range(a):
        direct = Fr(sum(1 for z in range(1 << n) if tt[z] != tt[z ^ (1 << j)]), 1 << n)
        formula = sum((Fr(sum(1 for yi in range(D) if branches[b][yi] != branches[b ^ (1 << j)][yi]), D)
                       for b in range(N)), Fr(0)) / N
        spec = sum((w for S, w in sp.items() if (S >> j) & 1), Fr(0))
        infl_sel_ok &= (direct == formula == spec)
    return {'prob_vectors_and_coefficients': ok_prob, 'identity_eq_shared_data_collision': iv_contains_zero(ident),
            'upper_2a_plus_avgH': upper_ok, 'Isel_spectral_formula': Isel == Isel_formula,
            'Idata_formula': Idata == Idata_formula, 'selector_influence_formula': infl_sel_ok}


agg = {}
nmux = 0
for (a, dbits, reps) in [(1, 2, 60), (1, 3, 60), (2, 2, 40), (2, 3, 40), (3, 2, 15)]:
    for _ in range(reps):
        N = 1 << a
        D = 1 << dbits
        branches = []
        for b in range(N):
            t = rng.random()
            if t < 0.15:
                g = [rng.choice([1, -1])] * D  # constant branch
            else:
                g = [rng.choice([1, -1]) for _ in range(D)]
            branches.append(g)
        r = check_mux(a, dbits, branches)
        nmux += 1
        for k, v in r.items():
            agg[k] = agg.get(k, 0) + (1 if v else 0)
r = check_mux(1, 4, [g_plus, g_minus])
nmux += 1
for k, v in r.items():
    agg[k] = agg.get(k, 0) + (1 if v else 0)
res['shared_data_random'] = {'multiplexers': nmux, 'passes_per_check': agg}

ok = True  # orthogonality <=> disagreement 1/2 for +-1 functions: E[gg'] = 1 - 2 P[g != g']
for t1 in range(256):
    for t2 in range(256):
        g1 = [1 - 2 * ((t1 >> i) & 1) for i in range(8)]
        g2 = [1 - 2 * ((t2 >> i) & 1) for i in range(8)]
        e = Fr(sum(x * y for x, y in zip(g1, g2)), 8)
        pdis = Fr(sum(1 for x, y in zip(g1, g2) if x != y), 8)
        ok &= (e == 1 - 2 * pdis)
res['orthogonal_iff_disagreement_half_all_3bit_pairs'] = ok


# ---------- (C) disjoint composition identity under induced bias (A056/A091) ----------
def comp_check(k, sizes):
    while True:
        fs = [[rng.choice([1, -1]) for _ in range(1 << s)] for s in sizes]
        if all(len(set(f)) > 1 for f in fs):
            break
    g = [rng.choice([1, -1]) for _ in range(1 << k)]
    offs = [sum(sizes[:i]) for i in range(k)]
    n = sum(sizes)
    tt = []
    for x in range(1 << n):
        z = 0
        for i in range(k):
            xi = (x >> offs[i]) & ((1 << sizes[i]) - 1)
            if fs[i][xi] == -1:
                z |= (1 << i)
        tt.append(g[z])
    sp = spectrum(tt)
    fsp = [spectrum(f) for f in fs]
    m = [Fr(sum(f), len(f)) for f in fs]
    v = [1 - mi * mi for mi in m]
    gnu = {}
    for A in range(1 << k):
        s = Fr(0)
        for z in range(1 << k):
            p = Fr(1)
            prod = Fr(1)
            for i in range(k):
                zi = -1 if (z >> i) & 1 else 1
                p *= (1 + m[i]) / 2 if zi == 1 else (1 - m[i]) / 2
                if (A >> i) & 1:
                    prod *= (zi - m[i])
            s += p * g[z] * prod
        den = Fr(1)
        for i in range(k):
            if (A >> i) & 1:
                den *= v[i]
        if s != 0:
            gnu[A] = s * s / den
    ok_coeff = (sum(gnu.values()) == 1)
    for S in range(1 << n):
        A = 0
        Ts = []
        for i in range(k):
            Ti = (S >> offs[i]) & ((1 << sizes[i]) - 1)
            if Ti:
                A |= (1 << i)
            Ts.append(Ti)
        val = gnu.get(A, Fr(0))
        for i in range(k):
            if Ts[i]:
                val *= fsp[i].get(Ts[i], Fr(0)) / v[i]
        if sp.get(S, Fr(0)) != val:
            ok_coeff = False
    a_i = [sum((w for A, w in gnu.items() if (A >> i) & 1), Fr(0)) / v[i] for i in range(k)]

    def h2(x):
        return H_of([x, 1 - x])
    rhs = H_of(gnu.values()) + sum((ivq(a_i[i]) * (H_of(fsp[i].values()) - h2(v[i])) for i in range(k)), iv.mpf(0))
    ent_ok = iv_contains_zero(H_of(sp.values()) - rhs)
    infl_ok = infl(sp) == sum((a_i[i] * infl(fsp[i]) for i in range(k)), Fr(0))
    var_ok = (1 - sp.get(0, Fr(0))) == (1 - gnu.get(0, Fr(0)))
    a_le_1 = all(0 <= x <= 1 for x in a_i)
    return {'squared_coefficient_product_formula': ok_coeff, 'entropy_identity': ent_ok,
            'influence_identity': infl_ok, 'variance_identity': var_ok, 'multipliers_in_[0,1]': a_le_1}


cagg = {}
ncomp = 0
for (k, sizes, reps) in [(2, [2, 2], 40), (2, [2, 3], 30), (3, [2, 2, 2], 25), (3, [1, 2, 3], 15)]:
    for _ in range(reps):
        r = comp_check(k, sizes)
        ncomp += 1
        for kk, vv in r.items():
            cagg[kk] = cagg.get(kk, 0) + (1 if vv else 0)
res['disjoint_composition_biased'] = {'compositions': ncomp, 'passes_per_check': cagg}

# ---------- (D) rank-code reduction for every Boolean f, every order ----------
CLEV = iv.log(4 + iv.e) / LN2
LPI = iv.log(iv.pi ** 2 / 4) / LN2
LNQ = {(p, j): iv.log(iv.mpf(p) / j) for p in range(1, 17) for j in range(1, 17)}


def rank_cost(sp, order_pos, n):  # R_pi = E sum_j ln(i_j / j), order_pos[c] = 1-based position of coordinate c
    R = iv.mpf(0)
    for S, w in sp.items():
        pos = sorted(order_pos[c] for c in range(n) if (S >> c) & 1)
        s = iv.mpf(0)
        for j, p in enumerate(pos, 1):
            if p != j:
                s += LNQ[(p, j)]
        R += ivq(w) * s
    return R


red_ok = 0
red_n = 0
min_slack = None
for n in (3, 4):
    for _ in range(120 if n == 4 else 60):
        tt = [rng.choice([1, -1]) for _ in range(1 << n)]
        sp = spectrum(tt)
        I = infl(sp)
        HF = H_of(sp.values())
        for perm in itertools.permutations(range(n)):
            pos = {c: perm.index(c) + 1 for c in range(n)}
            bound = (CLEV + LPI) * ivq(I) + 2 / LN2 * rank_cost(sp, pos, n)
            red_n += 1
            if HF.b <= bound.a:
                red_ok += 1
            sl = bound.a - HF.b
            min_slack = sl if min_slack is None or sl < min_slack else min_slack
res['rank_code_reduction_random_f'] = {'pairs_(f,order)': red_n, 'holds': red_ok, 'min_slack_bits': mpmath.nstr(min_slack, 8)}


# ---------- (E) global-order no-go: f = XOR of m disjoint AND_L blocks ----------
def and_spec(L):  # squared coefficients of AND_L in +-1 convention
    return {T: (Fr((2 ** L - 2) ** 2, 4 ** L) if T == 0 else Fr(4, 4 ** L)) for T in range(1 << L)}


def xor_and_spec(m, L):
    base = and_spec(L)
    sp = {0: Fr(1)}
    for b in range(m):
        new = {}
        for S, w in sp.items():
            for T, u in base.items():
                new[S | (T << (b * L))] = w * u
        sp = new
    return sp


def LB(m, L):  # 2^(1-L) * sum_p max{0, ln p - ln((L+1)/2 + (p-1) 2^(1-L))}; returns an interval whose .b is a valid upper end
    q = Fr(2, 2 ** L)
    s = iv.mpf(0)
    for p in range(1, m * L + 1):
        val = iv.log(iv.mpf(p)) - iv.log(ivq(Fr(L + 1, 2) + (p - 1) * q))
        if val.b > 0:
            s += iv.mpf([max(val.a, 0), val.b])
    return ivq(q) * s


nogo = []
for (m, L) in [(2, 2), (3, 2), (2, 3)]:
    sp = xor_and_spec(m, L)
    n = m * L
    I = infl(sp)
    assert I == m * L * Fr(2, 2 ** L)
    best = None
    for perm in itertools.permutations(range(n)):
        pos = {c: perm.index(c) + 1 for c in range(n)}
        R = rank_cost(sp, pos, n)
        if best is None or R.a < best.a:
            best = R
    lb = LB(m, L)
    nogo.append({'m': m, 'L': L, 'orders': math.factorial(n), 'I': str(I), 'min_over_orders_R_lower': mpmath.nstr(best.a, 10),
                 'LB_upper': mpmath.nstr(lb.b, 10), 'min_R_ge_LB': bool(best.a >= lb.b),
                 'H/I': mpmath.nstr((H_of(sp.values()) / ivq(I)).b, 8)})
res['nogo_exhaustive_small'] = nogo


# asymptotic lower bound per unit influence via the integral (phi increasing):
#   R/I >= (1/M) * int_{t0}^{M} [ln t - ln(c - q + q t)] dt,  c = (L+1)/2, q = 2^(1-L), t0 = (c-q)/(1-q), M = mL
def asym(L, M):
    q = iv.mpf(2) / iv.mpf(2) ** L
    c = iv.mpf(L + 1) / 2
    t0 = (c - q) / (1 - q)
    Mi = iv.mpf(M)

    def F1(t):
        return t * iv.log(t) - t

    def F2(t):
        u = c - q + q * t
        return (u * iv.log(u) - u) / q
    integral = (F1(Mi) - F1(t0)) - (F2(Mi) - F2(t0))
    return integral / Mi


rows = []
for L in (4, 8, 12, 16, 24, 32):
    a0 = Fr((2 ** L - 2) ** 2, 4 ** L)
    HA = H_of([a0]) + ivq((2 ** L - 1) * Fr(4, 4 ** L)) * log2q(Fr(4 ** L, 4))
    hratio = HA / ivq(L * Fr(2, 2 ** L))
    for M_exp in (9, 15):
        M = 10 ** M_exp
        lbI = asym(L, M)
        rows.append({'L': L, 'M=mL': '1e%d' % M_exp, 'R/I_lower': mpmath.nstr(lbI.a, 8),
                     '(L-1)ln2': mpmath.nstr((L - 1) * mpmath.log(2), 8),
                     'rank_term_(2/ln2)R/I_lower': mpmath.nstr((2 / LN2 * lbI).a, 8),
                     'H/I_of_f_upper': mpmath.nstr(hratio.b, 8)})
res['nogo_asymptotic'] = rows
json.dump(res, open(sys.argv[1], 'w', encoding='utf-8'), indent=1, default=str)
print(json.dumps(res, indent=1, default=str))
